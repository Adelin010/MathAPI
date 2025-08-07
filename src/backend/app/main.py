from fastapi import FastAPI
import os 
from dotenv import load_dotenv, dotenv_values
from routes.routes import router
from contextlib import asynccontextmanager
from redis.asyncio import Redis

# local imports 
from cache.cache import redis_pool


@asynccontextmanager
async def lifespan(app:FastAPI):
    app.state.redis = Redis(connection_pool = redis_pool)
    print(await app.state.redis.ping())
    yield
    await app.state.redis.close()


load_dotenv()
REDIS_URL = os.getenv('REDIS_URL')
app = FastAPI(lifespan=lifespan)
app.include_router(router=router)




