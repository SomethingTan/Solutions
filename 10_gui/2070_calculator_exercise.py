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
        # row 1
        self.button7 = tk.Button(self.input_frame,  text="7", width=2, command=lambda: write_display_entry(self, 7))
        self.button7.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.button8 = tk.Button(self.input_frame, text="8", width=2, command=lambda: write_display_entry(self, 8))
        self.button8.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        self.button9 = tk.Button(self.input_frame, text="9", width=2, command=lambda: write_display_entry(self, 9))
        self.button9.grid(row=0, column=2, padx=self.padx, pady=self.pady)
        # row 2
        self.button4 = tk.Button(self.input_frame, text="4", width=2, command=lambda: write_display_entry(self, 4))
        self.button4.grid(row=1, column=0, padx=self.padx, pady=self.pady)
        self.button5 = tk.Button(self.input_frame, text="5", width=2, command=lambda: write_display_entry(self, 5))
        self.button5.grid(row=1, column=1, padx=self.padx, pady=self.pady)
        self.button6 = tk.Button(self.input_frame, text="6", width=2, command=lambda: write_display_entry(self, 6))
        self.button6.grid(row=1, column=2, padx=self.padx, pady=self.pady)
        # row 3
        self.button1 = tk.Button(self.input_frame, text="1", width=2, command=lambda: write_display_entry(self, 1))
        self.button1.grid(row=2, column=0, padx=self.padx, pady=self.pady)
        self.button2 = tk.Button(self.input_frame, text="2", width=2, command=lambda: write_display_entry(self, 2))
        self.button2.grid(row=2, column=1, padx=self.padx, pady=self.pady)
        self.button3 = tk.Button(self.input_frame, text="3", width=2, command=lambda: write_display_entry(self, 3))
        self.button3.grid(row=2, column=2, padx=self.padx, pady=self.pady)
        # row 4
        self.button_AC = tk.Button(self.input_frame, text="AC", width=2, command=lambda: clear_display_entry(self))
        self.button_AC.grid(row=3, column=0, padx=self.padx, pady=self.pady)
        self.button0 = tk.Button(self.input_frame, text="0", width=2, command=lambda: write_display_entry(self, 0))
        self.button0.grid(row=3, column=1, padx=self.padx, pady=self.pady)
        self.button_equals = tk.Button(self.input_frame, text="=", width=2, command=lambda: evaluate(self))
        self.button_equals.grid(row=3, column=2, padx=self.padx, pady=self.pady)
        # operators
        self.button_plus = tk.Button(self.input_frame, text="+", width=2, command=lambda: write_display_entry(self, "+"))
        self.button_plus.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.button_minus = tk.Button(self.input_frame, text="-", width=2, command=lambda: write_display_entry(self, "-"))
        self.button_minus.grid(row=1, column=3, padx=self.padx, pady=self.pady)
        self.button_divide = tk.Button(self.input_frame, text="/", width=2, command=lambda: write_display_entry(self, "/"))
        self.button_divide.grid(row=2, column=3, padx=self.padx, pady=self.pady)
        self.button_multiply = tk.Button(self.input_frame, text="*", width=2, command=lambda: write_display_entry(self, "*"))
        self.button_multiply.grid(row=3, column=3, padx=self.padx, pady=self.pady)


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