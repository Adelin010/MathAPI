from sqlite3 import connect, Error as sqlError
import jwt
from typing import Union
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status

from ..models import models as mod


class Service:
    __outh2_schema = OAuth2PasswordBearer(tokenUrl="token")

    def __init__(self):
        self.db_url = "./app.db"
        self.__KEY = "f8574f697280a5dfdf80a84da8d2e7744c9b88a83c8fbdd3127c169acd898029"
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.__ALGO = "HS256"
        self.__expiring_time_minutes = 200

    def __hash_password(self, password: str) -> str:
        return self.__pwd_context.hash(password)

    def __verif_password(self, password: str, hash_password: str) -> bool:
        return self.__pwd_context.verify(password, hash_password)

    def __create_token(self, _data: dict[str, str]) -> str:
        expiring_time = datetime.now(timezone.utc) + timedelta(
            minutes=self.__expiring_time_minutes
        )
        for_encoding = _data.copy()
        for_encoding.update({"exp": expiring_time})
        print(f"the dict for the encoding --------------- {for_encoding}")
        encoded_jwt = jwt.encode(for_encoding, self.__KEY, algorithm=self.__ALGO)
        return encoded_jwt

    def get_user_through_token(
        self, token: Annotated[str, Depends(__outh2_schema)]
    ) -> mod.User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, self.__KEY, algorithms=[self.__ALGO])
            email = payload.get("sub")
            if email is None:
                raise credentials_exception
            user = self.get_user(email=email)
            if user is None:
                raise credentials_exception
            return user
        except jwt.PyJWTError:
            raise credentials_exception

    def login(self, credentials: mod.Credentials) -> mod.AuthToken:
        email, password = credentials.values()
        user = self.__auth_user(email, password)
        print("Final Auth done ###########")
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # sub = subject stands for the subject of the token
        access_token = self.__create_token({"sub": user[0][1]})
        print("Token created ############### ", access_token)
        return mod.AuthToken(token=access_token, token_type="bearer")

    def __auth_user(
        self, email: str, password: str
    ) -> Union[bool, list]:  # wtf bool | list =))))
        found_user = self.get_user(email=email)
        if len(found_user) == 0:
            return False
        elif not self.__verif_password(password, found_user[0][2]):
            return False
        return found_user

    def add_user(self, user: mod.User):
        connection = None  # paote ajunge in finally unbound
        try:
            connection = connect(self.db_url, check_same_thread=False)
            print("Connection established...")
            cursor = connection.cursor()
            query = "insert into User(name, email, password, date) values (?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    user.name,
                    user.email,
                    self.__hash_password(user.password),
                    str(datetime.now()),
                ),
            )
            connection.commit()
            print("User added into the database...")
        except sqlError as err:
            print("Connection failed, error occured...", err)
        finally:
            if connection:
                connection.close()
                print("Connection closed...")

    def get_user(self, **args: str) -> list:
        connection = None  # paote ajunge in finally unbound
        try:
            connection = connect(self.db_url, check_same_thread=False)
            print("Connection established...")
            cursor = connection.cursor()
            query = f"select * from user "
            if len(args) != 0:
                query += " where "
                for k, v in args.items():
                    query += f"{k} = '{v}',"
                # delete the last comma
                query = query[:-1]
            print(query)
            cursor.execute(query)
            return cursor.fetchall()
        except sqlError as err:
            print("Connection failed, error occured...", err)
        finally:
            if connection:
                connection.close()
                print("Connection closed...")
            return []
