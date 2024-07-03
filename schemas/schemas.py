from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    content: str
    # language: str Optional
    language: Optional[str] = None
