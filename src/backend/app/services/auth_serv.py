from sqlite3 import connect, Error as sqlError
from datetime import datetime, timedelta, timezone 
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt 
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from fastapi import Depends, HTTPException, status

from models import models as  mod



class Service:

    # OAuth2 schema for token authentication
    # tokenUrl: str - the URL to get the token
    __outh2_schema = OAuth2PasswordBearer(tokenUrl='token')

    # constructor gets the database path
    # stores it for the future connections
    # to the database
    # db_url: str - the path to the database
    # initializes the hashing context for passwords
    # initializes the JWT key and algorithm
    # initializes the expiration time for the token
    # initializes the password context for hashing
    # initializes the OAuth2 schema for token authentication
    # __KEY: str - the key used for encoding the JWT token
    # __ALGO: str - the algorithm used for encoding the JWT token
    # __expiring_time_minutes: int - the expiration time for the token in minutes
    # __pwd_context: CryptContext - the context for hashing passwords
    # __outh2_schema: OAuth2PasswordBearer - the schema for token authentication
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__KEY = 'f8574f697280a5dfdf80a84da8d2e7744c9b88a83c8fbdd3127c169acd898029'
        self.__pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        self.__ALGO =  'HS256'
        self.__expiring_time_minutes = 200


    # private method to hash a password
    # password: str - the password to be hashed
    # returns: str - the hashed password
    # raises: Exception - if the hashing fails
    def __hash_password(self, password: str) -> str:
        return self.__pwd_context.hash(password)
    
    # private method to verify a password against a hashed password
    # password: str - the password to be verified
    # hash_password: str - the hashed password to verify against
    # returns: bool - True if the password matches the hashed password, False otherwise
    # raises: Exception - if the verification fails
    def __verif_password(self, password: str, hash_password: str) -> bool:
        return self.__pwd_context.verify(password, hash_password)
    
    # private method to create a JWT token
    # _data: dict[str, str] - the data to be encoded in the token
    # returns: str - the encoded JWT token
    # raises: Exception - if the token creation fails
    def __create_token(self, _data: dict[str, str]) -> str:
        expiring_time = datetime.now(timezone.utc) + timedelta(minutes=self.__expiring_time_minutes)
        for_encoding = _data.copy()
        for_encoding.update({'exp': expiring_time})
        print(f"the dict for the encoding --------------- {for_encoding}")
        encoded_jwt = jwt.encode(for_encoding, self.__KEY, algorithm=self.__ALGO)
        return encoded_jwt
        
    # method to get the user through the token
    # token: str - the JWT token to be decoded
    # returns: mod.User - the user object if the token is valid
    # raises: HTTPException - if the token is invalid or the user is not found
    # uses: Depends - to inject the OAuth2 schema for token authentication
    def get_user_through_token(self, token: Annotated[str, Depends(__outh2_schema)]) -> mod.User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The token was either not found or is wrong",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, self.__KEY, algorithms=[self.__ALGO])
            email = payload.get('sub')
            if email is None:
                raise credentials_exception
            user = self.get_user(email=email)
            if user is None:
                raise credentials_exception
            return user
        except InvalidTokenError:
            raise credentials_exception
        
        
    # method to login a user
    # credentials: mod.Credentials - the credentials of the user to be logged in
    # returns: mod.AuthToken - the JWT token if the login is successful
    # raises: HTTPException - if the login fails
    def login(self, credentials: mod.Credentials) -> mod.AuthToken:
        email, password = credentials.values()
        user = self.__auth_user(email, password)
        print("Final Auth done ###########")
        if len(user) == 0:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # sub = subject stands for the subject of the token 
        access_token = self.__create_token({'sub': user[0][1]})
        print("Token created ############### ", access_token)
        return mod.AuthToken(token=access_token, token_type='bearer')

    # private method to authenticate a user
    # email: str - the email of the user to be authenticated
    # password: str - the password of the user to be authenticated
    # returns: bool | list - True if the user is authenticated, False if the user is not found or the password is incorrect, or a list of user data if the user is found
    # raises: Exception - if the authentication fails
    def __auth_user(self, email: str, password: str) ->  list:
        found_user = self.get_user(email=email)
        if len(found_user) == 0:
            return []
        elif not self.__verif_password(password, found_user[0][2]):
            return []
        return found_user


    # method to add a user to the database
    # user: mod.User - the user to be added
    # returns: None
    # raises: Exception - if the connection to the database fails
    def add_user(self, user: mod.User):
        try:
            connection = connect(self.db_url, check_same_thread=False)
            print('Connection established...')
            cursor = connection.cursor()
            query = 'insert into User(name, email, password, date) values (?, ?, ?, ?)'
            cursor.execute(query, (user.name, user.email, self.__hash_password(user.password), str(datetime.now())))
            connection.commit()
            print('User added into the database...')
        except sqlError as err:
            print('Connection failed, error occured...', err)
        finally:
            if connection:
                connection.close()
                print('Connection closed...')
            

    # method to get a user from the database
    # args: str - the arguments to filter the user by (e.g. name, email)
    # returns: list - the list of users that match the arguments
    # raises: Exception - if the connection to the database fails
    def get_user(self, **args: str) -> list:
        try:
            
            connection = connect(self.db_url, check_same_thread=False)
            print('Connection established...')
            cursor = connection.cursor()
            query = f'select * from user '
            if len(args) != 0:
                query += ' where '
                for k, v in args.items():
                    query += f'{k} = \'{v}\','
                # delete the last comma
                query = query[:-1]
            print(query)
            cursor.execute(query) 
            return cursor.fetchall()  
        except sqlError as err:
            print('Connection failed, error occured...', err)
        finally:
            if connection:
                connection.close()
                print('Connection closed...')

