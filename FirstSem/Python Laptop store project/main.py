from read import read_laptops
from operation import sell_laptops, order_laptops, display_inventory
from write import write_laptops

# Setting up loop for main program
loop = True
# Introduction Part or the Starting Part of the UI.
print(
    "=====================================================================================================================================================\n"
)
print("\t\t\t\t\t\t\tWelcome to Laptop Management System \n ")
print(
    "=====================================================================================================================================================\n"
)


def main():
    """
    The main function that contains the menu for the Laptop Management System.
    """
    loop = True
    # Read the laptop data
    laptops = read_laptops("laptop.txt")

    while loop:
        # Display the menu options to the user.
        print("  \n\t\t\t\t\t\t\t    *** Laptop Shop Menu ***")
        print("\n\n1. Display Inventory")
        print("\n2. Sell Laptops")
        print("\n3. Order Laptops")
        print("\n4. Exit")

        try:
            choice = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
            continue

        # Perform the action based on the user's choice.
        if choice == 1:
            display_inventory(laptops)
        elif choice == 2:
            sell_laptops(laptops)
        elif choice == 3:
            order_laptops(laptops)
        elif choice == 4:
            # Save the laptop data and exit the program.
            write_laptops("laptop.txt", laptops)
            print("Thank you for using our service!\n\n")
            print("Exiting the program...")
            loop = False
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
