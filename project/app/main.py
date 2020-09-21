from fastapi import FastAPI, Depends
import os
from tortoise.contrib.fastapi import register_tortoise


from app.config import get_settings, Settings

app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return dict(
        ping="pong!",
        environment=settings.environment,
        testing=settings.testing
    )
