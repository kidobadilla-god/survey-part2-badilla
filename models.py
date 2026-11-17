from sqlmodel import Field , SQLModel

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






