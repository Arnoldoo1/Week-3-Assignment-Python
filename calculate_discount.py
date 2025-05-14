# Function to calculate final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount if 20% or higher
        final_price = price - (price * (discount_percent / 100))
    else:
        final_price = price  # Return original price if discount is less than 20%
    return final_price

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(price, discount_percent)
print(f"Final price after discount: ${final_price:.2f}")
