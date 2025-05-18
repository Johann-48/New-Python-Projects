from datetime import datetime

# List of Items
items = []

# Model of item creation
class Item:
    def __init__(self, title, description):
        self.title = title.strip().lower()
        self.description = description
        self.status = False

# FUNCTIONS
# Add Item Function
def addItem(title, description, dueDate, priority):
    new_item = Item(str(title), str(description))
    items.append(new_item)

# Add Delete Item Function
def deleteItem(title):
    for i in items:
        if i.title == title:
            items.remove(i)
            return True
    return False

# Add cahnge Status Function
def changeStatus(title):
    for i in items:
        if i.title == title:
            if i.status == False:
                i.status = True
            else:
                i.status = False
            return True
    return False

# Add Show List Function
def showList():
    for i in items:
        if i.status == True:
            statusStr = 'Done'
        elif i.status == False:
            statusStr = 'Not done'
        print(f'- {i.title} // Status: {statusStr}')

# Add Show Description Function
def showDescription(title):
    for i in items:
        if i.title == title:
            print(f'{i.description}')
            return True
    return False


# RUNNING PROGRAM

while True:
    # Asks what the user wants to do
    default = input('What do you want to do? (Create/End/Show List/Delete/Change Status/Show Description): ').strip().lower()

    # Filter of the Selected Option
    match default:

        case 'create':
            sample = str(input('Insert a item: '))
            sampleDescription = str(input('Insert item description(If it doesnt have one, type NO): '))
            if sampleDescription != 'NO':
                addItem(sample, sampleDescription)
            else:
                addItem(sample, 'Description wasnt created')

        case 'end':
            break

        case 'show list':
            showList()

        case 'delete':
            itemTitle = str(input('Insert the item you want to delete: ')).strip().lower()
            if deleteItem(itemTitle):
                print('Item deleted successfully')
            else:
                print("Item not found")
        
        case 'change status':
            itemTitle = str(input('Insert the item you want to change the status: ')).strip().lower()
            if changeStatus(itemTitle):
                print('Item changed its status')
            else:
                print("Item not found")
        
        case 'show description':
            itemTitle = str(input('Insert the item you want to view description: ')).strip().lower()
            if showDescription(itemTitle):
                print('DESCRIPTION SHOWED')
            else:
                print("Item not found")
            
            
        case _:
            print('Non-existent option')





# Prints the To-Do List
showList()