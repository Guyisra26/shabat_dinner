from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import dinner

app = FastAPI()

app.include_router(dinner.router)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
