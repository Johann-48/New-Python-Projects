
# List of Items
items = []

# Model of data Creation
class Item:
    def __init__(self, title):
        self.title = title
        self.finished = False

# Creates and inserts samples

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
            break

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
                while True:
                    itemTitle = str(input('Insert the Item you want to delete: '))
                    for i in items:
                        if i.title == itemTitle:
                            items.remove(i)
                            print('Item Deleted')
                            break
                    else:
                            print('Item was not found, sure you wrote that right?')

        else:
            print('Awnser Unknown')
        
    if continue_input == 'n':
        break

# Prints the To-Do List
for i in items:
    print(f'- {i.title}')