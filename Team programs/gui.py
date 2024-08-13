# W06 Team Activity

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area")
    frm_main.pack(padx=10, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    
def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_height = Label(frm_main, text="Height:")

    # Create an integer entry box where the user will enter her age.
    ent_height = IntEntry(frm_main, width=4)

    # Create a label that displays "years"
    lbl_width = Label(frm_main, text="Width:")
    
    # Create an integer entry box where the user will enter her age.
    ent_width = IntEntry(frm_main, width=4)

    # Create a label that displays "Rates:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    area = Label(frm_main, width=3)
    
    # Create label to display error
    lbl_status = Label(frm_main, width=10)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_height.grid(      row=0, column=0, padx=3, pady=3)
    ent_height.grid(      row=0, column=1, padx=3, pady=3)
    lbl_width.grid(row=1, column=0, padx=3, pady=3)
    ent_width.grid(row=1, column=1, padx=3, pady=3)

    lbl_area.grid(      row=2, column=1, padx=3, pady=3)
    lbl_status.grid(row=3, column=0, padx=3, pady=3)
    btn_clear.grid(row=4, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            height = ent_height.get()
            width = ent_width.get()
            if height <= 0 or width <= 0:
                lbl_status.config(text="Invalid Input.")
            # Compute the user's maximum heart rate.
            area = height * width

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_area.config(text=f"Area: {area:.0f}")
            
        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_area.config(text="")
            lbl_status.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_height.clear()
        lbl_area.config(text="")
        ent_height.focus()
        ent_width.clear()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_height.bind("<KeyRelease>", calculate)
    ent_width.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_height.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()