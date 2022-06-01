import pymongo

class Database:
    def __init__(self):
        self.URI = 'mongodb://localhost:27017/'
        self.client = None

    # Efetua a conexão com o banco de dados
    def connectionDatabase(self):
        return pymongo.MongoClient(self.URI)

    # Inseri no banco de dados os metadatas da palavra-chave
    # Por que salvar os metadatas no banco? Caso queira buscar mais artigos(com a mesma palavra chave) continuar de onde parou
    # Query para verificação se a palavra-chave em questão ja encontra-se na base de dados
    # E atualizar os metadata
    def insertDataMetadata(self, nameColumn, data):
        self.client = self.connectionDatabase()
        database = self.client["Articles"]
        collection = database[nameColumn]
        query = {"keyword": data["keyword"]}
        resultQuery = collection.find(query)

        for x in resultQuery:
            data["quantityArticleTotalDownload"] = x["quantityArticleTotalDownload"] + data["quantityArticleDownload"]
            data["start"] = x["last"]
            data["last"] = data["last"] + x["last"]
            collection.update_one({"keyword": data["keyword"]}, {'$set': data})
            return data

        collection.insert_one(data)
        return data

    # Importa o arquivo JSON com uma coleção na base chamada Articles
    def insertDataSearch(self, nameColumn, data):
        self.client = self.connectionDatabase()
        database = self.client["Articles"]
        collection = database[nameColumn]
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)