def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        actual_price = price - (price * discount_percent / 100)
    else:
        actual_price = price
    return actual_price


p = float(input("Enter price: "))
d = float(input("Enter discount_percent: "))
final_price = calculate_discount(p, d)
print("Price after calculation: ", final_price)
