def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        item_total += v
        print(v, end = ' ')
        print(k)

    print("\nTotal number of items: " + str(item_total))

'''
Write a function named addToInventory(inventory, addedItems), where the inventory
parameter is a dictionary representing the player’s inventory (like in the previous
project) and the addedItems parameter is a list like dragonLoot. The addToInventory()
function should return a dictionary that represents the updated inventory. Note that
the addedItems list can contain multiples of the same item. Your code could look something
like this:
'''

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    # your code goes here
    for prop in dragonLoot:    
        if prop in inventory:
            inventory[prop] += 1
        else:
            inventory.update({prop:1})
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
