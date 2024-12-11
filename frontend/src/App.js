import React, { useState, useEffect } from 'react';
import api from './services/api';

function App() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    api.get('/noticias')
      .then((response) => {
        console.log(response.data); // Verificar a resposta da API no console
        setNews(response.data.dados); // Acesse o array dentro da chave 'dados'
      })
      .catch((error) => {
        console.error('Erro ao buscar notícias:', error);
      });
  }, []);

  return (
    <div>
      <h1>Notícias</h1>
      <ul>
        {news.map((item, index) => (
          <li key={index}>
            <h2>{item.titulo}</h2>
            <p>{item.data_e_hora}</p>
            <a href={item.link}>Ler mais</a>
            <img src={item.imagem} alt={item.titulo} style={{ width: '300px' }} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
