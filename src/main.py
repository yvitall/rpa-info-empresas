import html
from requests import status_codes
import requests
from bs4 import BeautifulSoup

MAPA_SITUACAO = {
    1: "NULA",
    2: "ATIVA",
    3: "SUSPENSA",
    4: "INAPTA",
    8: "BAIXADA"
}

def mapear_situacao_cadastral(situacao_cadastral):
    return MAPA_SITUACAO.get(situacao_cadastral, "Código Inválido")

print("Digite um cnpj para realizar consulta:")
cnpj = input("CNPJ: ")
cnpj_limpo = "".join(c for c in cnpj if c.isdigit())
try:
    print(f"Iniciando busca pelo CNPJ: {cnpj}")
    link_api = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    
    r = requests.get(link_api)
    
    if r.status_code == 200:
        dados_empresa = r.json()
        
        print(" ==== DADOS DA EMPRESA ==== ")
        print("Razão Social: ", dados_empresa["razao_social"])
        print("Nome fantasia:", dados_empresa["nome_fantasia"])
        print("CNPJ:", dados_empresa["cnpj"])
        
        print(" ==== INFORMAÇÕES LEGAIS ==== ")
        print("Natureza Jurídica: ", dados_empresa["natureza_juridica"])
        print("Situação Cadastral: ", mapear_situacao_cadastral(dados_empresa["situacao_cadastral"]))
        print("Data de Abertura: ", dados_empresa["data_inicio_atividade"])
        
        print(" ==== ENDEREÇO ==== ")
        print("CEP: ", dados_empresa["cep"])
        print("Cidade:", dados_empresa["municipio"])
        print("Estado:", dados_empresa["uf"])
        print("Endereço:", dados_empresa["logradouro"])
        print("Bairro:", dados_empresa["bairro"])
        print("Número:", dados_empresa["numero"])
        print("Complemento:", dados_empresa["complemento"])
        print(" ==== CONTATOS ==== ")
        print("E-mail:", dados_empresa["email"])
        print("Telefone 01:", dados_empresa["ddd_telefone_1"])
        print("Telefone 02:", dados_empresa["ddd_telefone_2"])
        
        print("==== O QUE DIZ O GOOGLE? ====")
        link_google = f"https://www.google.com.br/search?q={dados_empresa["razao_social" or "cnpj"]}"
        resposta = requests.get(link_google)
        if resposta.status_code == 200:
            html_puro = resposta.text()
            
            soup = BeautifulSoup(html_puro, "html.parser")

            titulo_pagina = soup.find("a").text
            print(titulo_pagina)
    else: 
        print(f"\nFalha ao consultar API, status code: {r.status_code}")
        print(f"Motivo: {r.text}")
        print("Aguarde um momento e tente novamente.")
except Exception as erro_encontrado:
    print("Opa, tivemos um problema na execução:", erro_encontrado)