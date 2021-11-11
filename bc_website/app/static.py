from bc_website.app import app, PATH
from fastapi.staticfiles import StaticFiles


app.mount("/static", StaticFiles(directory=str(PATH / "static")), name="static")
