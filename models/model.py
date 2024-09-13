from pydantic import BaseModel


class Postragem(BaseModel):
    nome: str
    