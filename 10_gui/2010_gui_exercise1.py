"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

padx = 15
pady = 5

labelFrame = tk.LabelFrame(main_window, text="Container")
labelFrame.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

label1 = tk.Label(labelFrame, text="Id")
label1.grid(row=0, column=0, padx=padx, pady=pady)
entry1 = tk.Entry(labelFrame, width=2)
entry1.grid(row=1, column=0, padx=padx, pady=pady)
button1 = tk.Button(labelFrame, text="Create")
button1.grid(row=2, column=0, padx=padx, pady=pady)
if __name__ == "__main__":
    main_window.mainloop()