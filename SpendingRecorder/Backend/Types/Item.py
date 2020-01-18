class Item:
    def __init__(self, date, name, cost):
        self.date = date
        self.name = name
        self.cost = cost

    def __str__(self):
        return str(self.date.date()) + ":" + str(self.name) + ":" + str(self.cost)