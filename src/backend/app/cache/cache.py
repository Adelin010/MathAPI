from  redis.asyncio import ConnectionPool, Redis
import os 
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("CACHE_HOST", "redis")
port = os.getenv("CHACE_PORT", 6379)


redis_pool = ConnectionPool(host='localhost', port=port, db=0, decode_responses=True)
    
