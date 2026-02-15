import redis
from app.config import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def save_message(session_id, message):
    r.rpush(session_id, message)

def get_memory(session_id):
    return [m.decode() for m in r.lrange(session_id, 0, -1)]
