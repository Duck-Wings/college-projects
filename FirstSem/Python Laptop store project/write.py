def write_laptops(filename: str, laptops: dict) -> None:
    """
    Write a dictionary of laptops to a txt file with the specified filename.

    Args:
        filename (str): The filename to write to.
        laptops (dict): A dictionary containing laptop data.

    Returns:
        None
    """
    # Open the file for writing
    with open(filename, 'w') as file:
        # Write each laptop to the file in CSV format
        for name, laptop in laptops.items():
            brand = laptop['brand']
            price = laptop['price']
            model = laptop['model']
            quantity = laptop['quantity']
            processor = laptop['processor']
            graphics = laptop['graphics']
            file.write(f"{name},{brand},{model},{price:.2f},{quantity},{processor},{graphics}\n")
