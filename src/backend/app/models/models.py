from pydantic import BaseModel, Field
from datetime import datetime

# for the models  we have to match the fields in name, mostly like a database entity
class Req2Int(BaseModel):
    n: int
    m: int 


class Req1Int(BaseModel):
    n: int


class HistoryRecord(BaseModel):
    id: int
    func_name: str
    nr_params: int
    params_name: str
    params_value: str
    date: str = Field(str(datetime.now()))

class User(BaseModel):
    name: str
    email: str
    password: str
    date: str = Field(default=str(datetime.now()))


class Credentials(BaseModel):
    email: str
    password: str 

    
    def values(self) -> list[str]:
        return [self.email, self.password]

class AuthToken(BaseModel):
    token: str
    token_type: str
