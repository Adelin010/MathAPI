from  redis.asyncio import ConnectionPool, Redis
import os 
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("REDIS_HOST")
port = os.getenv("REDIS_PORT")
redis_pool = ConnectionPool(host=host, port=port, db=0, decode_responses=True)
