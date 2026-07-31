# python-test_driven_development

Advanced Python: writing functions the TDD way — docstrings and
doctests first, then a matching unittest suite, with strict input
validation throughout.

## Description

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two ints/floats (cast to int); `tests/0-add_integer.txt` |
| `2-matrix_divided.py` | Divides all elements of a matrix by `div`, rounded to 2 decimals; `tests/2-matrix_divided.txt` |
| `3-say_my_name.py` | Prints `My name is <first> <last>`; `tests/3-say_my_name.txt` |
| `4-print_square.py` | Prints a square of `#`; `tests/4-print_square.txt` |
| `5-text_indentation.py` | Prints text with 2 new lines after `.`, `?` and `:`; `tests/5-text_indentation.txt` |
| `6-max_integer.py` | Returns the max of a list (or `None` if empty); `tests/6-max_integer_test.py` |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line
- Every module, class, and function has a docstring
- Tasks 0-5 are tested with `doctest` (`tests/*.txt`); task 5's
  `max_integer` is tested with `unittest`
  (`python3 -m unittest tests.6-max_integer_test`)

## Key concepts

- **Doctests as documentation** — the `>>>` examples in a `.txt` file
  under `tests/` double as both the spec and the test: run them with
  `python3 -m doctest -v tests/X-file.txt`.
- **Strict type checking with `isinstance`** — every function raises
  a specific `TypeError` (or `ValueError`) with an exact message when
  given the wrong type, rather than failing with a generic Python
  error later.
- **`matrix_divided`** never mutates the input matrix — it always
  builds and returns a new one via nested list comprehension.
- **`text_indentation`** has a subtle edge case: the very last
  sentence, if it doesn't end in `.`, `?`, or `:`, is printed with
  *no* trailing newline — matching the exact byte output of the
  reference solution (verified against the sample in this repo).
- **`unittest` vs `doctest`** — task 5 (`max_integer`) is the one
  exception in this project: it's tested with Python's `unittest`
  module instead of `doctest`, run as
  `python3 -m unittest tests.6-max_integer_test`.

## Author

David-Harold
