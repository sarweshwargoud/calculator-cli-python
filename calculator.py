def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation with zero division check"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    """Safely get a number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n=== Calculator Menu ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def main():
    """Main calculator function"""
    print("Welcome to the Calculator CLI App!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select 1-5.")
            continue
        
        # Get numbers from user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Perform calculation based on user choice
        try:
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()