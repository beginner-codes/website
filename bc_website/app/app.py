from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import pathlib

PATH = pathlib.Path(__file__).parent.parent

app = FastAPI()
templates = Jinja2Templates(directory=str(PATH / "templates"))
