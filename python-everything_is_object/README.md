# python-everything_is_object

Advanced Python: object identity (`id`), type (`type`), mutability,
aliasing, and how arguments are passed to functions.

## Description

Every task in this project is a short, standalone answer exploring how
CPython represents objects in memory — when two names point to the
*same* object vs. an *equal* object, and what that means for mutable
vs. immutable types.

| File | Question | Answer |
| --- | --- | --- |
| `0-answer.txt` | Function to print an object's type | `type` |
| `1-answer.txt` | Function to get an object's memory address | `id` |
| `2-answer.txt` | `a = 89`, `b = 100` — same object? | `No` |
| `3-answer.txt` | `a = 89`, `b = 89` — same object? | `Yes` |
| `4-answer.txt` | `a = 89`, `b = a` — same object? | `Yes` |
| `5-answer.txt` | `a = 89`, `b = a + 1` — same object? | `No` |
| `6-answer.txt` | `s1 = "Best School"`, `s2 = s1`, `s1 == s2` | `True` |
| `7-answer.txt` | `s1 = "Best"`, `s2 = s1`, `s1 is s2` | `True` |
| `8-answer.txt` | `s1 = "Best School"`, `s2 = "Best School"`, `s1 == s2` | `True` |
| `9-answer.txt` | Same as above, `s1 is s2` (typed line-by-line) | `False` |
| `10-answer.txt` | `l1 = [1,2,3]`, `l2 = [1,2,3]`, `l1 == l2` | `True` |
| `11-answer.txt` | Same as above, `l1 is l2` | `False` |
| `12-answer.txt` | `l1 = [1,2,3]`, `l2 = l1`, `l1 == l2` | `True` |
| `13-answer.txt` | Same as above, `l1 is l2` | `True` |
| `14-answer.txt` | `l2 = l1; l1.append(4); print(l2)` | `[1, 2, 3, 4]` |
| `15-answer.txt` | `l2 = l1; l1 = l1 + [4]; print(l2)` | `[1, 2, 3]` |
| `16-answer.txt` | `n += 1` inside a function, then `print(a)` | `1` |
| `17-answer.txt` | `n.append(4)` inside a function, then `print(l)` | `[1, 2, 3, 4]` |
| `18-answer.txt` | `n = v` (rebinding) inside a function, then `print(l1)` | `[1, 2, 3]` |
| `19-copy_list.py` | Function that returns a copy of a list | `def copy_list(l): return l[:]` |
| `20-answer.txt` | Is `()` a tuple? | `Yes` |
| `21-answer.txt` | Is `(1, 2)` a tuple? | `Yes` |
| `22-answer.txt` | Is `(1)` a tuple? | `No` (it's just `int` `1`) |
| `23-answer.txt` | Is `(1,)` a tuple? | `Yes` |
| `24-answer.txt` | `a = (1)`, `b = (1)`, `a is b` | `True` (both are the cached int `1`) |
| `25-answer.txt` | `a = (1, 2)`, `b = (1, 2)`, `a is b` | `False` |
| `26-answer.txt` | `a = ()`, `b = ()`, `a is b` | `True` (empty tuple is a singleton) |
| `27-answer.txt` | Does `id(a)` stay the same after `a = a + [5]`? | `No` |
| `28-answer.txt` | Does `id(a)` stay the same after `a += [4]`? | `Yes` (in-place extend) |
| `29-blog_post.md` / `29-blog_post_linkedin.md` | Blog post covering the whole project | drafted, pending publish + URLs |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- `19-copy_list.py`: max 3 lines, no imports, no documentation required
- Every `.py` file starts with `#!/usr/bin/python3` and ends with a new line
- Every `.txt` answer file contains only the requested value (no extra text)

## Key concepts

- **`id(obj)`** returns an object's identity (its memory address in
  CPython). **`type(obj)`** returns its class.
- **`==`** compares value; **`is`** compares identity. Two objects can
  be equal without being the same object.
- **Mutable** built-ins (`list`, `dict`, `set`, `bytearray`) can change
  in place — `id()` stays constant while contents change.
- **Immutable** built-ins (`int`, `float`, `complex`, `str`, `tuple`,
  `frozenset`, `bytes`) can never change after creation; anything that
  looks like a mutation creates a new object instead.
- CPython caches small integers from **-5 to 256** at startup
  (`NSMALLNEGINTS` / `NSMALLPOSINTS`), so equal small ints are often
  the same object (`3-answer.txt`, `24-answer.txt`).
- The empty tuple `()` is a singleton in CPython, so all empty tuples
  share one object (`26-answer.txt`).
- `l1 = l1 + [4]` builds a new list; `l1 += [4]` (or `.append()`)
  mutates in place — hence the different answers for `15` vs. `28`.
- Function arguments are passed by object reference: mutating a
  mutable argument is visible to the caller; rebinding a parameter
  name never is (`16`, `17`, `18`).

## Author

David-Harold
