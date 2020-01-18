class Pay:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def to_json(self):
        return '{"date":"' + str(self.date.date()) + '","amount":'+ str(self.amount) + '}'