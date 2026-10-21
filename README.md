# 🏢 Consulta CNPJ via BrasilAPI (RPA-info-empresas)

Aprendizado prático de Python desenvolvendo uma RPA para automação de coleta de dados com Web Scraping para consulta de informações detalhadas de empresas utilizando o CNPJ através da **BrasilAPI**. 

Este projeto foi desenvolvido como prática de automação, consumo de APIs RESTful e manipulação de dados JSON utilizando a biblioteca `requests`, com implementação de ``BeautifulSoup`` & ``Playwright`` em breve.

## Atual Funcionalidades

- **Busca Automatizada:** Coleta de dados atualizados de empresas usando apenas o CNPJ.
- **Tratamento de Dados:** Limpeza automática de caracteres especiais (pontos, barras, traços) antes de realizar a requisição HTTP.
- **Exibição Estruturada:** Retorno formatado no terminal categorizado em:
  - Dados da Empresa (Razão Social, Nome Fantasia, CNPJ).
  - Informações Legais (Natureza Jurídica, Situação Cadastral, Data de Abertura).
  - Endereço Completo.
  - Contatos (E-mail, Telefones).
- **Tratamento de Erros:** Estrutura `try/except` para lidar com falhas de conexão ou problemas no retorno da API (Status Codes diferentes de 200).

Futura Implementação: 

- Implementação de Loop para leitura de dados em Lote de processamento
- Entrada dinâmica para consulta de qualquer CNPJ pelo terminal.
- Implementar Beautiful Soup para Web Scraping
- Implementar Playwright para automação de tarefas
- Saída Estruturada em PDF/Excel/Json
- Tratamento de Exceções e Vazios e nulos

## Tecnologias Utilizadas

- **Python 3**
- Biblioteca **Requests** 

## Como executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/yvitall/rpa-info-empresas.git](https://github.com/yvitall/rpa-info-empresas.git)
   cd rpa-info-empresas
   
2. Instale a dependência necessária:
 ```bash
    pip install requests
```
3. Execute o script via CLI: 
```bash
    python dossie.py
```

## Exemplo de saída:
    ```bash
    Iniciando busca pelo CNPJ: 02.636.065/0001-53
    ==== DADOS DA EMPRESA ==== 
    Razão Social: QUEIROZ CAVALCANTI - ADVOCACIA
    Nome fantasia:
    CNPJ: 02636065000153
    ==== INFORMAÇÕES LEGAIS ==== 
    Natureza Jurídica: Sociedade Simples Pura
    Situação Cadastral: ATIVA
    Data de Abertura: 1998-02-06
    ==== ENDEREÇO ==== 
    CEP: 51020015
    Cidade: RECIFE
    Estado: PE
    Endereço: DA HORA
    Bairro: ESPINHEIRO
    Número: 670
    Complemento: E 692
    ==== CONTATOS ==== 
    E-mail: None
    Telefone 01: 8121015757
    Telefone 02: 8121015344
    ```