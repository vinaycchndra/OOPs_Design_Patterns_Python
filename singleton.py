# Singleton class can have only one instance
# We do not use a constructor instead we use getInstance method to 

class Singleton:
    __instance = None

    def __init__(self):
        self.isLoggedIn = False
        if Singleton.__instance != None:
            raise Exception('This can have only one instance')
        Singleton.__instance = self


    @staticmethod
    def getApp():
        if Singleton.__instance is None:
            Singleton()    
        return Singleton.__instance
        

app = Singleton.getApp()
print(app.isLoggedIn)

app.isLoggedIn = True

app2 = Singleton.getApp()

print(app2.isLoggedIn)


