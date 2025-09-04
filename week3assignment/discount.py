def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


if __name__ == "__main__":
    try:
        price_input = float(input("Enter the original price: "))
        discount_input = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        final_price = calculate_discount(price_input, discount_input)
        print(final_price)


