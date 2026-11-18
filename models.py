from sqlmodel import Field , SQLModel , hashlib

class Survey(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    first_name: str
    sur_name: str
    middle_name: str
    suffix: str|None = None
    birthday_date: str
    age: int
    where: str
    place: str
    civil_status: str
    religion: str

class UserLogin(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    username: str
    password: str
    
class UserRegister(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    username: str
    password: str
    Confirmed_password: str
    



