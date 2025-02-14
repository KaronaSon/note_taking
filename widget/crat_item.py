from tkinter import Tk, Frame, Label, Button
import tkinter.messagebox as messagebox

class CartItem:
    def __init__(self, model):
        self.model = model
        self.root = Tk()
        self.root.title("Cart Item")
        self.setup_ui()

    def setup_ui(self):
        frame = Frame(self.root)
        frame.pack(padx=10, pady=10)

        Label(frame, text=self.model.title, font=("Arial", 18, "bold")).pack()
        Label(frame, text=self.model.description).pack()
        Label(frame, text=self.model.time).pack()

        edit_button = Button(frame, text="Edit", command=self.edit_action, bg="green", fg="white")
        edit_button.pack(side="left", padx=5)

        delete_button = Button(frame, text="Delete", command=self.delete_action, bg="red", fg="white")
        delete_button.pack(side="right", padx=5)

    def edit_action(self):
        messagebox.showinfo("Edit", "Edit action triggered for: " + self.model.title)

    def delete_action(self):
        messagebox.showinfo("Delete", "Delete action triggered for: " + self.model.title)
        self.root.destroy()


