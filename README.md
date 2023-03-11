# EXTRAÇÃO DE DADOS BRUTOS EM ARTIGOS CIENTÍFICOS UTILIZANDO WEB SCRAPING NA BASE DE DADOS DO SCIENCEDIRECT
Feito pelos alunos Mateus e Vanessa do curso de Tecnologia de Sistema da Computação.
## Sistema para Web Scrapping de artigos cientificos da API do ScienceDirect

## :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: Efetua web scrapping na api do ScienceDirect.
- `Funcionalidade 2`: Retorna os dados encontrado em forma bruta para analise futura.
- `Funcionalidade 3`: Salva os dados no banco de dados não relacional(MongoDB).
- `Funcionalidade 4`: Permite que a busca dos dados continua, ou seja, com a mesma palavra-chave o usuário continua a busca de onde parou.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3.8``
- ``MongoDB``
- ``Pycharm Community``
- ``Paradigma de orientação a objetos``

## ✔️ Pré-Requisitos

- Python 3.x instalado (Caso não tenha clique <a href="https://www.python.org/downloads/">aqui</a>.)
- MongoDB instalado (Caso não tenha clique <a href="https://www.mongodb.com/try/download/community">aqui</a>.)
- Pycharm Community (Caso não tenha clique <a href="https://download.jetbrains.com/python/pycharm-community-2022.1.1.exe">aqui</a>.)
- Uma chave de API do http://dev.elsevier.com (Tutorial para gerar chave da API <a href="https://www.youtube.com/watch?v=9IIpYZQvnYw">aqui</a>.)
- Uma conexão de rede em uma instituição que tenha inscrição no ScienceDirect. 

## 📁 Acesso ao projeto

Você pode <a href="https://github.com/altobellibm/-CEDERJ_2022_MATEUS_VANESSA-">acessar o codigo fonte do projeto</a> ou <a href="https://github.com/altobellibm/-CEDERJ_2022_MATEUS_VANESSA-/archive/refs/heads/main.zip">baixa-lo</a>.

## 🛠️ Abrir e rodar o projeto

#### Após baixar o projeto, você pode abrir com o Pycharm. Para isso após executar o Pycharm, clique em:
- File
- Open
- Busque a pasta onde estar o projeto e selecione (Caso o projeto seja baixado via zip, é necessário extrai-lo antes de procura-lo).
- Clica em Ok

#### Instalação das bibliotecas do Python
- Instale a versão estável do pymongo: ``pip install pymongo``
- Instale a versão estável do requests: ``pip install requests``

#### Configuração
- Crie um arquivo config.json, caso exista apenas atualize com as informações que deseja:
  ```json
  { 
    "keyword": "palavra-chave que deseja",
    "scienceDirectApiKey": "ApiKey",
    "quantityArticleDownload": "quantidade de Artigos para busca"
  }
  ```
#### Execução do Projeto
- Para executar o projeto basta abrir o terminal na mesma pasta do projeto e executar o comando:
``python main.py``

