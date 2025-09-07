class Menu:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items
    def add_item(self, item):
        if item in self.items:
            print(f"{item} is already present in the list")
        else:
            self.items.append(item)
    def remove_item(self, item):
        if item not in self.items:
            print(f"{item} is not present in list")
        else:
            menu.items.remove(item)
    def check_availability(self, item):
        if item in self.items:
            print(f"{item} is available in menu")
        else:
            print(f"{item} is not available in menu")
    def show_menu(self):
        print("Updated menu:", self.items)
menu_items=input("Enter menu items: ").split(",")
print("MENU: ",menu_items)
menu=Menu(menu_items)
add=input("Enter item to be added: ")
menu.add_item(add)
remove=input("Enter item to be removed: ")
menu.remove_item(remove)
menu.show_menu()
aval=input("Enter an item to check availability: ")
menu.check_availability(aval)