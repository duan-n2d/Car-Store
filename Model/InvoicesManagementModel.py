import pymongo

class InvoicesManagementModel():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.myclient["project"]
        self.mycollection = self.mydb["Invoice"]