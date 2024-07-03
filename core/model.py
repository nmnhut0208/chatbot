import os
from groq import Groq
import config

class Chatbot:
    def __init__(self):
        self.client = Groq(
            # This is the default and can be omitted
            api_key=config.GROQ_API_KEY,
        )

    def chat(self, content, model="llama3-70b-8192", language="English"):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant. Your response must be in {language}."
                },
                {
                    "role": "user",
                    "content": f"{content}",
                }
            ],
            model=model,
        )

        return chat_completion.choices[0].message.content