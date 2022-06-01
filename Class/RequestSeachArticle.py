import json
from time import sleep
from Class.BaseRequest import BaseRequest
from Class.Database import Database
from Class.ProgressBar import ProgressBar


class RequestSeachArticle:
    def __init__(self):
        self.request = BaseRequest()
        self.progress = ProgressBar()
        self.database = Database()

    # Metodo que busca os artigos na API do ScienceDirect
    def requestSeachArticle(self, data, scienceDirectApiKey):
        self.keyword = data["keyword"]
        self.scienceDirectApiKey = scienceDirectApiKey
        self.start = data["start"]
        self.last = data["last"]

        # Lista para armazenar os artigos que foram buscados
        articleList = []

        # Barra de prograsso para representa o andamento das buscas
        for i in self.progress.progressbar(range(self.start, int(self.last)), "Downloading: "):
            # Requisição na API
            resp = self.request.baseRequest(self.keyword, self.scienceDirectApiKey, i)

            # Verifica a resposta da requisição
            # Caso não seja Ok retorna a resposta falsa
            if not resp.ok:
                return resp.ok

            # Carrega na variavel data o json
            data = json.loads(resp.content)

            # Adiciona na lista o resultado da resposta
            articleList.append(data)
            sleep(0.30)

        # Escreve no arquivo 'search.json' a lista com todos os artigos extraidos
        self.database.insertDataSearch(self.keyword, articleList)