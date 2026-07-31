# python-inheritance

Advanced Python: class inheritance, `dir()`/introspection, `type()` vs
`isinstance()`, private attributes across a class hierarchy, and
building a small geometry class tree (`BaseGeometry` → `Rectangle` →
`Square`).

## Description

| File | Description |
| --- | --- |
| `0-lookup.py` | `lookup(obj)` — returns `dir(obj)`, the list of an object's available attributes and methods |
| `1-my_list.py` | `MyList(list)` — adds `print_sorted()`, which prints the list in ascending order without modifying it |
| `tests/1-my_list.txt` | Doctest suite for `MyList` |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` — `True` only if `obj` is *exactly* an instance of `a_class` (`type(obj) is a_class`) |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` — `True` if `obj` is an instance of `a_class` or any of its subclasses (`isinstance`) |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` — `True` only if `obj`'s class is a *subclass* of `a_class` (excludes an exact match) |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | Adds `area()`, which raises `Exception("area() is not implemented")` |
| `7-base_geometry.py` | Adds `integer_validator(name, value)`, validating a positive integer |
| `tests/7-base_geometry.txt` | Doctest suite for `integer_validator` and `area` |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` — private `width`/`height`, validated on init, no getters/setters |
| `9-rectangle.py` | Adds `area()` and `__str__` (`[Rectangle] <width>/<height>`) |
| `10-square.py` | `Square(Rectangle)` — private `size`, validated on init; inherits `area()` and `__str__` from `Rectangle` |
| `11-square.py` | Overrides `__str__` to print `[Square] <size>/<size>` |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line
- No modules are imported directly (`8-rectangle.py` through `11-square.py`
  load prior tasks via `__import__()`, per the project's own convention)
- All modules, classes, and functions are documented

## Key concepts

- **`dir(obj)`** lists every attribute and method an object exposes,
  including everything inherited from its parent classes — that's all
  `lookup()` is.
- **`type(obj) is a_class`** checks for an exact class match.
  **`isinstance(obj, a_class)`** also accepts subclasses.
  **`inherits_from()`** deliberately excludes the exact-match case, so
  it only reports "yes" when a *subclass* is involved (e.g. `bool`
  inherits from `int`, but `is_same_class(True, int)` is `False` while
  `inherits_from(True, int)` is `True`).
- **Private attributes and name mangling**: `self.__width` inside
  `Rectangle` is stored as `_Rectangle__width` on the instance — the
  mangled name is based on *where the attribute is defined*, not where
  it's accessed. That's why `Square.__str__` (in `11-square.py`) reads
  `self._Rectangle__width` directly instead of `self.__width` — writing
  `self.__width` inside `Square` would look for `_Square__width`, which
  doesn't exist, and raise an `AttributeError`.
- **`Square` reuses `Rectangle`'s `area()`** by calling
  `super().__init__(size, size)` — since `area()` just multiplies the
  stored width and height, setting both to `size` makes it correct
  without needing to override it.

## Author

David-Harold
