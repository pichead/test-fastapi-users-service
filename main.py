import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

load_dotenv()

Base = declarative_base()


app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

cors_config = {
    "allow_origin_regex": ".*",
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

app.add_middleware(
    CORSMiddleware,
    **cors_config
)

db_config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"


db_engine = create_engine(db_url)
db = Session(db_engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=db_engine)


print("swagger ui: http://localhost:8000/docs")
print("server is running http://localhost:8000")

class UserCreate(BaseModel):
    username: str
    email: str


@app.get("/")
def read_root():
    return {
        "statusCode": 200,
        "message": "Welcome to FastAPI server : Test api",
    }


@app.get("/users")
def all_users():
    try:
        user = db.query(User).all()
        return {
            "statusCode": 200,
            "message": "User created successfully",
            "data": user,
        }
    except Exception:
        return {
            "statusCode": 500,
            "message": "Internal server error",
        }


@app.post("/users")
def create_user(body: UserCreate):

    try:
        user = User(username=body.username, email=body.email)
        db.add(user)
        db.commit()
    except IntegrityError:
        db.rollback()
        return {
            "statusCode": 400,
            "message": "Username or email already exists",
        }

    return {
        "statusCode": 200,
        "message": "User created successfully",
        "data": {
            "username": body.username,
            "email": body.email,
        },
    }


@app.get("/users/{user_id}")
def find_user_by_id(user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return {
                "statusCode": 404,
                "message": "User not found",
            }
        return {
            "statusCode": 200,
            "message": "data found",
            "data": user,
        }
    except Exception:
        return {
            "statusCode": 500,
            "message": "Internal server error",
        }



if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=int(os.getenv("PORT", 8000)), reload=True
    )

