from pydantic import BaseModel, Field
from datetime import datetime

class AuthToken(BaseModel):
    token: str
    token_type: str

# Models use in the Request body parsing 
# In the context of mathematical operations we diferenciate between
# requests with one integer parameter and requests with two integer parameters
class Req2Int(BaseModel):
    n: int
    m: int 


class Req1Int(BaseModel):
    n: int


# The HistoryRecord is used to parse the entity of the history table 
# In which we store the order-call of the mathematical operations
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


