from DataStore.UsageTracking.Facades.MemoryFacade import MemoryFacade

class UsageFacadeFactory:
    def __init__(self, facadeType):
        self.facadeType = facadeType

    def Create(self):
        if self.facadeType == "Memory":
            return MemoryFacade()
        return None