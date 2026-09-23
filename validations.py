# Funciones de validacion de los datos de una pieza.
# Estas funciones NO imprimen nada: solo lanzan ValueError si algo esta mal.


def validate_not_empty(value, field_name):
    """Valida que un campo de texto no venga vacio."""
    if value is None:
        raise ValueError("El campo '" + field_name + "' no puede estar vacio.")

    # Quitamos los espacios de los lados para que " " tambien cuente como vacio
    if str(value).strip() == "":
        raise ValueError("El campo '" + field_name + "' no puede estar vacio.")

    return True


def validate_price(price):
    """Valida que el precio sea un numero y que sea mayor que cero."""
    # bool tambien es int en Python, por eso lo descartamos aparte
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("El precio debe ser un numero.")

    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")

    return True