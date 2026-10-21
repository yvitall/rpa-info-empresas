# 🏢 Consulta CNPJ via BrasilAPI (RPA-info-empresas)

Aprendizado prático de Python desenvolvendo uma RPA para automação de coleta de dados com Web Scraping para consulta de informações detalhadas de empresas utilizando o CNPJ através da **BrasilAPI**. 

Este projeto foi desenvolvido como prática de automação, consumo de APIs RESTful e manipulação de dados JSON utilizando a biblioteca `requests`, com implementação de ``BeautifulSoup`` & ``Playwright`` em breve.

## 🚀 Atual Funcionalidades

- **Busca Automatizada:** Coleta de dados atualizados de empresas usando apenas o CNPJ.
- **Tratamento de Dados:** Limpeza automática de caracteres especiais (pontos, barras, traços) antes de realizar a requisição HTTP.
- **Exibição Estruturada:** Retorno formatado no terminal categorizado em:
  - Dados da Empresa (Razão Social, Nome Fantasia, CNPJ).
  - Informações Legais (Natureza Jurídica, Situação Cadastral, Data de Abertura).
  - Endereço Completo.
  - Contatos (E-mail, Telefones).
- **Tratamento de Erros:** Estrutura `try/except` para lidar com falhas de conexão ou problemas no retorno da API (Status Codes diferentes de 200).

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca **Requests** 

## ⚙️ Como executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/yvitall/rpa-info-empresas.git](https://github.com/yvitall/rpa-info-empresas.git)
   cd rpa-info-empresas