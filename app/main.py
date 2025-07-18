from fastapi import FastAPI
import os 
from dotenv import load_dotenv, dotenv_values

from routes.routes import router

app = FastAPI()
app.include_router(router=router)


