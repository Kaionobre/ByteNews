# ByteNews

ByteNews é uma aplicação que realiza web scraping no site de tecnologia **Adrenaline** para capturar as principais notícias, expondo-as através de uma API desenvolvida com **FastAPI**. O servidor retorna as informações em formato JSON, permitindo que outras aplicações as consumam facilmente.

## Funcionalidades
- Coleta automática das principais notícias do site **Adrenaline**.
- Retorna uma lista contendo **título**, **data** e **link** das notícias.
- Exposição das informações através de uma API REST em formato JSON.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para desenvolvimento da API.
- **BeautifulSoup**: Ferramenta para web scraping.
- **Requests**: Biblioteca para requisições HTTP.
- **Uvicorn**: Servidor para executar a aplicação.
- **JSON**: Formato de resposta da API.
