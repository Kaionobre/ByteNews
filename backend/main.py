from fastapi import FastAPI
from scrapy import pegar_noticias_e_links
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/noticias")
async def mostrar_noticias():
    noticias = pegar_noticias_e_links()
    return {"dados": noticias}


