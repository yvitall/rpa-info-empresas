from mapa_situacao import mapa_situacao
import requests



cnpj = "02.636.065/0001-53";
cnpj_limpo = "".join(c for c in cnpj if c.isdigit())
try:
    print(f"Iniciando busca pelo CNPJ: {cnpj}")
    link_api = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    
    r = requests.get(link_api)
    
    if r.status_code == 200:
        dados_empresa = r.json()
        
        print(" ==== DADOS DA EMPRESA ==== ")
        print("Razão Social:", dados_empresa["razao_social"])
        print("Nome fantasia:", dados_empresa["nome_fantasia"])
        print("CNPJ:", dados_empresa["cnpj"])
        
        print(" ==== INFORMAÇÕES LEGAIS ==== ")
        print("Natureza Jurídica:", dados_empresa["natureza_juridica"])
        texto_situacao = mapa_situacao.get(dados_empresa["situacao_cadastral"]) #######     PAREI AQUI
        print("Situação Cadastral:", texto_situacao)
        print("Data de Abertura:", dados_empresa["data_inicio_atividade"])
        
        print(" ==== ENDEREÇO ==== ")
        print("CEP:", dados_empresa["cep"])
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
    else: 
        print(f"Falha ao consultar API, status code: {r.status_code}")
        print(f"Motivo: {r.text}")
        print("Aguarde um momento e tente novamente.")
except Exception as erro_encontrado:
    print("Opa, tivemos um problema na execução:", erro_encontrado)