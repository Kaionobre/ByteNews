import requests
from bs4 import BeautifulSoup

def pegar_noticias():
    url = 'https://www.adrenaline.com.br/noticias/'                    
    response = requests.get(url)
    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    article = parsed_html.find('div', class_='archive-list-posts')
    noticias = article.find_all('h2')

    lista_noticias = []

    for noticia in noticias:

        lista_noticias.append({"titulo": noticia.text})
    
    return lista_noticias
