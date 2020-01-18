class MemoryFacade:
    def __init__(self):
        self.items = dict()
        self.newItemKey = 0

    def Insert(self, item):
        item.usesBreakfast = 0
        item.usesLunch = 0
        item.usesDinner = 0
        item.usesOther = 0
        self.items[self.newItemKey] = item
        self.newItemKey += 1


    def GetAll(self):
        return self.items

    def UseItem(self, id, usedFor):
        if usedFor == "Breakfast":
            self.items[id].usesBreakfast += 1
        elif usedFor == "Lunch":
            self.items[id].usesLunch += 1
        elif usedFor == "Dinner":
            self.items[id].usesDinner += 1
        elif usedFor == "Other":
            self.items[id].usesOther += 1