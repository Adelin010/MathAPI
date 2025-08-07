from utils import algorithms as alg
from sqlite3 import connect, Error as sqlError
from datetime import datetime
from fastapi import FastAPI


class Service: 

    # constructor gets the database path
    # stores it for the future connections
    # to the database
    # db_path: str - the path to the database
    def __init__(self, db_path: str)-> None:
        self.db_path = db_path
        
    # private method to add an entry to the history table
    # func_name: str - the name of the function
    # nr_params: int - the number of parameters
    # params_name: str - the name of the parameters
    # params_value: str - the value of the parameters
    def __add_to_db(self, func_name: str, nr_params: int, params_name: str, params_value: str) -> None:
        try:
            connection = connect(self.db_path, check_same_thread=False)
            print('Connection established...') 

            cursor = connection.cursor()
            query = f'insert into history(func_name, nr_params, params_name, params_value, date) values(?, ?, ?, ?, ?)'
            cursor.execute(query, (func_name, nr_params, params_name, params_value, str(datetime.now())))
            connection.commit()
            print('Insertion statement completly run...')

        except sqlError as err:
            print('Error occured when trying to connect with the database for adding entry...\n', err)
        finally:
            if connection:
                connection.close()
                print('Connection to the DB closed...')

    # private method to cache the result of a computation
    # redis: Redis - the redis connection
    # key: str - the key under which the result is stored
    # val: int - the value to be cached 
    # exp: int - the expiration time in seconds (default is 7200 seconds)
    @staticmethod
    async def __cach_result(*, redis, key: str, val: int, exp: int = 7200):
        if not redis:
            raise Exception("Cache ref not initialised in the Math_Service...")
        await redis.set(key, val, exp)

    # private method to extract a value from the cache
    # redis: Redis - the redis connection
    # key: str - the key under which the value is stored
    @staticmethod
    async def __extract_cach(*, redis,  key: str) -> str | None:
        return await redis.get(key)
    
    # method to get the whole database
    # returns a list of all entries in the history table
    # or None if the connection fails
    # returns: list[any] | None - the list of all entries in the history table
    # or None if the connection fails
    def get_whole_db(self) -> list[any] | None:
        try:    
            connection = connect(self.db_path, check_same_thread=False)
            print('Connection established...')
            
            cursor = connection.cursor()
            query = 'select * from history'
            cursor.execute(query)
            return cursor.fetchall()
        except sqlError as err:
            print('Error occured when trying to connect with the database for adding entry...\n', err)
        finally:
            if connection:
                connection.close()
                print('Connection to the DB closed...')


    # method to get the nth Fibonacci number
    # redis: Redis - the redis connection
    # n: int - the index of the Fibonacci number to be computed
    # returns: int - the nth Fibonacci number
    # or None if the connection fails
    # or if the value is not cached
    # raises: Exception - if the redis connection is not initialized
    async def fibo(self,*, redis, n: int) -> int:
        self.__add_to_db('fibo', 1, 'n', str(n))

        # fiunding the value in the cach 
        val = await Service.__extract_cach(redis=redis, key=f'fibo_{n}')
        if val :
            print('################No Cached')
            return int(val) 
        # Otherwise compute and save the value
        # res = alg.fibo(n = n)
        res = 0
        for i in range(n):
            res = alg.fibo(n=i)
            await Service.__cach_result(redis=redis, key=f'fibo_{i}', val=res)
        return res
    
    # method to compute the power of a number
    # redis: Redis - the redis connection       
    # n: int - the base number
    # m: int - the exponent
    # returns: int - the result of n raised to the power of m
    # or None if the connection fails
    async def pow(self, *, redis, n: int, m: int) -> int:
        self.__add_to_db('pow', 2, 'n,m', f'{n},{m}')

        val = await Service.__extract_cach(redis=redis, key=f'pow_{n}')
        if val :
            print('################No Cached')
            return int(val) 

        res = alg.pow(n, m)
        if res > 100000:
            await Service.__cach_result(redis=redis, key=f'pow_{n}', val=res)
        return res

    # method to compute the greatest common divisor of two numbers
    # n: int - the first number
    # m: int - the second number
    async def cmmdc(self, *,redis,  n: int, m: int) -> int:
        self.__add_to_db('cmmdc', 2, 'n,m', f'{n},{m}')

        val = await Service.__extract_cach(redis=redis, key=f'cmmdc_{n}')
        if val :
            print('################No Cached')
            return int(val) 

        res = alg.cmmdc(n, m)
        if res > 100000:
            await Service.__cach_result(redis=redis, key=f'cmmdc_{n}', val=res)
        return res
    

    # method to compute the least common multiple of two numbers
    # n: int - the first number
    # m: int - the second number
    async def cmmmc(self, *, redis , n: int, m: int) -> int:
        self.__add_to_db('cmmmc', 2, 'n, m', f'{n},{m}')

        val = await Service.__extract_cach(redis=redis, key=f'cmmmc_{n}')
        if val :
            print('################No Cached')
            return int(val) 

        res =  alg.cmmmc(n, m)
        if res > 100000:
            await Service.__cach_result(redis=redis, key=f'cmmmc_{n}', val=res)
        return res


    # method to compute the factorial of a number
    # redis: Redis - the redis connection
    # n: int - the number for which the factorial is computed
    async def fact(self, *, redis,  n: int) -> int:
        self.__add_to_db('fact', 1, 'n', str(n))

        val = await Service.__extract_cach(redis=redis, key=f'fact_{n}')
        if val :
            print('################No Cached')
            return int(val) 
        
        res = 0
        for i in range(n):
            res = alg.fact(i)
            await Service.__cach_result(redis=redis, key=f'fact_{i}', val=res)
        return res
    
    # method to compute the sum of the first n natural numbers
    # redis: Redis - the redis connection
    # n: int - the number of natural numbers to be summed
    async def gama_sum(self, *, redis, n: int) -> int:
        self.__add_to_db('gama_sum', 1, 'n', str(n))

        val = await Service.__extract_cach(redis=redis, key=f'gama_sum_{n}')
        if val:
            print('##################### No Cache')
            return int(val)

        res = alg.gama_sum(n)
        if res > 100000:
            await Service.__cach_result(redis= redis, key=f'gama_sum_{n}', val=res)
        return res
