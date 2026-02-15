import requests
import hashlib
import redis
from fastapi.responses import StreamingResponse
from app.config import OLLAMA_URL, OLLAMA_MODEL, REDIS_HOST, REDIS_PORT

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)

def generate(prompt):

    key = hashlib.md5(prompt.encode()).hexdigest()

    if cache.exists(key):
        return cache.get(key).decode()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]
    cache.set(key, answer)

    return answer

def stream(prompt):

    def generator():
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )

        for line in response.iter_lines():
            if line:
                yield line.decode() + "\n"

    return StreamingResponse(generator(), media_type="text/plain")
