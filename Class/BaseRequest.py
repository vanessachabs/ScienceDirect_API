import requests


class BaseRequest:
    # Metodo que de fato faz a requisição dos artigos na API do ScienceDirect
    def baseRequest(self, keyword, scienceDirectApiKey, page):
        self.keyword = keyword
        self.scienceDirectApiKey = scienceDirectApiKey
        self.page = page

        API_ENDPOINT = 'https://api.elsevier.com/content/search/sciencedirect?'

        # Query da requisição
        queryScienceDirect = {
            'query': self.keyword,
            'count': 25,
            'start': self.page
        }

        # Header da requisição
        headerScienceDirect = {
            'Accept': 'application/json',
            'X-ELS-APIKey': self.scienceDirectApiKey
        }

        # Retorno dos dados extraidos
        return requests.get(API_ENDPOINT, params=queryScienceDirect, headers=headerScienceDirect)
