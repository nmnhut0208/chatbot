from fastapi import APIRouter
from utils.logging import Logger
from api.endpoints.health import HealthEndpoints
from api.endpoints.chatbot import ChatbotEndpoints
import config

class Endpoints:
    def __init__(self, logger: Logger) -> None:
        self.health_routers = HealthEndpoints().get_router()
        self.chatbot_routers = ChatbotEndpoints(logger).get_router()
        self.routers = APIRouter(prefix=config.SERVICE_NAME)
        self.routers.include_router(self.health_routers, tags=["health"])
        self.routers.include_router(self.chatbot_routers, tags=["chatbot"])

    def get_routers(self):
        return self.routers