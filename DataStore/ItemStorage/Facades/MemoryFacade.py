class MemoryFacade:
    def __init__(self):
        self.items = dict()
        self.newItemKey = 0

    def Insert(self, item, category):
        table = None
        try:
            table = self.items[category]
        except KeyError:
            self.items[category] = dict()
            table = self.items[category]
        table[self.newItemKey] = item
        self.newItemKey += 1
        

    def GetAll(self):
        return self.items

    def GetTable(self, category):
        return self.items[category]