import requests

link_api = "https://testedefensoriapr.pythonanywhere.com/precos"


def buscar_dados(data: str):

    resposta = requests.get(link_api, params={"data": data}) #requisitando a API e adicionando a data como parâmetro
    dados = resposta.json() #convertendo a resposta para formato JSON
    
    if resposta.status_code == 200: #verificando se a resposta foi bem-sucedida 

        resultado = [] #criando uma lista para armazenar os dados retirados da API

        for item in dados: #iterando sobre os dados e imprimindo cada item
            resultado.append({
                "data atual": data,
                "estilo do tapete": item["nome"],
                "preco por metro quadrado": item["valor_m2"]
            })
        return resultado
    else: 
        print("Erro ao acessar a API:", resposta.status_code)
        return None

  