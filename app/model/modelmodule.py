from app.extensions import mongo

class Model():
    def __init__(self):
        self.collection = mongo

    def Add(self, username, password):
        self.collection.db.insert({'username': username, 'password': password})

    def GetPass(self, username):
        rec = self.collection.db.find({"username": username})
        if rec.count() > 0:
            return rec["password"]
        return ""

    def IsExist(self, username):
        rec = self.collection.db.find({"username": username})
        if rec.count() > 0:
            return True
        return False

