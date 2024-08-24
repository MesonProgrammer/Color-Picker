import pyautogui
from pynput.mouse import Listener, Button
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Color Picker')
        self.geometry('400x300')
        self.configure(borderwidth=5)

        self.rgb = None
        self.hex = None

        self.pick_color_button = tk.Button(self, text="Pick Color", command=self.pick_color)
        self.pick_color_button.grid(row=0, column=0, sticky='w', pady=2)

        self.rgb_frame = tk.Frame(self)
        self.rgb_frame.grid(row=1, column=0, sticky='w')

        self.rgb_label = tk.Label(self.rgb_frame, text="RGB: ")
        self.rgb_label.grid(row=0, column=0, sticky='w', pady=2)

        self.rgb_entry = tk.Entry(self.rgb_frame, width=13, state='readonly', font=('Courier New', 11))
        self.rgb_entry.grid(row=0, column=1, sticky='w', pady=2)

        self.hex_frame = tk.Frame(self)
        self.hex_frame.grid(row=2, column=0, sticky='w')

        self.hex_label = tk.Label(self.hex_frame, text="HEX: ")
        self.hex_label.grid(row=0, column=0, sticky='w', pady=2)

        self.hex_entry = tk.Entry(self.hex_frame, width=6, state='readonly', font=('Courier New', 11))
        self.hex_entry.grid(row=0, column=1, sticky='w', pady=2)

        self.color_display = tk.Label(self, text='\t\t\n\n\n\n\n\n', fg='white')
        self.color_display.grid(row=3, column=0, sticky='w', pady=12)

    def pick_color(self):
        def on_click(x, y, button, pressed):
            if button == Button.left and pressed:
                r, g, b = pyautogui.pixel(x, y)
                self.rgb = f'{r}, {g}, {b}'
                self.hex = f'{r:02x}{g:02x}{b:02x}'

                self.rgb_entry.configure(state='normal')
                self.rgb_entry.delete('1', tk.END)
                self.rgb_entry.insert('1', self.rgb)
                self.rgb_entry.configure(state='readonly')

                self.hex_entry.configure(state='normal')
                self.hex_entry.delete('1', tk.END)
                self.hex_entry.insert('1', self.hex)
                self.hex_entry.configure(state='readonly')

                self.color_display.configure(bg=f'#{self.hex}')

                l.stop()
                self.pick_color_button.configure(state='normal', relief='raised')

        self.pick_color_button.configure(state='disabled', relief='sunken')
        l = Listener(on_click=on_click)
        l.run()

if __name__ == '__main__':
    app = App()
    app.mainloop()
