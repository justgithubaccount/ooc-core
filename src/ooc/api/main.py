from fastapi import FastAPI
from ooc.api.routes import ooc_routes
from ooc.config.settings import settings
from ooc.config.logging_config import setup_logging

setup_logging()

app = FastAPI(title=settings.app_name)

app.include_router(ooc_routes.router)
