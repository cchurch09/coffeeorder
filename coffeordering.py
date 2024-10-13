#Cailli Church
#Date: 10/6/2024
#This programs allows the user to enter their coffee order of choice and/or food and the program calculates how much the user would need to pay


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


#main title of the screeen
class MainWindow:   #determing the main window with the two buttons of going the coffee screen or to exit
    def __init__(self, master):
        self.master = master
        master.title("Main Window")

        welcome_label = tk.Label(master, text="Welcome to the Coffee Shop!", font=("Arial", 18))
        welcome_label.pack(pady=20)

        proceed_button = tk.Button(master, text="Proceed to Coffee Shop", command = self.open_coffee_shop)
        proceed_button.pack(pady=10)

        exit_button = tk.Button(root, text= "Exit", command=root.destroy)
        exit_button.pack(pady=10)

    def open_coffee_shop(self):
        # Destroy the main window and open the Coffee Shop window
        self.master.destroy()
        root = tk.Tk()  # Create a new root window
        CoffeeShop(root)

       #creating the main window of the coffee shop window
class CoffeeShop:
    def __init__(self,master):
        self.master = master
        master.title("Coffee Shop")

        self.create_menu()
        self.create_order_summary()

        #defining of the menus 
    def create_menu(self):
        menu_frame = tk.Frame(self.master)
        menu_frame.pack(side="left", fill="both", expand=True)

        # Example coffee items
        coffee_items = [
            ("Cappuccino", 10, "cappuccino.jpg"),   #name,price, the file
            ("Latte", 12, "latte.jpg"),
            ("Espresso", 8, "espresso.jpg"),
            ("Croissant", 5, "croissant.jpg")
            ]
        for name, price, image_file in coffee_items:
            self.create_coffee_item(menu_frame, name, price, image_file)

    def create_coffee_item(self, frame, name, price, image_file):
        item_frame = tk.Frame(frame)
        item_frame.pack(pady=10)

        # Load and display the image
        print('****DEBUG image file =',image_file) #tutor had helped me put this (i forgot as to why)
        import os
        print(os.getcwd())
        image = Image.open(image_file)
        image = image.resize((120, 120))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(item_frame, image=photo)
        image_label.image = photo
        image_label.pack(side="left")

        # Create labels for name and price
        name_label = tk.Label(item_frame, text=name)
        name_label.pack(side="top")
        price_label = tk.Label(item_frame, text=f"${price}")
        price_label.pack(side="top")

        # Add a button to order
        order_button = tk.Button(item_frame, text="Add to Order", command=lambda n=name, p=price: self.add_to_order(n, p))
        order_button.pack(side="bottom")

#defing of where the order summery will be
    def create_order_summary(self):
        order_frame = tk.Frame(self.master)
        order_frame.pack(side="right", fill="y")

        self.order_label = tk.Label(order_frame, text="Order Summary:")
        self.order_label.pack()

        self.order_items = {}

#what items are beiing added and will double when added again
    def add_to_order(self, name, price):
        if name not in self.order_items:
            self.order_items[name] = 0
        self.order_items[name] += 1
        self.update_order_summary()
#defing the itwems of which will be added 
    def update_order_summary(self):
        order_text = "Order Summary:\n"
        for name, quantity in self.order_items.items():
            order_text += f"{name} x {quantity}\n"
        self.order_label.config(text=order_text)

        
root = tk.Tk()
app = MainWindow(root)
root.mainloop()
