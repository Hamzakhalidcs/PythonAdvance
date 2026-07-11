while True:
    try:
        number = int(input("Enter a number: "))
        print(10 / number)

    except ValueError:
        print("Please enter a valid number")

    except ZeroDivisionError:
        print("Number cannot be zero")

    else:
        print("No Exception Occurred")

    finally:
        print("Execution Completed")

    # Ask if they want to continue
    again = input("\nWould you like to make another calculation? (yes/no): ").strip().lower()
    
    if again != "yes":
        print("Goodbye!")
        break