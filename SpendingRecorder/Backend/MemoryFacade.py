from Backend.Types.Pay import Pay

class MemoryFacade:
    def __init__(self):
        self.income = list()
        self.spending = list()

    def GetIncome(self, page, page_size):
        self._sortIncomeByDate()
        start_index = int(page) * int(page_size)
        end_index = start_index + int(page_size)
        if start_index > len(self.income) - 1 or int(page) < 0:
            raise IndexError("Invalid page number")
        sorted_list = self.income.copy()
        results = list()
        for i, pay in enumerate(sorted_list):
            if(i < start_index):
                continue
            if i >= end_index:
                break
            results.append(pay)
        return results

    def GetIncomeInRange(self, start, end):
        result = list()
        for pay in self.income:
            if pay.date >= start and pay.date <= end:
                result.append(pay)
        return result

    def AddIncome(self, date, amount):
        self.income.append(Pay(date, amount))

    def _sortIncomeByDate(self):
        self.income.sort(key=lambda pay: pay.date)