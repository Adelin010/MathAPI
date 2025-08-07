from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse, PlainTextResponse
from fastapi import status
import os
from dotenv import load_dotenv

# local imports
from services.math_serv import Service as MathServ
from models import models as mod
from services.auth_serv import Service as AuthServ

# enivronment variables
load_dotenv()
DB_URL = os.getenv('DB_URL')

# router setup
router = APIRouter()
math_serv = MathServ(DB_URL)
auth_serv = AuthServ(DB_URL)

# basic route redirected to math_formulas in case someone tries to access the root
@router.get('/')
async def base(request: Request):

    return RedirectResponse('/math_formulas', status_code=status.HTTP_303_SEE_OTHER)

# The route of the api 
@router.get('/math_formulas', response_class=JSONResponse, tags=['landing'])
async def landing_page():
    return math_serv.get_whole_db()

# singin route for the new users 
@router.post('/signin', response_class=JSONResponse, tags=['signin'])
async def signin(user: mod.User):
    auth_serv.add_user(user)
    return {'action_status': 'executed...'}

# a simple read of the users' database for ease of testing
@router.get('/users', response_class=JSONResponse, tags=['users'])
async def view_users(): 
    return auth_serv.get_user(name = 'Alex') 

# authentication route for the users
@router.post('/auth', response_class=JSONResponse, tags=['auth'])
async def auth(credentials: mod.Credentials):
    return auth_serv.login(credentials)

# JWT token for verifyng the current user
@router.post('/auth_current_user', response_class=PlainTextResponse, tags=['current_user'])
async def current_user(req: Request):
    token = req.headers.get('token')
    token_type = req.headers.get('token_type')
    user_as_list = auth_serv.get_user_through_token(token)
    print(user_as_list)
    return "All good..."


# Fibo route to get the nth Fibonacci number
# expected parameter: n (int)
@router.post('/math_formulas/fibo', response_class=JSONResponse, tags=['fibo'])
async def fibo(req: Request, body: mod.Req1Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')
    
    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"FIBO": await math_serv.fibo(**dict_body)}

# Factorial route to get the factorial of a number
# expected parameter: n (int)
@router.post('/math_formulas/fact', response_class=JSONResponse, tags=['fact'])
async def fact(req: Request, body: mod.Req1Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')

    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"FACT": await math_serv.fact(**dict_body)}

# Gama sum route to get the sum of the first n natural numbers
# expected parameter: n (int)
@router.post('/math_formulas/gama_sum', response_class=JSONResponse, tags=['gama_sum'])
async def gama_sum(req: Request, body: mod.Req1Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')

    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"FIBO": await math_serv.gama_sum(**dict_body)}


# Power route to get the power of a number
# expected parameters: n (int), m (int)
@router.post('/math_formulas/pow', response_class=JSONResponse, tags=['pow'])
async def pow(req: Request, body: mod.Req2Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')

    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"POW": await math_serv.pow(**dict_body)}

# CMMDC route to get the greatest common divisor of two numbers
# expected parameters: n (int), m (int)
@router.post('/math_formulas/cmmmc', response_class=JSONResponse, tags=['cmmmc'])
async def cmmmc(req: Request, body: mod.Req2Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')

    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"CMMMC": await math_serv.cmmmc(**dict_body)}

# CMMDC route to get the least common multiple of two numbers
# expected parameters: n (int), m (int)
@router.post('/math_formulas/cmmdc', response_class=JSONResponse, tags=['cmmdc'])
async def cmmdc(req: Request, body: mod.Req2Int):
    redis_ref = req.app.state.redis
    token = req.headers.get('token')

    auth_serv.get_user_through_token(token)

    dict_body = body.model_dump()
    dict_body.update({"redis": redis_ref})
    return {"CMMDC": await math_serv.cmmdc(**dict_body)}

