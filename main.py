"""Main program of the collectibles catalog."""

import catalog as catalog_module


def show_menu():
    """Print the available options of the program."""
    print("")
    print("=== Collectibles catalog ===")
    print("1. Add piece")
    print("2. Show all pieces")
    print("3. Show available pieces")
    print("4. Show average price")
    print("5. Find piece by ID")
    print("6. Remove piece")
    print("7. Exit")


def ask_price():
    """Ask for the price from the keyboard and return it as a number."""
    raw_price = input("Price: ").strip()

    try:
        return float(raw_price)
    except ValueError:
        raise ValueError("The price must be a number.")


def option_add_piece(catalog):
    """Ask for the data of a new piece and add it to the catalog."""
    print("")
    print("--- Add piece ---")

    piece_id = input("ID: ").strip()
    name = input("Name: ").strip()
    category = input("Category: ").strip()

    try:
        price = ask_price()
        status = input("Status (available, reserved, sold): ").strip()
        description = input("Description: ").strip()

        if catalog_module.piece_exists(catalog, piece_id):
            raise ValueError("A piece with id '" + piece_id + "' already exists.")

        piece = catalog_module.add_piece(
            piece_id, name, category, price, status, description
        )
        catalog.append(piece)
        print("Piece added successfully.")

    except ValueError as error:
        print("The piece could not be added: " + str(error))


def print_piece(piece):
    """Print the data of a piece on a single line."""
    print(
        piece["id"]
        + " | "
        + piece["name"]
        + " | "
        + piece["category"]
        + " | "
        + str(piece["price"])
        + " | "
        + piece["status"]
    )


def option_list_pieces(catalog):
    """Print all the stored pieces."""
    print("")
    print("--- Catalog pieces ---")

    if len(catalog) == 0:
        print("There are no pieces stored yet.")
        return

    for piece in catalog:
        print_piece(piece)


def option_available_pieces(catalog):
    """Print only the pieces whose status is available."""
    print("")
    print("--- Available pieces ---")

    try:
        available = catalog_module.filter_by_status(catalog, "available")
    except ValueError as error:
        print("The pieces could not be filtered: " + str(error))
        return

    if len(available) == 0:
        print("There are no available pieces right now.")
        return

    for piece in available:
        print_piece(piece)


def option_average_price(catalog):
    """Print the average price of the pieces in the catalog."""
    print("")
    print("--- Average price ---")

    average = catalog_module.get_average_price(catalog)

    if len(catalog) == 0:
        return

    print("The average price is " + str(round(average, 2)) + " euros.")


def option_find_piece(catalog):
    """Ask for an id and print the piece if it is in the catalog."""
    print("")
    print("--- Find piece by ID ---")

    piece_id = input("ID to find: ").strip()

    if piece_id == "":
        print("You must enter an id.")
        return

    piece = catalog_module.find_piece_by_id(catalog, piece_id)

    if piece is None:
        print("There is no piece with id '" + piece_id + "'.")
        return

    print_piece(piece)
    print("Description: " + piece["description"])


def option_remove_piece(catalog):
    """Ask for an id and remove that piece from the catalog."""
    print("")
    print("--- Remove piece ---")

    piece_id = input("ID to remove: ").strip()

    if piece_id == "":
        print("You must enter an id.")
        return

    removed = catalog_module.remove_piece(catalog, piece_id)

    if removed:
        print("Piece removed successfully.")


def main():
    """Keep the menu running in a loop until the user chooses to exit."""
    catalog = []

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "7":
            print("Goodbye.")
            break
        elif option == "1":
            option_add_piece(catalog)
        elif option == "2":
            option_list_pieces(catalog)
        elif option == "3":
            option_available_pieces(catalog)
        elif option == "4":
            option_average_price(catalog)
        elif option == "5":
            option_find_piece(catalog)
        elif option == "6":
            option_remove_piece(catalog)
        else:
            print("Invalid option, choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
