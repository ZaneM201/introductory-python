product_cart = [100, 200, 300, 400, 500]

def total(product_cart):
    total=0
    for product in product_cart:
        total += product
    return total

total = total(product_cart)

def average(total, length):
    return total / length

cart_lenght = len(product_cart)
cart_average = average(total, cart_lenght)

print(f"Total: ${total}")
print(f"Average: ${cart_average}")
    