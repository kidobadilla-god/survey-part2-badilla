from fastapi import FastAPI
from requests import session
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware
import hashlib
from models import Survey , UserLogin , UserRegister

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/Survey/{id}")
async def read_Survey(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        users = session.get(Survey, id)
        return {"message": users}
    

@app.post("/Survey")
async def root(Survey  : Survey):
    with Session(engine) as session:
        session.add(Survey)
        session.commit()
        session.refresh(Survey)
        return {"message": Survey}

@app.post("UserRegister/")
async def user_register(UserRegister  : UserRegister):
    with Session(engine) as session:
        hashed = hashlib.sha256(UserRegister.password.encode()).hexdigest()
        UserRegister.password = hashed
        session.add(UserRegister)
        session.commit()
        session.refresh(UserRegister)
        return {"message": UserRegister}

@app.post("Userlogin/")
async def user_login(Userlogin  : user_login):
    with Session(engine) as session:
        existing_user = session.exec(select(Userlogin).where(Userlogin.username == Userlogin.username)).first()
        if not existing_user:
            return {'Message': 'User not Found'}
        input_hashed = hashlib.sha256(Userlogin.password.encode()).hexdigest()
        if existing_user.password == input_hashed:
            print("login success")
        session.add(Userlogin)
        session.commit()
        session.refresh(Userlogin)
        return {"message": Userlogin}


@app.get("/Userlogin/{id}")
async def user_login(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        users = session.get(UserLogin, id)
        return {"message": users}
    

