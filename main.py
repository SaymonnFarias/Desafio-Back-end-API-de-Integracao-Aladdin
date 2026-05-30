
"""
PASSO A PASSO PARA RODAR A API:

1o passo - No cmd digite: uvicorn main:app --reload
2o passo - clique no link http://127.0.0.1:8000 para abrir a pagina da API 
3o passo - Para acessar o Swagger UI, insira a palavra docs ao final do URL  (desssa forma) -- >(http://127.0.0.1:8000/docs) e pressione Enter. 
4o passo - Na interface do Swagger clique na rota GET /preco-tapetes para expandir os detalhes dela. 
5o passo - Clique no botão "Try it out" para habilitar a edição dos parâmetros da rota.
6o passo - No campo "data" insira a data desejada no formato DD/MM/AAAA e clique no botão "Execute"
7o passo - Com isso você verá os dados dos tapetes, retirados da outra API, para a data especificada.
"""

from fastapi import FastAPI
from API_tapetes import buscar_dados

app = FastAPI()

@app.get("/")
def home():
    return {"API funcionando!"}

@app.get("/preco-tapetes")
def listar_preco_tapetes(data: str):
    resultado = buscar_dados(data)
    return resultado
