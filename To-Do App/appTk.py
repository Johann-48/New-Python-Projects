import tkinter as tk
from tkinter import ttk
import main as code

root = tk.Tk()
root.title("Table with Entry Widgets")
root.geometry("1000x500")

#TABLE
# Create a Treeview widget
columns = ("Title", "Description", "DueDate", "Priority", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)

# Takes the data from main.py

# FUNCTIONS

def packTitle(sampleInput):
    title = sampleInput.get()
    print('GOT', title)
    return title
def packDescription(sampleInput):
    description = sampleInput.get()
    print('GOT', description)
    return description
def packDueDate(sampleInput):
    dueDate = sampleInput.get()
    print('GOT', dueDate)
    return dueDate
def packPriority(sampleInput):
    priority = sampleInput.get()
    print('GOT', priority)
    return priority


def refreshTreeview():
    for item in tree.get_children():
        tree.delete(item)
    for row in code.items:
        tree.insert("", tk.END, values=(row.title, row.description, row.dueDate, row.priority, row.status))

def create():
    # Title
    titleLabel = tk.Label(root, text="Title")
    titleLabel.pack()
    sampleTitle = tk.Entry(root, width=30)
    sampleTitle.pack(pady=(0, 10))

    # Description
    descriptionLabel = tk.Label(root, text="Description")
    descriptionLabel.pack()
    sampleDescription = tk.Entry(root, width=30)
    sampleDescription.pack(pady=(0, 10))

    # Due Date
    dueDateLabel = tk.Label(root, text="Due Date (DD/MM/YYYY)")
    dueDateLabel.pack()
    sampleDueDate = tk.Entry(root, width=30)
    sampleDueDate.pack(pady=(0, 10))

    # Priority
    priorityLabel = tk.Label(root, text="Priority (1-5)")
    priorityLabel.pack()
    samplePriority = tk.Entry(root, width=30)
    samplePriority.pack(pady=(0, 10))

    def onClick():
        outTitle = packTitle(sampleTitle)
        sampleTitle.destroy()
        titleLabel.destroy()

        outDescription = packDescription(sampleDescription)
        sampleDescription.destroy()
        descriptionLabel.destroy()

        outDueDate = packDueDate(sampleDueDate)
        sampleDueDate.destroy()
        dueDateLabel.destroy()

        outPriority = packPriority(samplePriority)
        samplePriority.destroy()
        priorityLabel.destroy()

        okButton.destroy()

        code.addItem(outTitle, outDescription, outDueDate, outPriority)  

        refreshTreeview()
  

    okButton = tk.Button(root, text='Confirm', command=onClick)
    okButton.pack()

def status():
    sampleTitle = tk.Entry(root, width=30)
    sampleTitle.insert(0, "Title")
    sampleTitle.pack(pady=10)

    def onClick():
        search = packTitle(sampleTitle)
        sampleTitle.destroy()
        okButton.destroy()

        code.changeStatus(search)

        refreshTreeview()

    okButton = tk.Button(root, text='Confirm', command=onClick)
    okButton.pack()


# BUTTONS

createButton = tk.Button(root, text = 'Create', command = create)
statusButton = tk.Button(root, text = 'Change Status', command = status)


createButton.pack()
statusButton.pack()
# Pack the Treeview
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()