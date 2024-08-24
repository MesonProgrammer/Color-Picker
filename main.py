import pyautogui
from pynput.mouse import Listener, Button
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Sets the title and dimensions of the window.
        self.title('Color Picker')
        self.geometry('400x300')

        # Sets the border of the window to 5.
        self.configure(borderwidth=5)

        # Defines the `rgb` and `hex` variables.
        self.rgb = None
        self.hex = None

        # Creates a button with the text of "Pick Color". When this button is pressed, it runs the command `self.pick_color`.
        self.pick_color_button = tk.Button(self, text="Pick Color", command=self.pick_color)
        self.pick_color_button.grid(row=0, column=0, sticky='w', pady=2)

        # Creates a frame to store the RGB value.
        self.rgb_frame = tk.Frame(self)
        self.rgb_frame.grid(row=1, column=0, sticky='w')

        # Creates a label to show that the entry is of an RGB value.
        self.rgb_label = tk.Label(self.rgb_frame, text="RGB: ")
        self.rgb_label.grid(row=0, column=0, sticky='w', pady=2)

        # Creates a readonly entry to display the RGB value.
        self.rgb_entry = tk.Entry(self.rgb_frame, width=13, state='readonly', font=('Courier New', 11))
        self.rgb_entry.grid(row=0, column=1, sticky='w', pady=2)

        # Creates a frame to store the HEX value.
        self.hex_frame = tk.Frame(self)
        self.hex_frame.grid(row=2, column=0, sticky='w')

        # Creates a label to show that the entry is of a HEX value.
        self.hex_label = tk.Label(self.hex_frame, text="HEX: ")
        self.hex_label.grid(row=0, column=0, sticky='w', pady=2)

        # Creates a readonly entry to display the HEX value.
        self.hex_entry = tk.Entry(self.hex_frame, width=6, state='readonly', font=('Courier New', 11))
        self.hex_entry.grid(row=0, column=1, sticky='w', pady=2)

        # Creates a "box" to display the chosen color. (I have no idea why I set the foreground to white.)
        self.color_display = tk.Label(self, text='\t\t\n\n\n\n\n\n', fg='white')
        self.color_display.grid(row=3, column=0, sticky='w', pady=12)

    # Defines the pick_color function that is referred to as `self.pick_color` in code.
    def pick_color(self):

        # A function that fires when the mouse clicks.
        def on_click(x, y, button, pressed):

            # Checks if the button that was clicked was the left mouse button and the button was pressed down and not up.
            if button == Button.left and pressed:

                # Stores the r, g, and b values of the pixel at where the mouse cursor is at.
                r, g, b = pyautogui.pixel(x, y)

                # Formats the RGB values into a string with commas seperating them.
                self.rgb = f'{r}, {g}, {b}'

                # Formats the RGB values into a 6-digit hexadecimal value.
                self.hex = f'{r:02x}{g:02x}{b:02x}'

                # Inserts the RGB value into the RGB entry.
                self.rgb_entry.configure(state='normal')
                self.rgb_entry.delete('1', tk.END)
                self.rgb_entry.insert('1', self.rgb)
                self.rgb_entry.configure(state='readonly')

                # Inserts the HEX value into the HEX entry.
                self.hex_entry.configure(state='normal')
                self.hex_entry.delete('1', tk.END)
                self.hex_entry.insert('1', self.hex)
                self.hex_entry.configure(state='readonly')

                # Sets the background of the "box" to the color that was selected.
                self.color_display.configure(bg=f'#{self.hex}')

                # Stops the mouse listener once the button is pressed.
                l.stop()

                # Enables the pick color button to be pressed again and raises the button's relief.
                self.pick_color_button.configure(state='normal', relief='raised')

        # Disables the pick color button so it cannot be pressed and sinks the button's relief.
        self.pick_color_button.configure(state='disabled', relief='sunken')

        # Defines and runs a mouse listener to listen for mouse clicks.
        l = Listener(on_click=on_click)
        l.run()

# If the program is being run directly and not as an imported module, it runs the following code.
if __name__ == '__main__':

    # Defines and runs the app.
    app = App()
    app.mainloop()
