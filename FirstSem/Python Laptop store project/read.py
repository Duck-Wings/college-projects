def read_laptops(filename):
    '''
    Reads laptop data from a file and returns it as a dictionary.

    Each line of the file should contain laptop data in the following format:
    name,brand,model,price,quantity,processor,graphics

    Args:
    filename (str): Name of the file to read.

    Returns:
    laptops (dict): A dictionary where the keys are laptop names and
                     the values are dictionaries containing the laptop data.
    '''
    laptops = {}
    with open(filename, 'r') as f:
        for line in f:
            # Split the line into individual data points
            data = line.strip().split(',')
            # Extract the name of the laptop
            name = data[0]
            if len(data) >= 7:
                # Extract the remaining laptop data if it exists
                brand = data[1]
                model = data[2]
                price = float(data[3])
                quantity = int(data[4])
                processor = data[5]
                graphics = data[6]
            else:
                # Handle unexpected data format
                brand = ''
                model = ''
                price = 0.0
                quantity = 0
                processor = ''
                graphics = ''

            # Add the laptop data to the dictionary
            laptops[name] = {
                'brand': brand,
                'model': model,
                'price': price,
                'quantity': quantity,
                'processor': processor,
                'graphics': graphics
            }
    return laptops
