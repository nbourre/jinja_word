import tkinter as tk

class CustomControlTemplate(tk.Frame):
    def __init__(self, master, label_text, button_text, button_command):
        super().__init__(master)

        self.label = tk.Label(self, text=label_text)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text=button_text, command=button_command)

        self.label.pack(side="left")
        self.entry.pack(side="left")
        self.button.pack(side="left")

# Example usage
def on_button_click(entry_widget):
    text = entry_widget.get()
    print(f"Button clicked! Entered text: {text}")

root = tk.Tk()

template1 = CustomControlTemplate(root, "Label 1:", "Button 1", on_button_click)
template1.pack()

template2 = CustomControlTemplate(root, "Label 2:", "Button 2", on_button_click)
template2.pack()

root.mainloop()
