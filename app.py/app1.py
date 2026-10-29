def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def calculate_discounted_total(price: float, quantity: int, discount_percent: float = 10.0) -> tuple:
    subtotal = calculate_total(price, quantity)
    discount = subtotal * (discount_percent / 100)
    final_total = subtotal - discount
    return subtotal, discount, final_total

def main():
    print("=== Shopping Bill Calculator ===")
    print("1. Calculate total bill")
    print("2. Calculate total with discount")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            total = calculate_total(price, quantity)
            print(f"Total bill: ${total:.2f}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == "2":
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            discount_percent = float(input("Enter discount percentage: "))
            subtotal, discount, final_total = calculate_discounted_total(price, quantity, discount_percent)
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Discount: ${discount:.2f}")
            print(f"Final total after discount: ${final_total:.2f}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == "3":
        print("Goodbye!")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()