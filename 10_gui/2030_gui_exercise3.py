"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk



def clearEntryBoxes():
    entryId.delete(0,tk.END)
    entryWeight.delete(0, tk.END)
    entryDestination.delete(0, tk.END)
    entryWeather.delete(0, tk.END)


padx = 5
pady = 5
rowheight = 20

treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#773333"

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

style1 = ttk.Style()
style1.theme_use('default')
style1.configure("tree1", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style1.map('tree1', background=[('selected', treeview_selected)])

labelFrame1 = tk.LabelFrame(main_window, text="Container")
labelFrame1.grid(row="0", column="0", padx=padx, pady=pady)

treeFrame1 = tk.Frame(labelFrame1)
treeFrame1.grid(row="0", column="0", padx=padx, pady=pady)

labels = tk.Frame(labelFrame1)
labels.grid(row=1, column=0, padx=padx, pady=pady, sticky=tk.N)
buttons = tk.Frame(labelFrame1)
buttons.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)


treeSB1 = tk.Scrollbar(treeFrame1)
treeSB1.grid(row="0", column="0", padx=padx, pady=pady)
tree1 = ttk.Treeview(treeFrame1, yscrollcommand="treeSB1", selectmode="browse")
tree1.grid(row="0", column="0", padx=padx, pady=pady)

tree1['columns'] = ["col1", "col2", "col3"]
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("col1", anchor=tk.W, width="40")
tree1.column("col2", anchor=tk.W, width="100")
tree1.column("col3", anchor=tk.W, width="200")

tree1.heading("#0", text="", anchor=tk.CENTER)
tree1.heading("col1", text="Id", anchor=tk.CENTER)
tree1.heading("col2", text="Weight", anchor=tk.CENTER)
tree1.heading("col3", text="Destination", anchor=tk.CENTER)


labelId = tk.Label(labels, text="Id")
labelId.grid(row=0, column=0, padx=padx, pady=pady)
entryId = tk.Entry(labels, width=4)
entryId.grid(row=1, column=0, padx=padx, pady=pady)

labelWeight = tk.Label(labels, text="Weight")
labelWeight.grid(row=0, column=1, padx=padx, pady=pady)
entryWeight = tk.Entry(labels, width=8)
entryWeight.grid(row=1, column=1, padx=padx, pady=pady)

labelDestination = tk.Label(labels, text="Destination")
labelDestination.grid(row=0, column=2, padx=padx, pady=pady)
entryDestination = tk.Entry(labels, width=15)
entryDestination.grid(row=1, column=2, padx=padx, pady=pady)

labelWeather = tk.Label(labels, text="Weather")
labelWeather.grid(row=0, column=3, padx=padx, pady=pady)
entryWeather = tk.Entry(labels, width=12)
entryWeather.grid(row=1, column=3, padx=padx, pady=pady)

buttonCreate = tk.Button(buttons, text="Create")
buttonCreate.grid(row=0, column=0, padx=padx, pady=pady)

buttonUpdate = tk.Button(buttons, text="Update")
buttonUpdate.grid(row=0, column=1, padx=padx, pady=pady)

buttonDelete = tk.Button(buttons, text="Delete")
buttonDelete.grid(row=0, column=2, padx=padx, pady=pady)

buttonClear = tk.Button(buttons, text="Clear Entry Boxes", command=clearEntryBoxes)
buttonClear.grid(row=0, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()