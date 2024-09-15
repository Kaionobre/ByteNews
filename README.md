# Projeto de Web Scraping e API - Notícias Adrenaline

Este projeto realiza web scraping no site de tecnologia **Adrenaline** para obter as principais notícias e depois expõe essas informações em uma **API** utilizando **FastAPI**. O servidor retorna os dados em formato **JSON** para que possam ser consumidos por outras aplicações.

## Funcionalidades

- Coleta as principais notícias do site **Adrenaline** utilizando web scraping.
- Retorna uma lista das notícias contendo o **título** e **link**.
- Exposição dos dados por meio de uma API REST, com resposta em formato **JSON**.

## Tecnologias Utilizadas

- **Python** (linguagem principal)
- **BeautifulSoup** (para o web scraping)
- **FastAPI** (para a criação da API)
- **Requests** (para fazer requisições HTTP)
- **Uvicorn** (para servir a API)
- **JSON** (formato de resposta da API)

