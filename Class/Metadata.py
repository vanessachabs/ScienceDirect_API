from Class.Database import Database


class Metadata:
    def __init__(self):
        self.database = Database()

    # Metodo onde é gerado o arquivo "metadata.json"
    def generateMetada(self, data):
        self.keyword = data['keyword'].lower()
        self.scienceDirectApiKey = data['scienceDirectApiKey']
        self.qtdArticle = data['quantityArticleDownload']

        # Calculo para saber qual a ultima pagina do arquivo
        last = self.qtdArticle / 25

        # Dicionário para criação do arquivo
        metadata = {
            'keyword': self.keyword,
            'quantityArticleDownload': self.qtdArticle,
            'quantityArticleTotalDownload': self.qtdArticle,
            'start': 0,
            'last': int(last)
        }

        # Salva no Base de dados chamada "Article", coleção metadata
        # Caso a palavra-chave ja foi buscada anteriomente tem um metodo que verifica essa parte no arquivo Database
        return self.database.insertDataMetadata("metadata", metadata)
