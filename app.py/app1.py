def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative.")
    return round(price * quantity, 2)

def main():
    print("Shopping Bill Calculator")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        total = calculate_total(price, quantity)
        print(f"Total Bill: ${total}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()