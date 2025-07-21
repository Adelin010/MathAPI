from utils import algorithms as alg
from sqlite3 import connect, Error as sqlError
from datetime import datetime
from fastapi import FastAPI


class Service: 

    def __init__(self, db_path: str)-> None:
        self.db_path = db_path
        


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


    async def __cach_result(*, redis, key: str, val: int, exp: int = 7200):
        if not redis:
            raise Exception("Cache ref not initialised in the Math_Service...")
        await redis.set(key, val, exp)

    async def __extract_cach(*, redis,  key: str) -> str | None:
        return await redis.get(key)
    
    def print_db(self) -> None:
        try:    
            connection = connect(self.db_path, check_same_thread=False)
            print('Connection established...')
            
            cursor = connection.cursor()
            query = 'select * from history'
            cursor.execute(query)
            print(cursor.fetchall())
        except sqlError as err:
            print('Error occured when trying to connect with the database for adding entry...\n', err)
        finally:
            if connection:
                connection.close()
                print('Connection to the DB closed...')



    async def fibo(self,*, redis, n: int) -> int:
        self.__add_to_db('fibo', 1, 'n', str(n))

        # fiunding the value in the cach 
        val = await Service.__extract_cach(redis=redis, key=f'fibo_{n}')
        if val :
            print('################No Cached')
            return int(val) 
        # Otherwise compute and save the value
        res = alg.fibo(n = n)
        if res > 100000:
            print('############## Cached')
            await Service.__cach_result(redis=redis, key=f'fibo_{n}', val=res)
        return res
    
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

    def cmmdc(self, *, n: int, m: int) -> int:
        self.__add_to_db('cmmdc', 2, 'n,m', f'{n},{m}')
        return alg.cmmdc(n, m)

    def cmmmc(self, *, n: int, m: int) -> int:
        self.__add_to_db('cmmmc', 2, 'n, m', f'{n},{m}')
        return alg.cmmmc(n, m)

    async def fact(self, *, redis,  n: int) -> int:
        self.__add_to_db('fact', 1, 'n', str(n))

        val = await Service.__extract_cach(redis=redis, key=f'fact_{n}')
        if val :
            print('################No Cached')
            return int(val) 
        
        res = alg.fact(n)
        if res > 100000:
            await Service.__cach_result(redis=redis, key=f'fact_{n}', val=res)
        return res
    
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
