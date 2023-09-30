from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, APIRouter, HTTPException, status, WebSocketException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db import get_db, ActiveSession
from models.user import User
from models.doctor import Doctor
from settings import *
import random
from sqlalchemy.orm import joinedload
from models.queue import Queue, now_sanavaqt

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_router = APIRouter(tags=["Xavsizlik"])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return False
    return user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_ws_active_user(token: str, db: Session = ActiveSession):
    
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username:
        token_data = TokenData(username=username)
        user = get_user(username=token_data.username, db=db)

        if user:
            return user


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    u_count = db.query(User).count()
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials__{u_count}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, db=db)
    if not user:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(400, "Inactive user")
    
    if current_user.disabled:
        raise HTTPException(400, "Inactive user")
    return current_user

@auth_router.get("/me")
async def get_me(usr: UserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    user = db.query(User).options(joinedload(User.doctors).subqueryload(Doctor.service)).filter_by(id=usr.id).first()
    return user


@auth_router.get("/queue_number", tags=['Queue Endpoint'])
async def get_queue_number(room_number:int, db:Session = ActiveSession):

    currque = db.query(Queue).filter(Queue.room==room_number, Queue.step==3, Queue.date==now_sanavaqt.strftime("%Y-%m-%d")).order_by(Queue.number.asc()).first()

    if currque:
        return currque.number
    else:
        return 0


@auth_router.post("/token", description="Bu joy login qilish uchun kerak boladi")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
   
   
    user = authenticate_user(form_data.username, form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "user": user}





