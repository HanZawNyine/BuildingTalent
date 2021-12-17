import pymongo

class mongoDB:
    def __init__(self,client,databaseName,collection):
        self.client = pymongo.MongoClient(client)
        self.databaseName = self.client[databaseName]
        self.collection = self.databaseName[collection]

    def insert(self,*args):
        self.myInsertData =dict(args[0])
        #print(self.myInsertData)
        # print(type(self.myInsertData))
        # mydict = {"name": "aa", "address": "Highway 37"}
        self.collection.insert_one(self.myInsertData)
        #print("Data inserted")
        #except:
        #    print("OOPs...Inserting Error !")

    def search(self,*args):
        toserach = dict(args[0])
        #print(self.toserach)
        mydoc = self.collection.find(toserach)
        for data in mydoc:
            print(data)
            # print(data["name"])
            # print(data["address"])
            # print(data["_id"])
            # print(type(data["address"]))

    def searchingAnyColumn(self,searchString:str):
        name = {'name': searchString}
        name = self.collection.find(name)
        for data in name:
            print(data)

        address = {'address': searchString}
        address = self.collection.find(address)
        for data in address:
            print(data)
        #print(filteringResult)

if __name__ == "__main__":
    mongoDB = mongoDB(client="mongodb://localhost:27017/",databaseName="bank",collection="bank")
    # mongoDB.insert({"name": "a", "address": "dfg"})
    # mongoDB.insert({"name": "s", "address": "fdfdf"})
    # mongoDB.insert({"name": "b", "address": "10dfsdfd"})
    # mongoDB.insert({"name": "dd", "address": "fdf"})
    # mongoDB.insert({"name": "ii", "address": "fdfg"})
    # mongoDB.insert({"name": "fdsafsd", "address": "hh"})
    #mongoDB.insert({"name": "aaaaaaaa", "address": "han"})
    #mongoDB.search({"name": "jj"})
    mongoDB.searchingAnyColumn("han")