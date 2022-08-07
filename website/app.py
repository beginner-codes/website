from starlette.applications import Starlette
from starlette.responses import RedirectResponse, HTMLResponse
from starlette.routing import Route
import pathlib


async def discord_redirect(request):
    return RedirectResponse("https://discord.gg/F56Gg9w")


async def index(request):
    return HTMLResponse(pathlib.Path("templates/index.html").read_text())


app = Starlette(
    routes=[
        Route("/", index, name="index"),
        Route('/discord', discord_redirect, name="discord-invite"),
    ]
)
