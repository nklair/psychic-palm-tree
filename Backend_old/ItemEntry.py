class ItemEntry:
    def __init__(self, dataStoreFacadeFactory, usageFacadeFactory):
        self.dataStoreFacade = dataStoreFacadeFactory.Create()
        self.usageFacade = usageFacadeFactory.Create()

    def EnterItem(self, item, category, trackUsage=False):
        self.dataStoreFacade.Insert(item, category)
        if trackUsage:
            self.usageFacade.Insert(item)

    def GetItems(self):
        return self.dataStoreFacade.GetAll()

    def GetItemsByCategory(self, category):
        return self.dataStoreFacade.GetTable(category)

    def GetItemUsages(self):
        return self.usageFacade.GetAll()

    def UseItem(self, id, usedFor):
        self.usageFacade.UseItem(id, usedFor)