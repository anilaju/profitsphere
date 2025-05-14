import tkinter as tk
from tkinter import messagebox

class ProfitsphereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profitsphere Trading Bot")
        self.root.geometry("600x400")
        
        # Add your GUI components here
        self.label = tk.Label(root, text="Welcome to Profitsphere!", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Check Signals", command=self.show_signals)
        self.button.pack()

    def show_signals(self):
        messagebox.showinfo("Signals", "Buy NIFTY 50 CE @ 22,800")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfitsphereApp(root)
    root.mainloop()