from pydantic import BaseModel
from datetime import date

class Postagem(BaseModel):
    nome: str
    link: str
    data: date
    
