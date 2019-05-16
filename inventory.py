user1 = {'banaandrink': 1, 'kyouko': 3, 'madoka': 7, 'sayaka': 8, 'homura': 11}
dragonLoot = ['banaandrink', 'banaandrink', 'madoka', 'kyouko', 'banaandrink', 'homer']

def displayInventory(inv):
  print("Inventory:")
  itemTotal = 0
  for key, value in inv.items():
    print(value, key)
    itemTotal = itemTotal + value
  print("\nTotal number of items: " + str(itemTotal))

def addToInventory(inv, loot):
  for item in loot:
    if item in inv:
      inv[item] += 1
    else:
      inv[item] = 1

addToInventory(user1, dragonLoot)
displayInventory(user1)
