from fastapi import APIRouter, HTTPException, status, Request
from utils.logging import Logger
import config
import os
from core.model import Chatbot
from schemas.schemas import ChatRequest

class ChatbotEndpoints():
    def __init__(self, logger: Logger) -> None:
        self.router = APIRouter()
        self.logger = logger
        self.chatbot = Chatbot()
        self.model_name = config.MODEL_NAME
        self.language = config.LANGUAGE

        @self.router.post("/generate")
        async def generate(request: ChatRequest):
            """
            Generate a response from the AI model.
            args:
                request (Request): The request object.
            return:
                dict: The response of the AI model.
            """
            try:
                content = request.content
                language = self.language if request.language is None else request.language
                chat_completion = self.chatbot.chat(content, model=self.model_name, language=language)

                return {"response": chat_completion}
            except Exception as e:
                self.logger.error({"error": str(e)})
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_router(self):
        return self.router