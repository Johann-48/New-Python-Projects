
# List of Items
List = []

# Model of data Creation
class Item:
    def __init__(self, title):
        self.title = title
        self.finished = False

# Creates and inserts samples
n1 = Item('English Homework')
n2 = Item('Tidy the Room')
n3 = Item('Learn Pyhton')
List.extend([n1, n2, n3])

# Add Item Function
def addItem(title):
    new_item = Item(str(title))
    List.append(new_item)

while True:
    title = input('Insert an item: ')
    addItem(title)

    while True:
        # Asks the user if it wants to stop
        continue_input = input('Do you want to add another item? (y/n): ').strip().lower()
        if continue_input == 'n':
            break
        elif continue_input == 'y':
            break
        else:
            print('Awnser Unknown')
        
    if continue_input == 'n':
        break

# Prints the To-Do List
for item in List:
    print(f'- {item.title}')