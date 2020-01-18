import datetime
from Backend_old.ItemEntry import ItemEntry
from Backend_old.Item import Item
from DataStore.ItemStorage.DataStoreFacadeFactory import DataStoreFacadeFactory
from DataStore.UsageTracking.UsageFacadeFactory import UsageFacadeFactory

if __name__ == "__main__":
    entry = ItemEntry(DataStoreFacadeFactory("Memory"), UsageFacadeFactory("Memory"))
    entry.EnterItem(Item(datetime.datetime(2019,11,3), "Bread", 2.59), "Food", True)
    entry.EnterItem(Item(datetime.datetime(2019,11,3), "Frosted Mini Wheats", 7.99), "Food", True)
    entry.EnterItem(Item(datetime.datetime(2019, 11,17), "Rent", 645), "Rent")
    entry.UseItem(1, "Breakfast")
    entry.UseItem(0, "Lunch")
    itemUsage = entry.GetItemUsages()
    for id in itemUsage:
        print(str(id) + ":" + str(itemUsage[id].usesBreakfast) + ":" + str(itemUsage[id].usesLunch) + ":" + str(itemUsage[id].usesDinner) + ":" + str(itemUsage[id].usesOther) + ":" + str(itemUsage[id]))