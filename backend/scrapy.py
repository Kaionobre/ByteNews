from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def pegar_noticias_e_links():
    url = 'https://www.adrenaline.com.br/noticias/'                    

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Roda sem abrir o navegador
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(10)  # Dá tempo para as imagens carregarem

    raw_html = driver.page_source
    driver.quit()  # Fecha o navegador depois de carregar a página

    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    artigo = parsed_html.find('div', class_='archive-list-posts')
    artigos = artigo.find_all('article', class_='feed feed-4-list')

    lista_noticias = []

    for artigo in artigos:
        titulo_elemento = artigo.find('h2')
        imagem_noticia = artigo.find('a').find('figure').find('img')
        data_hora = artigo.find('span')
        link_elemento = artigo.find('a')
        
        if titulo_elemento and link_elemento and imagem_noticia:
            imagem_url = imagem_noticia.get("src")
            
            # Se ainda for um placeholder, tenta pegar do srcset
            if "data:image" in imagem_url:  
                srcset = imagem_noticia.get("srcset")
                if srcset:
                    imagem_url = srcset.split(",")[-1].strip().split(" ")[0]
            
            lista_noticias.append({
                "titulo": titulo_elemento.text.strip(),
                "data_e_hora": data_hora.text.strip(),
                "link": link_elemento['href'],
                "imagem": imagem_url
            })

    return lista_noticias

# Testando a função
noticias = pegar_noticias_e_links()
for noticia in noticias:
    print(noticia)
