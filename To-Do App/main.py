
# List of Items
items = []

# Model of data Creation
class Item:
    def __init__(self, title):
        self.title = title.strip().lower(   )
        self.finished = False

# Creates and inserts samples
n1 = Item('tidy')
items.append(n1)

# FUNCTIONS
# Add Item Function
def addItem(title):
    new_item = Item(str(title))
    items.append(new_item)

#Add Delete Item Function
def deleteItem(title):
    for i in items:
        if i.title == title:
            items.remove(i)
            return True
        else:
            return False
        

while True:
    title = input('Insert an item: ')
    addItem(title)

    while True:
        # Asks the user if it wants to stop
        continue_input = input('Do you want to add another item? (y/n/Show List/Delete): ').strip().lower()
        if continue_input == 'n':
            break
        elif continue_input == 'y':
            break
        elif continue_input == 'show list':
            for i in items:
                print(f'- {i.title}')
        elif continue_input == 'delete':
                
            itemTitle = str(input('Insert the item you want to delete: '))
            if deleteItem(itemTitle):
                print('Item deleted successfully')
            else:
                print("Item not found")
        else:
            print('Non-existent option')
        
    if continue_input == 'n':
        break

# Prints the To-Do List
for i in items:
    print(f'- {i.title}')


print(items)