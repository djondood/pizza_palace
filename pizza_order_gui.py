import tkinter as tk
from tkinter import messagebox

# Main App Class
class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Palace")
        self.root.geometry("400x400")
        self.create_main_window()

    # Window 1: Welcome Screen
    def create_main_window(self):
        self.clear_window()

        tk.Label(self.root, text="Welcome to Pizza Palace!", font=("Arial", 16)).pack(pady=10)

        # Image 1 # Only works for .png or .gif
        try:
            img = tk.PhotoImage(file="pizza_logo.png")
            label = tk.Label(root, image=img)
            label.pack()
            tk.Label(self.root, image=self.logo, text="Pizza Logo", compound="top").pack(pady=5)
        except:
            tk.Label(self.root, text="[Image: Pizza Logo]").pack()

        tk.Button(self.root, text="Start Order", command=self.create_order_window).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    # Window 2: Order Screen
    def create_order_window(self):
        self.clear_window()

        tk.Label(self.root, text="Choose your Crust:", font=("Arial", 12)).pack()
        self.crust_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.crust_var).pack()

        tk.Label(self.root, text="Choose your Topping:", font=("Arial", 12)).pack()
        self.topping_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.topping_var).pack()

        # Image 2
        try:
            img2 = Image.open("pizza_order.png")
            img2 = img2.resize((100, 100))
            self.pizza_img = ImageTk.PhotoImage(img2)
            tk.Label(self.root, image=self.pizza_img, text="Pizza Image", compound="top").pack(pady=5)
        except:
            tk.Label(self.root, text="[Image: Pizza Slice]").pack()

        tk.Button(self.root, text="Place Order", command=self.place_order).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_main_window).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    # Callback Function
    def place_order(self):
        crust = self.crust_var.get()
        topping = self.topping_var.get()

        # Secure Input Validation
        if not crust.strip() or not topping.strip():
            messagebox.showerror("Input Error", "Please enter both crust and topping.")
            return

        if crust.lower() not in ["thin", "thick", "cheese-stuffed"]:
            messagebox.showwarning("Invalid Crust", "Please choose: Thin, Thick, or Cheese-Stuffed.")
            return

        if topping.lower() not in ["pepperoni", "mushrooms", "onions"]:
            messagebox.showwarning("Invalid Topping", "Please choose: Pepperoni, Mushrooms, or Onions.")
            return

        # Display Order Summary
        messagebox.showinfo("Order Placed", f"Crust: {crust}\nTopping: {topping}\nThank you for your order!")

    # Clear Window Content
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()