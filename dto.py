from typing import List, Dict, Any
from pydantic import BaseModel, Field, HttpUrl, ValidationError

class LinkDTO(BaseModel):
    link: HttpUrl
    text: str = None
    alttext: str = None

class ScrapDTO(BaseModel):
    AboutUs: List[HttpUrl]
    sampleBlogPost: List[HttpUrl]

class IncludeDTO(BaseModel):
    redirectLink: List[LinkDTO] = []
    internalLink: List[LinkDTO] = []
    imageLink: List[LinkDTO] = []
    blogTitle: str = ''
    metaDescription: str = ''
    keywords: List[str] = []

class BlogAiDTO(BaseModel):
    scrap: ScrapDTO
    include: IncludeDTO

class RequestDTO(BaseModel):
    blogAi: BlogAiDTO
    version: int



def validate_blogai_dto(data: Dict[str, Any]) -> List[str]:
    try:
        RequestDTO(**data)
        return []
    except ValidationError as e:
        return e.errors()
