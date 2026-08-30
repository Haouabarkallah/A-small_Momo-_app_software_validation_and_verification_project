from app.payment import process_payment


def main():
    print(" MoMo Fee Payment ")

    try:
        amount = int(input("Enter amount (FCFA): "))
        pin = input("Enter 4-digit PIN: ")
        balance = int(input("Enter current balance (FCFA): "))

        result = process_payment(amount, pin, balance)

        print("\n--- Result ---")
        print(result["message"])

        if "fee" in result:
            print(f"Fee: {result['fee']} FCFA")
            print(f"Total: {result['total']} FCFA")

        if result.get("success"):
            print(f"Remaining balance: {result['remaining_balance']} FCFA")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
