def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = (discount_percent * price)/100
        new_price = price - discount
        return new_price
        
    else:
        return price

total_cost = calculate_discount(int(input("Enter price: ")), int(input("Enter discount: ")))
print(f"The total price is {total_cost}")
    
    