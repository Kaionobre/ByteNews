from fastapi import FastAPI
from scrapy import pegar_noticias_e_links
import json

app = FastAPI()

@app.get("/noticias")
async def mostrar_noticias():
    noticias = pegar_noticias_e_links()
    return {"dados": noticias}
