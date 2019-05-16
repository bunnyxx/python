user1 = {'banaandrink': 1, 'kyouko': 3, 'madoka': 7, 'sayaka': 8, 'homura': 11}

def displayInventory(inv):
  print("Inventory:")
  itemTotal = 0
  for key, value in inv.items():
    print(value, key)
    itemTotal = itemTotal + value
  print("\nTotal number of items: " + str(itemTotal))

displayInventory(user1)
