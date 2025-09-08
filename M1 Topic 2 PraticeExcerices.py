# Excercise 1: Calculate Total Cost with Discount
item_price = 49.99
quantity_purchased = 5 
discount_percent = 0.15

# Calculate Subtotal
subtotal = item_price * quantity_purchased 
discount_amount = subtotal * discount_percent
final_price = subtotal - discount_amount 


# Print the final_price formatted to 2 decimal places.
print("final Price: $", format(final_price, ".2f"))
print(f"Final price after 15% discount is: ${final_price:.2f}")