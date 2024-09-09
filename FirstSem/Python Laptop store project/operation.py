import datetime
from write import write_laptops
from read import read_laptops

def sell_laptops(laptops):
    """
    Sells laptops to a customer and saves transaction details to a file.

    Args:
        laptops (dict): A dictionary containing laptop data.

    Returns:
        None
    """

    # Prompt the user to enter the laptop name to sell
    name = input("Enter the laptop name: ")

    # Check if the laptop exists in the inventory
    if name not in laptops:
        print("Laptop not found.")
        return

    # Get the laptop details
    laptop = laptops[name]

    # Prompt the user to enter the quantity to sell
    quantity = None
    while not quantity:
        try:
            quantity = int(input("Enter the quantity to sell: "))
            if quantity <= 0:
                print("Invalid quantity. Please enter a positive number.\n\n")
                quantity = None
        except ValueError:
            print("Invalid input. Please enter a valid quantity.\n\n")

    # Check if there is sufficient stock
    if quantity > laptop['quantity']:
        print("Insufficient stock.\n\n")
        return

    # Prompt the user to enter the customer name
    customer_name = input("Enter the customer name: ")

    # Prompt the user to enter the shipping cost
    shipping_cost = None
    while not shipping_cost:
        try:
            shipping_cost = float(input("Enter the shipping cost: "))
            if shipping_cost < 0:
                print("Invalid shipping cost. Please enter a non-negative number.\n\n")
                shipping_cost = None
        except ValueError:
            print("Invalid input. Please enter a valid shipping cost.\n\n")

    # Update the inventory
    laptop['quantity'] -= quantity
    laptops[name] = laptop

    # Calculate the total amount, VAT amount and total amount with shipping and VAT
    total_amount = laptop['price'] * quantity
    vat_amount = total_amount * 0.13
    total_amount_with_shipping_vat = total_amount + shipping_cost + vat_amount

    # Generate a filename for the transaction details file
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"Sale_{name}_{customer_name}_{timestamp}.txt"

    # Save the transaction details to a file
    with open(filename, 'w') as file:
        file.write(f"Laptop Name: {name}\n")
        file.write(f"Brand: {laptop['brand']}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Date and Time of Purchase: {datetime.datetime.now()}\n")
        file.write(f"Total Amount: ${total_amount:.2f}\n")
        file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
        file.write(f"VAT Amount: ${vat_amount:.2f}\n")
        file.write(f"Total Amount with Shipping and VAT: ${total_amount_with_shipping_vat:.2f}\n")

    # Print the transaction details and prompt the user to sell more laptops
    print(f"{quantity} {name} laptops sold to {customer_name}. Transaction details saved to {filename}.")
    write_laptops('laptop.txt', laptops)
    choice = input("Do you want to sell more laptops? (Y/N): ")
    if choice.lower() == 'n':
        print("Thank you for using our service!\n\n")
    elif choice.lower() == 'y':
        sell_laptops(laptops)
    else:
        print("Invalid input. Please enter Y or N.\n\n")

        



def order_laptops(laptops):
    """
    This function allows the user to order laptops and saves the transaction details to a file.
    It takes a dictionary of laptops as a parameter and updates it with the new order.

    Args:
        laptops (dict): A dictionary of laptops with their details.

    Returns:
        None
    """
    try:
        # Get laptop details from user input
        name = input("Enter the laptop name: ")
        brand = input("Enter the brand: ")
        model = input("Enter the model: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        processor = input("Enter the processor: ")
        graphics = input("Enter the graphics: ")

        # Check if price and quantity are valid
        if price <= 0 or quantity <= 0:
            print("Quantity and price must be greater than zero.\n\n")
            return

    except ValueError:
        print("Invalid input. Please enter numeric values for price and quantity.\n\n")
        return

    # Get the laptop from the dictionary, or create a new one if it doesn't exist
    laptop = laptops.get(name, {})
    laptop['brand'] = brand
    laptop['model'] = model
    laptop['price'] = price
    laptop['quantity'] = laptop.get('quantity', 0) + quantity
    laptop['processor'] = processor
    laptop['graphics'] = graphics
    laptops[name] = laptop
    write_laptops('laptop.txt', laptops)

    try:
        # Write transaction details to file
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        filename = f"Order_{name}_{brand}_{timestamp}.txt"
        net_amount = price * quantity
        vat_amount = net_amount * 0.13
        gross_amount = net_amount + vat_amount
        with open(filename, 'w') as file:
            file.write(f"Distributor Name: My Laptop Shop\n")
            file.write(f"Laptop Name: {name}\n")
            file.write(f"Brand: {brand}\n")
            file.write(f"Model: {model}\n")
            file.write(f"Date and Time of Purchase: {datetime.datetime.now()}\n")
            file.write(f"Net Amount: ${net_amount:.2f}\n")
            file.write(f"VAT Amount: ${vat_amount:.2f}\n")
            file.write(f"Gross Amount: ${gross_amount:.2f}\n")
        print(f"{quantity} {name} laptops ordered from {brand}. Transaction details saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while processing the order: {str(e)}")

    # Ask user if they want to order more laptops
    choice = input("Do you want to order more laptops? (Y/N): ")
    if choice.lower() == 'n':
        print("Thank you for using our service!\n\n")
    elif choice.lower() == 'y':
        order_laptops(laptops)
    else:
        print("Invalid input. Please enter Y or N.\n\n")




def display_inventory(laptops):
    """
    Display the current inventory of laptops.

    Args:
        laptops (dict): A dictionary of laptops, where the keys are laptop names and the values are dictionaries
        containing the laptop's brand, price, quantity, processor, and graphics.

    Returns:
        None

    """
    # Print the header for the table
    print("Current Inventory:")
    print("------------------------------------------------------------------------------------")
    print("Laptop Name        Brand           Price       Quantity    Processor           Graphics")
    print("------------------------------------------------------------------------------------")

    # Iterate over each laptop in the dictionary and print its information
    for name, laptop in laptops.items():
        brand = laptop['brand']
        price = laptop['price']
        quantity = laptop['quantity']
        processor = laptop['processor']
        graphics = laptop['graphics']
        print(f"{name.ljust(20)}{brand.ljust(15)}${price:.2f}{' ' * 6}{str(quantity).ljust(10)}{processor.ljust(20)}{graphics}")
        print("------------------------------------------------------------------------------------")

laptops=read_laptops('laptop.txt')
display_inventory(laptops)
