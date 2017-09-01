from app.model.modelmodule import Model

class Control():
    def __init__(self):
        self.model = Model()

    def LogInAction(self, username, password):
        if self.model.IsExist(username) == False:
            return False

        if self.model.GetPass(username) == password:
            return True

        return False

    def RegisterAction(self, username, password):
        if self.model.IsExist(username) == True:
            return False

        if len(password) < 6 or len(password) > 8:
            return False

        self.model.Add(username, password)

        return True
