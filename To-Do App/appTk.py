import tkinter as tk

root = tk.Tk()
root.title("Table with Entry Widgets")

rows = 2
columns = 4
entries = []

for i in range(rows):
    row_entries = []
    for j in range(columns):
        e = tk.Entry(root)
        e.grid(row=i, column=j, padx=5, pady=5)
        e.insert(0, f"Row {i+1}, Col {j+1}")
        row_entries.append(e)
    entries.append(row_entries)


root.mainloop()