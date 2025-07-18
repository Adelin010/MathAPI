from utils import algorithms as alg
from sqlite3 import connect, Error as sqlError
from datetime import datetime

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



    def fibo(self, *, n: int) -> int:
        self.__add_to_db('fibo', 1, 'n', str(n))
        return alg.fibo(n = n)
    
    def pow(self, n: int, m: int) -> int:
        self.__add_to_db('pow', 2, 'n,m', f'{n},{m}')
        return alg.pow(n, m)

    def cmmdc(self, *, n: int, m: int) -> int:
        self.__add_to_db('cmmdc', 2, 'n,m', f'{n},{m}')
        return alg.cmmdc(n, m)

    def cmmmc(self, *, n: int, m: int) -> int:
        self.__add_to_db('cmmmc', 2, 'n, m', f'{n},{m}')
        return alg.cmmmc(n, m)

    def fact(self, *, n: int) -> int:
        self.__add_to_db('fact', 1, 'n', str(n))
        return alg.fact(n)
    
    def gama_sum(self, *, n: int) -> int:
        self.__add_to_db('gama_sum', 1, 'n', str(n))
        return alg.gama_sum(n)
