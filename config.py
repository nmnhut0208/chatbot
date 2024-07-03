import os
from dotenv import load_dotenv

load_dotenv()
SERVICE_NAME = os.getenv('SERVICE_NAME', '/chat')
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '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')
LANGUAGE = os.getenv('LANGUAGE', 'English')
MODEL_NAME = os.getenv('MODEL_NAME', 'llama3-70b-8192')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_MAX_SIZE_BYTES = int(os.getenv('LOG_MAX_SIZE_BYTES', 20*1024*1024))
LOG_MAX_LENGTH_FIELD = int(os.getenv('LOG_MAX_LENGTH_FIELD', 256))
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'logs/access.log')