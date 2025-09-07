def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = total * 0.10
        total -= discount
        return f"10% discount applied!\nFinal Price: {int(total)}"
    else:
        return f"Total Price: {int(total)}"
cart1 = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print("---- CART 1-----")
print(calculate_total(cart1))  
cart2 = {
    'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500,
    'Keyboard': 1500, 'Monitor': 10000, 'USB': 800
}
print("---- CART 2-----")
print(calculate_total(cart2))  
cart3 = {}
print("---- CART 3-----")
print(calculate_total(cart3))  