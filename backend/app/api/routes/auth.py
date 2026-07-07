from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.db.base import SessionLocal
from app.db.models import User
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserCreate(BaseModel):
    email: str
    password: str

@router.post('/signup')
def signup(payload: UserCreate):
    db = SessionLocal()
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')
    user = User(email=payload.email, hashed_password=pwd_context.hash(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'email': user.email, 'id': user.id}

class LoginPayload(BaseModel):
    email: str
    password: str

@router.post('/login')
def login(payload: LoginPayload):
    db = SessionLocal()
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not pwd_context.verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    return {'message': 'Login successful', 'user_id': user.id}
