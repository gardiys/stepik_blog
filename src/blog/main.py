from fastapi import FastAPI
from blog.resources import router


def get_app():
    app = FastAPI()

    app.include_router(router)

    return app


app = get_app()
