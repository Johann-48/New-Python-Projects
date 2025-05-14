
# List of Items
items = []

# Model of data Creation
class Item:
    def __init__(self, title):
        self.title = title.strip().lower()
        self.status = False

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
            return True
    return False

def changeStatus(title):
    for i in items:
        if i.title == title:
            if i.status == False:
                i.status = True
            else:
                i.status = False
            return True
    return False

def showList():
    for i in items:
        if i.status == True:
            statusStr = 'Done'
        elif i.status == False:
            statusStr = 'Not done'
        print(f'- {i.title} // Status: {statusStr}')


while True:
    title = input('Insert an item: ')
    addItem(title)

    while True:
        # Asks the user if it wants to stop
        continue_input = input('What do you want to do? (Create/End/Show List/Delete/Change Status): ').strip().lower()

        if continue_input == 'create':
            break

        elif continue_input == 'e':
            break

        elif continue_input == 'show list':
            showList()

        elif continue_input == 'delete':
            itemTitle = str(input('Insert the item you want to delete: ')).strip().lower()
            if deleteItem(itemTitle):
                print('Item deleted successfully')
            else:
                print("Item not found")
        
        elif continue_input == 'change status':
            itemTitle = str(input('Insert the item you want to change the status: ')).strip().lower()
            if changeStatus(itemTitle):
                print('Item changed its status')
            else:
                print("Item not found")
            
        else:
            print('Non-existent option')
        
    if continue_input == 'n':
        break




# Prints the To-Do List
showList()