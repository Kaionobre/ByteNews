from fastapi import FastAPI
from scrapy import pegar_noticias
import json

app = FastAPI()

@app.get("/noticias")
async def mostrar_noticias():
    noticias = pegar_noticias()
    print(noticias)
    return {"dados": noticias}