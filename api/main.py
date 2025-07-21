from fastapi import FastAPI

from .routes.routes import router

from .db import Base, engine  # for sqlite orm

Base.metadata.create_all(
    bind=engine
)  # this way when you just run the app you automatically have the db

app = FastAPI()
app.include_router(router=router)
