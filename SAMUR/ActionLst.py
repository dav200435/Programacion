class ActionsLst:
    def __init__(self) -> None:
        self.list = []
        
    def addAction(self,action):
        self.list.append(action)
        
    def getList(self):
        return self.list