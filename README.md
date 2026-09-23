# Catálogo de piezas coleccionables

Programa de consola escrito en Python que permite gestionar un catálogo básico
de piezas coleccionables: registrar piezas, consultarlas, filtrarlas, calcular
métricas y validar todos los datos que introduce el usuario.

Es la solución al **Reto Python nivel II — Catálogo básico de coleccionables**.

Solo usa la librería estándar de Python, no hace falta instalar nada.

## Estructura del proyecto

Este repositorio hace de carpeta `catalogo_coleccionables/` del enunciado:

```
catalogo_coleccionables/
├── catalog.py        -> Funciones del catálogo (agregar, listar, buscar, quitar, filtrar, métricas)
├── validations.py    -> Funciones de validación de los datos de una pieza
├── main.py           -> Programa principal, menú y flujo de ejecución
└── README.md
```

La lógica está repartida en tres módulos y no se duplica:

- `main.py` importa `catalog.py`.
- `catalog.py` importa `validations.py`.
- Las validaciones viven solo en `validations.py`.

## Cómo ejecutar

Hace falta tener Python 3 instalado. Desde la carpeta del proyecto:

```
python main.py
```

En Linux o macOS puede que haya que escribir `python3 main.py`.

## Cómo es una pieza

Cada pieza es un diccionario con esta forma:

```python
{
    "id": "p1",
    "name": "Funko Batman",
    "category": "Figuras",
    "price": 25.0,
    "status": "disponible",
    "description": "pieza usada en caja"
}
```

## Reglas de validación

- Ningún campo obligatorio puede quedar vacío.
- El precio tiene que ser un número mayor que cero.
- El estado solo puede ser `disponible`, `reservada` o `vendida`.
- La descripción tiene que contener la palabra `usada` o `certificada`.

Si algo de esto falla se lanza un `ValueError` con un mensaje claro. Las
funciones de validación nunca imprimen nada: quien las llama es el que decide
qué mensaje mostrar.

## Funciones de cada archivo

### `validations.py`

| Función | Qué hace |
| --- | --- |
| `validate_not_empty(value, field_name)` | Comprueba que un campo no venga vacío e indica su nombre en el error. |
| `validate_price(price)` | Comprueba que el precio sea numérico y mayor que cero. |
| `validate_status(status)` | Comprueba que el estado esté entre los permitidos. |
| `validate_description(description)` | Comprueba que la descripción lleve `usada` o `certificada`. |

También define la constante `ALLOWED_STATUSES` con los tres estados válidos.

### `catalog.py`

| Función | Qué devuelve |
| --- | --- |
| `add_piece(id, name, category, price, status, description)` | La pieza como diccionario, después de validar todos los datos. |
| `list_pieces(catalog)` | Lista con los nombres de todas las piezas. |
| `find_piece_by_id(catalog, id)` | La pieza con ese id, o `None` si no está (no es un error). |
| `remove_piece(catalog, id)` | `True` si la quitó, `False` si la pieza no existía. |
| `piece_exists(catalog, id)` | `True` o `False`, sin lanzar errores. |
| `get_catalog_summary(catalog)` | Diccionario con cuántas piezas hay por categoría. |
| `get_pieces_by_category(catalog, category)` | Lista con los nombres de las piezas de esa categoría. |
| `filter_by_status(catalog, status)` | Lista de piezas con ese estado; error si el estado no es válido. |
| `filter_by_min_price(catalog, min_price)` | Lista de piezas más caras que ese precio; error si no es un número. |
| `get_average_price(catalog)` | Precio promedio, o `0` si el catálogo está vacío. |

Todas comprueban primero que el catálogo recibido sea una lista.

### `main.py`

Monta el menú y va llamando a las funciones de `catalog.py`. Cada opción tiene
su propia función, así el bucle del menú queda limpio:

- `show_menu()` — imprime las opciones.
- `ask_price()` — pide el precio y lo convierte a número.
- `print_piece(piece)` — muestra una pieza en una sola línea.
- `option_add_piece`, `option_list_pieces`, `option_available_pieces`,
  `option_average_price`, `option_find_piece`, `option_remove_piece` — una por
  cada opción del menú.
- `main()` — mantiene el programa en marcha hasta que se elige salir.

## El menú

```
=== Catalogo de coleccionables ===
1. Agregar pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Ver precio promedio
5. Buscar pieza por ID
6. Eliminar pieza
7. Salir
```

## Ejemplo de uso

```
Elige una opcion: 1

--- Agregar pieza ---
ID: p1
Nombre: Funko Batman
Categoria: Figuras
Precio: 25
Estado (disponible, reservada, vendida): disponible
Descripcion: pieza usada en caja
Pieza agregada correctamente.

Elige una opcion: 2

--- Piezas del catalogo ---
p1 | Funko Batman | Figuras | 25.0 | disponible

Elige una opcion: 4

--- Precio promedio ---
El precio promedio es 25.0 euros.
```

Si se mete un dato mal, el programa avisa y sigue funcionando:

```
Elige una opcion: 1

--- Agregar pieza ---
ID: p2
Nombre: Moneda romana
Categoria: Monedas
Precio: barato
No se pudo agregar la pieza: El precio debe ser un numero.
```

## Notas

- El catálogo se guarda en memoria mientras el programa está abierto; al
  cerrarlo se pierde.
- Los errores se controlan con `try / except`, así que el programa no se rompe
  aunque el usuario escriba cualquier cosa.
