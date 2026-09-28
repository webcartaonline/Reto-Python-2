# Collectible pieces catalog

A console program written in Python to manage a basic catalog of collectible
pieces: register pieces, look them up, filter them, compute metrics and
validate all the data entered by the user.

It is the solution to the **Python Challenge level II — Basic collectibles catalog**.

It only uses the Python standard library, so there is nothing to install.

## Project structure

This repository acts as the `catalogo_coleccionables/` folder from the assignment:

```
catalogo_coleccionables/
├── catalog.py        -> Catalog functions (add, list, find, remove, filter, metrics)
├── validations.py    -> Validation functions for the data of a piece
├── main.py           -> Main program, menu and execution flow
└── README.md
```

The logic is split into three modules and is not duplicated:

- `main.py` imports `catalog.py`.
- `catalog.py` imports `validations.py`.
- Validations live only in `validations.py`.

## How to run

You need Python 3 installed. From the project folder:

```
python main.py
```

On Linux or macOS you may need to type `python3 main.py`.

## What a piece looks like

Each piece is a dictionary with this shape:

```python
{
    "id": "p1",
    "name": "Funko Batman",
    "category": "Figures",
    "price": 25.0,
    "status": "available",
    "description": "used piece in box"
}
```

## Validation rules

- No required field can be empty.
- The price must be a number greater than zero.
- The status can only be `available`, `reserved` or `sold`.
- The description must contain the word `used` or `certified`.

If any of these checks fails, a `ValueError` with a clear message is raised.
The validation functions never print anything: the caller decides which
message to show.

## Functions in each file

### `validations.py`

| Function | What it does |
| --- | --- |
| `validate_not_empty(value, field_name)` | Checks that a field is not empty and names the field in the error. |
| `validate_price(price)` | Checks that the price is numeric and greater than zero. |
| `validate_status(status)` | Checks that the status is one of the allowed ones. |
| `validate_description(description)` | Checks that the description contains `used` or `certified`. |

It also defines the `ALLOWED_STATUSES` constant with the three valid statuses.

### `catalog.py`

| Function | What it returns |
| --- | --- |
| `add_piece(id, name, category, price, status, description)` | The piece as a dictionary, after validating all the data. |
| `list_pieces(catalog)` | A list with the names of all the pieces. |
| `find_piece_by_id(catalog, id)` | The piece with that id, or `None` if it is not there (not an error). |
| `remove_piece(catalog, id)` | `True` if it was removed, `False` if the piece did not exist. |
| `piece_exists(catalog, id)` | `True` or `False`, without raising errors. |
| `get_catalog_summary(catalog)` | A dictionary with how many pieces there are per category. |
| `get_pieces_by_category(catalog, category)` | A list with the names of the pieces in that category. |
| `filter_by_status(catalog, status)` | A list of pieces with that status; error if the status is not valid. |
| `filter_by_min_price(catalog, min_price)` | A list of pieces more expensive than that price; error if it is not a number. |
| `get_average_price(catalog)` | The average price, or `0` if the catalog is empty. |

All of them first check that the received catalog is a list.

### `main.py`

Builds the menu and calls the functions in `catalog.py`. Each option has its
own function, so the menu loop stays clean:

- `show_menu()` — prints the options.
- `ask_price()` — asks for the price and converts it to a number.
- `print_piece(piece)` — prints a piece on a single line.
- `option_add_piece`, `option_list_pieces`, `option_available_pieces`,
  `option_average_price`, `option_find_piece`, `option_remove_piece` — one for
  each menu option.
- `main()` — keeps the program running until the user chooses to exit.

## The menu

```
=== Collectibles catalog ===
1. Add piece
2. Show all pieces
3. Show available pieces
4. Show average price
5. Find piece by ID
6. Remove piece
7. Exit
```

## Usage example

```
Choose an option: 1

--- Add piece ---
ID: p1
Name: Funko Batman
Category: Figures
Price: 25
Status (available, reserved, sold): available
Description: used piece in box
Piece added successfully.

Choose an option: 2

--- Catalog pieces ---
p1 | Funko Batman | Figures | 25.0 | available

Choose an option: 4

--- Average price ---
The average price is 25.0 euros.
```

If a value is wrong, the program warns the user and keeps running:

```
Choose an option: 1

--- Add piece ---
ID: p2
Name: Roman coin
Category: Coins
Price: cheap
The piece could not be added: The price must be a number.
```

## Notes

- The catalog is kept in memory while the program is open; it is lost when
  the program closes.
- Errors are handled with `try / except`, so the program does not crash
  whatever the user types.
