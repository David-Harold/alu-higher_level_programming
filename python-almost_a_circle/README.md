# python-almost_a_circle

Advanced Python: object-oriented programming with inheritance,
properties, `*args`/`**kwargs`, JSON serialization, and full unit
test coverage.

## Description

| File | Description |
| --- | --- |
| `models/__init__.py` | Makes `models` a Python package |
| `models/base.py` | `Base`: manages `id`, plus JSON/file (de)serialization (`to_json_string`, `save_to_file`, `from_json_string`, `create`, `load_from_file`) |
| `models/rectangle.py` | `Rectangle(Base)`: validated `width`/`height`/`x`/`y` properties, `area`, `display`, `__str__`, `update`, `to_dictionary` |
| `models/square.py` | `Square(Rectangle)`: `size` property, `__str__`, `update`, `to_dictionary` |
| `tests/test_models/test_base.py` | Unit tests for `Base` |
| `tests/test_models/test_rectangle.py` | Unit tests for `Rectangle` |
| `tests/test_models/test_square.py` | Unit tests for `Square` |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line
- Every module, class, and method has a docstring
- All files, classes, and methods are unit tested: run the full
  suite with `python3 -m unittest discover tests`

## Key concepts

- **`Base`** centralizes `id` management so every subclass gets it
  for free — pass an `id`, or one is auto-assigned from a private
  class counter (`__nb_objects`).
- **Private attributes with property getters/setters** (`Rectangle`'s
  `width`, `height`, `x`, `y`) let the class validate every
  assignment, not just the ones made in `__init__`. Wrong type raises
  `TypeError`, wrong value raises `ValueError`, both with an exact
  message spelled out in the setter.
- **`Square` inherits from `Rectangle`**, not `Base` — it calls
  `super().__init__(size, size, x, y, id)` and adds no new attributes;
  `size` is just a property that reads/writes `width`/`height`
  together, so all of `Rectangle`'s validation is reused for free.
- **`update(*args, **kwargs)`** — positional args are applied in a
  fixed order (`id, width, height, x, y` for `Rectangle`; `id, size,
  x, y` for `Square`); if any positional args are given, `**kwargs`
  is ignored entirely, not merged.
- **`Base.create`** builds a "dummy" instance with placeholder
  mandatory args, then calls `update(**dictionary)` on it — this is
  how a full object gets reconstructed from a plain dict without
  using `eval`.
- **JSON round-trip**: `to_dictionary` → `to_json_string` → write to
  `<ClassName>.json` (`save_to_file`) → read back → `from_json_string`
  → `create` per dict (`load_from_file`). Each piece is tested and
  used independently by the next.
- **Testing `display()`** requires capturing stdout — the test suite
  uses `unittest.mock.patch("sys.stdout", new=StringIO())` to assert
  on exact printed output, including blank lines from `y` and leading
  spaces from `x`.

## Author

David-Harold
