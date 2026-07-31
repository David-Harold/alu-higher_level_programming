# python-input_output

Advanced Python: reading and writing files, JSON serialization, and
using `__dict__` to turn objects into simple, serializable
dictionaries.

## Description

| File | Description |
| --- | --- |
| `0-read_file.py` | `read_file(filename)` — reads a UTF-8 text file and prints its contents to stdout |
| `1-write_file.py` | `write_file(filename, text)` — writes (creates/overwrites) a UTF-8 file, returns the number of characters written |
| `2-append_write.py` | `append_write(filename, text)` — appends to a UTF-8 file (creating it if needed), returns the number of characters added |
| `3-to_json_string.py` | `to_json_string(my_obj)` — returns the JSON string representation of an object |
| `4-from_json_string.py` | `from_json_string(my_str)` — returns the Python object represented by a JSON string |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` — writes an object's JSON representation to a file |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` — reads a JSON file and returns the object it represents |
| `7-add_item.py` | Script: appends all CLI arguments to the list stored in `add_item.json` (creating the file if it doesn't exist) |
| `8-class_to_json.py` | `class_to_json(obj)` — returns `obj.__dict__`, a JSON-serializable dictionary of an object's attributes |
| `9-student.py` | `Student` class with `first_name`, `last_name`, `age`, and `to_json()` |
| `10-student.py` | Adds an optional `attrs` filter to `to_json()`, to return only selected attributes |
| `11-student.py` | Adds `reload_from_json(json)`, which restores an instance's attributes from a dictionary |
| `12-pascal_triangle.py` | `pascal_triangle(n)` — returns Pascal's triangle as a list of lists, or `[]` if `n <= 0` |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line
- Files that don't need it (`0`-`2`, `8`-`12`) import no modules;
  `3`-`6` use the `json` module (unavoidable for JSON (de)serialization),
  and `7` uses `sys` (for CLI arguments) alongside `5` and `6`
- All modules, classes, and functions are documented

## Key concepts

- **`with open(...)`** is used everywhere a file is touched, so file
  handles are always closed automatically, even if an error occurs
  mid-read/write.
- **`json.dumps`/`json.loads`** convert between Python objects and JSON
  strings in memory; **`json.dump`/`json.load`** do the same directly
  against an open file, skipping the intermediate string.
- Only `list`, `dict`, `str`, `int`, `float`, `bool`, and `None` are
  JSON-serializable by default — a `set` (as in tasks 3 and 5) raises
  `TypeError`, which is expected, not a bug.
- **`obj.__dict__`** returns an object's instance-attribute dictionary
  directly, including "private" name-mangled attributes (e.g.
  `_MyClass__name`) — that's the entire trick behind
  `class_to_json()` and `Student.to_json()`: no manual serialization
  code needed, just expose what's already there.
- **`Student.to_json(attrs=...)`** only filters by the optional list if
  it's actually a list of strings; anything else (a dict, a single
  string, `None`) falls back to returning every attribute.
- **`reload_from_json(json)`** uses `setattr()` in a loop over the
  dictionary's items — this is the deserialization half of the same
  round-trip `to_json()` sets up, i.e. an object → dict → JSON file →
  dict → object cycle with no data lost.
- Minor note: a couple of the sample outputs in the task instructions
  (dict key ordering in printed JSON, and the exact `TypeError`/
  `JSONDecodeError` wording) reflect a different Python version than
  the one used to verify these files — the underlying behavior is
  correct either way.

## Author

David-Harold
