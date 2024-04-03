from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    content: str
    is_published: Optional[bool]
