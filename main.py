import json
from Class.Metadata import Metadata
from Class.RequestSeachArticle import RequestSeachArticle

if __name__ == '__main__':
    metadata = Metadata()
    requestArticle = RequestSeachArticle()
    data = dict()

    with open("config.json", 'r') as file:
        data = json.load(file)

    findDataBase = metadata.generateMetada(data)
    requestArticle.requestSeachArticle(findDataBase, data["scienceDirectApiKey"])
