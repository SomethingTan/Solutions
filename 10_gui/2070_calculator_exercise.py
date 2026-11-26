"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""


import tkinter as tk


class GUIElements:

    def __init__(self):
        self.padx = 8  # Horizontal distance to neighboring objects
        self.pady = 4  # Vertical distance to neighboring objects
        self.rowheight = 24  # rowheight in treeview


        self.main_window = tk.Tk()
        self.main_window.title("GUI Calculator")
        self.main_window.geometry("500x700")


        self.output_frame = tk.Frame(self.main_window)
        self.output_frame.grid(row=0, column=0, padx=self.padx, pady=self.pady)

        self.display_entry = tk.Entry(self.output_frame, justify="right", state="readonly")
        self.display_entry.grid(row=0, column=0, padx=self.padx, pady=self.pady)


        self.input_frame = tk.Frame(self.main_window)
        self.input_frame.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("*", 2, 3),
                         ("0", 3, 1),              ("/", 3, 3),
        ]
        for text, row, column in buttons:
            tk.Button(self.input_frame,  text=text, width=2, command=lambda t=text: write_display_entry(self, t)).grid(row=row, column=column, padx=self.padx, pady=self.pady)

        self.button_AC = tk.Button(self.input_frame, text="AC", width=2, command=lambda: clear_display_entry(self))
        self.button_AC.grid(row=3, column=0, padx=self.padx, pady=self.pady)
        self.button_equals = tk.Button(self.input_frame, text="=", width=2, command=lambda: evaluate(self))
        self.button_equals.grid(row=3, column=2, padx=self.padx, pady=self.pady)


def clear_display_entry(gui):
    gui.display_entry.config(state=tk.NORMAL)
    gui.display_entry.delete(0, tk.END)
    gui.display_entry.config(state="readonly")


def write_display_entry(gui, text):
    gui.display_entry.config(state=tk.NORMAL)
    gui.display_entry.insert(tk.END, f"{text}")
    gui.display_entry.config(state="readonly")

def evaluate(gui):
    solution = str(eval(gui.display_entry.get()))
    clear_display_entry(gui)
    write_display_entry(gui, solution)

def main():
    gui = GUIElements()
    gui.main_window.mainloop()

   
main()