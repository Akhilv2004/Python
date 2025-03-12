while True:
    print("\nMenu:")
    print("1. Check even or odd")
    print("2. Check positive, negative, or zero")
    print("3. Generate factors of a number")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Even" if num % 2 == 0 else "Odd")
    
    elif choice == 2:
        num = float(input("Enter a number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    elif choice == 3:
        num = int(input("Enter a number: "))
        print("Factors:", [i for i in range(1, num + 1) if num % i == 0])
    
    elif choice == 4:
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")