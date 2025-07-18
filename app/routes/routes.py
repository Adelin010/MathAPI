from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse, PlainTextResponse
from fastapi import status
import os
from dotenv import load_dotenv

# local imports
from services.math_serv import Service as MathServ
from models import models as mod
from services.auth_serv import Service as AuthServ

load_dotenv()
DB_URL = os.getenv('DB_URL')

router = APIRouter()
math_serv = MathServ(DB_URL)
auth_serv = AuthServ(DB_URL)


@router.get('/')
async def base():
    math_serv.print_db()
    return RedirectResponse('/math_formulas', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/math_formulas', response_class=JSONResponse, tags=['landing'])
async def landing_page():
    return {"msg": "A correct request..."}


@router.post('/signin', response_class=JSONResponse, tags=['signin'])
async def signin(user: mod.User):
    auth_serv.add_user(user)
    return {'action_status': 'executed...'}

@router.get('/users', response_class=JSONResponse, tags=['users'])
async def view_users(): 
    return auth_serv.get_user(name = 'Alex') 

@router.post('/auth', response_class=JSONResponse, tags=['auth'])
async def auth(credentials: mod.Credentials):
    return auth_serv.login(credentials)

@router.post('/auth_current_user', response_class=PlainTextResponse, tags=['current_user'])
async def current_user(token: mod.AuthToken):
    dict_token = token.model_dump()
    token_str = dict_token['token']
    user_as_list = auth_serv.get_user_through_token(token_str)
    print(user_as_list)
    return "All good..."



@router.post('/math_formulas/fibo', response_class=JSONResponse, tags=['fibo'])
async def fibo(body: mod.Req1Int):
    
    dict_body = body.model_dump()
    return {"FIBO": math_serv.fibo(**dict_body)}


@router.post('/math_formulas/fact', response_class=JSONResponse, tags=['fact'])
async def fact(body: mod.Req1Int):

    dict_body = body.model_dump()
    return {"FACT": math_serv.fact(**dict_body)}


@router.post('/math_formulas/gama_sum', response_class=JSONResponse, tags=['gama_sum'])
async def gama_sum(body: mod.Req1Int):
    
    dict_body = body.model_dump()
    return {"FIBO": math_serv.gama_sum(**dict_body)}



@router.post('/math_formulas/pow', response_class=JSONResponse, tags=['pow'])
async def pow(body: mod.Req2Int):

    dict_body = body.model_dump()
    print(dict_body)
    return {"POW": math_serv.pow(**dict_body)}


@router.post('/math_formulas/cmmmc', response_class=JSONResponse, tags=['cmmmc'])
async def cmmmc(body: mod.Req2Int):

    dict_body = body.model_dump()
    return {"CMMMC": math_serv.cmmmc(**dict_body)}


@router.post('/math_formulas/cmmdc', response_class=JSONResponse, tags=['cmmdc'])
async def cmmdc(body: mod.Req2Int):

    dict_body = body.model_dump()
    return {"CMMDC": math_serv.cmmdc(**dict_body)}

