def apply_discount(price , discount):

    if not isinstance (price, (int, float)):
        return "Price should be a Number"

    if not isinstance (discount, (int, float)):
            return "Discount should be a Number"

    if price <= 0:
         return "Price should be a Positive Number"

    if discount < 1 or discount > 100:
         return "The Discount amount should be between 1-100"

    discount_amount = price * (discount/100)
    final_price = price - discount_amount

    final_price= (final_price)
    return (final_price)

a = float(input("Enter Price: "))
b = float(input("Enter Discount: "))

result = apply_discount(a,b)
print(result)


