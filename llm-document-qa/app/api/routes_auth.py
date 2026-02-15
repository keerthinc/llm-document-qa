from fastapi import APIRouter
from jose import jwt
from app.config import SECRET_KEY

router = APIRouter()

@router.post("/login")
def login(username: str):
    token = jwt.encode({"user": username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
