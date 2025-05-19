
# List of Items
items = []

# Model of item creation
class Item:
    def __init__(self, title, description, dueDate, priority):
        self.title = title.strip().lower()
        self.description = description
        self.dueDate = dueDate
        self.priority = priority
        self.status = False

# FUNCTIONS
# Add Item Function
def addItem(title, description, dueDate, priority):
    new_item = Item(str(title), str(description), str(dueDate), int(priority))
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

        match i.priority:
            case 1:
                priorityStr = 'Not Important'
            case 2:
                priorityStr = 'Keep In Mind'
            case 3:
                priorityStr = 'Better Do'
            case 4:
                priorityStr = 'Important'
            case 5:
                priorityStr = 'Urgent'

        print(f'- {i.title} // Status: {statusStr} // Due Date: {i.dueDate} // Priority: {priorityStr}')

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
            sampleTitle = str(input('Insert a item: '))
            sampleDescription = str(input('Insert item description (If it doesnt have one, type NO): '))
            sampleDueDate = str(input('Insert a Due Date (Format: DD/MM/YYYY)(If no Due Date, type NO): '))
            samplePriority = int(input('Insertr the item priority (Type from 1 to 5, 1 being not important, and 5 being urgent): '))


            if sampleDescription == 'NO':
                sampleDescription = 'Description wasnt created'
            if sampleDueDate == 'NO':
                sampleDueDate = 'Due Date wasnt created'

            addItem(sampleTitle, sampleDescription, sampleDueDate, samplePriority)
                

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