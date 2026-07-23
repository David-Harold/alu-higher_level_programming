#!/usr/bin/env bash

cat << 'EOF' > "0-safe_print_list.py"
#!/usr/bin/python3
"""Prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list on one line.

    Returns the actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
EOF

cat << 'EOF' > "1-safe_print_integer.py"
#!/usr/bin/python3
"""Safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer if possible.

    Returns True if value was an integer and got printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
EOF

cat << 'EOF' > "2-safe_print_list_integers.py"
#!/usr/bin/python3
"""Prints the first x elements of a list, integers only."""


def safe_print_list_integers(my_list=[], x=0):
    """Print only the integer elements among the first x of my_list.

    Non-integer elements are skipped silently.
    If x is bigger than the list, an IndexError is allowed to propagate.
    Returns the number of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
EOF

cat << 'EOF' > "3-safe_print_division.py"
#!/usr/bin/python3
"""Divides two integers safely."""


def safe_print_division(a, b):
    """Divide a by b, printing debug info in the finally clause.

    Returns the division result, or None if division by zero occurred.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
EOF

cat << 'EOF' > "4-list_division.py"
#!/usr/bin/python3
"""Divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a new list of length list_length with element-wise divisions.

    Any element that can't be divided becomes 0, with an explanatory
    message printed: "wrong type", "division by 0", or "out of range".
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
EOF

cat << 'EOF' > "5-raise_exception.py"
#!/usr/bin/python3
"""Raises a type exception."""


def raise_exception():
    """Raise a TypeError."""
    raise TypeError()
EOF

cat << 'EOF' > "6-raise_exception_msg.py"
#!/usr/bin/python3
"""Raises a name exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError with the given message."""
    raise NameError(message)
EOF

cat << 'EOF' > "README.md"
Non empty README file
EOF

