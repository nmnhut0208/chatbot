from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from api.routers import Endpoints
from utils.logging import Logger

logger = Logger(config.LOG_FILE_PATH, max_length=config.LOG_MAX_LENGTH_FIELD)
endpoints = Endpoints(logger)
# init app
app = FastAPI()
app.include_router(endpoints.get_routers())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


