import requests
from bs4 import BeautifulSoup

def pegar_noticias_e_links():
    url = 'https://www.adrenaline.com.br/noticias/'                    
    response = requests.get(url)
    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    artigo = parsed_html.find('div', class_='archive-list-posts')
    artigos = artigo.find_all('article', class_='feed feed-4-list')

    lista_noticias = []

    for artigo in artigos:
        titulo_elemento = artigo.find('h2')
        link_elemento = artigo.find('a')
        
        if titulo_elemento and link_elemento:
            lista_noticias.append({
                "titulo": titulo_elemento.text.strip(),
                "link": link_elemento['href']
            })

    return lista_noticias


