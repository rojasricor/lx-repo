import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Hola mundo!", font=("Helvetica", 32))
        self.label.pack(padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()

