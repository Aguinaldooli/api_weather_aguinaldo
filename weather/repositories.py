from django.conf import settings
import pymongo

class WeatherRepository:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        documents = list(self.getCollection().find({}))
        return documents
    
    def insert(self, document):
        self.getCollection().insert_one(document)

    def delete(self, document) -> None:
        self.getCollection().delete_one({"_id": document["_id"]})
        
    def deleteAll(self) -> None:
        self.getCollection().delete_many({})