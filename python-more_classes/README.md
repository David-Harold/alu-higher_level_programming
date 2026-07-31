# python-more_classes

Advanced Python: object-oriented programming with classes, private
attributes, properties, class methods, static methods, and magic
methods (`__str__`, `__repr__`, `__del__`).

## Description

This project builds a `Rectangle` class incrementally across ten
files, each adding one new concept on top of the last:

| File | Adds |
| --- | --- |
| `0-rectangle.py` | Empty class |
| `1-rectangle.py` | Private `width`/`height` with property getters/setters, type and value validation |
| `2-rectangle.py` | `area()` and `perimeter()` |
| `3-rectangle.py` | `__str__` (prints the rectangle using `#`) |
| `4-rectangle.py` | `__repr__` (eval-able representation) |
| `5-rectangle.py` | `__del__` (prints `Bye rectangle...` on deletion) |
| `6-rectangle.py` | `number_of_instances` class attribute |
| `7-rectangle.py` | `print_symbol` class attribute |
| `8-rectangle.py` | `bigger_or_equal()` static method |
| `9-rectangle.py` | `square()` class method |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (`python3` interpreter, version 3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line
- All modules, classes, and functions/methods are documented
- No modules are imported

## Usage

Each file is standalone and can be imported directly:

```
$ cat main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

$ ./main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

## Rectangle class (final version, `9-rectangle.py`)

- `width` / `height`: private instance attributes, accessed through
  properties. Setting a non-integer raises `TypeError`; setting a
  negative value raises `ValueError`.
- `number_of_instances`: public class attribute, incremented on
  `__init__`, decremented on `__del__`.
- `print_symbol`: public class attribute (default `#`) used by
  `__str__` to render the rectangle; can be reassigned to any type.
- `area()`: returns `width * height`.
- `perimeter()`: returns `2 * (width + height)`, or `0` if either
  dimension is `0`.
- `__str__`: renders the rectangle using `print_symbol`, or `""` if
  either dimension is `0`.
- `__repr__`: returns a string such as `Rectangle(2, 4)` that can be
  passed to `eval()` to recreate an equivalent instance.
- `__del__`: prints `Bye rectangle...` when an instance is deleted.
- `bigger_or_equal(rect_1, rect_2)` (static method): returns whichever
  rectangle has the larger area (`rect_1` on a tie). Raises `TypeError`
  if either argument isn't a `Rectangle`.
- `square(size=0)` (class method): returns a new `Rectangle` with
  `width == height == size`.

## Author

David-Harold
