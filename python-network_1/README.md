# python-network_1

Advanced Python: HTTP requests from Python itself, first with the
standard-library `urllib`, then with the third-party `requests`
library — GET/POST, headers, error handling, JSON, and Basic Auth.

## Description

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches `/status` with `urllib`, prints type/content/utf8 content of the body |
| `1-hbtn_header.py` | Prints the `X-Request-Id` response header for a URL, using `urllib` |
| `2-post_email.py` | `POST`s an `email` parameter to a URL, using `urllib`, prints the body |
| `3-error_code.py` | Fetches a URL with `urllib`, prints the body or `Error code: <code>` on `HTTPError` |
| `4-hbtn_status.py` | Same as task 0, using `requests` instead |
| `5-hbtn_header.py` | Same as task 1, using `requests` instead |
| `6-post_email.py` | Same as task 2, using `requests` instead |
| `7-error_code.py` | Same as task 3, using `requests` (checks `status_code >= 400` instead of catching an exception) |
| `8-json_api.py` | `POST`s a letter (`q`) to `/search_user`, prints `[<id>] <name>`, `Not a valid JSON`, or `No result` |
| `10-my_github.py` | Prints a GitHub user's `id` via Basic Auth against the GitHub API |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.4.3+)
- Code follows `pycodestyle` (2.5.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line,
  and is executable (`chmod +x *.py`)
- Tasks 0-3 import only `urllib` (and its submodules) plus `sys`
  where needed; tasks 4-8 and 10 import only `requests` and `sys`
- Tasks 0-3 use a `with` statement around `urllib.request.urlopen(...)`

## Key concepts

- **`urllib.request.urlopen()`** returns a response object usable as a
  context manager (`with ... as response:`), which is why tasks 0-3
  specifically require `with` — it's the standard-library way to
  guarantee the connection gets closed.
- **`requests`** wraps the same underlying work in a much higher-level
  API: `requests.get()`/`requests.post()` return a `Response` object
  directly, no context manager needed, with `.text`, `.json()`, and
  `.headers` doing the decoding/parsing for you — tasks 4-8 and 10
  show the same operations as 0-3, dramatically shorter.
- **Error handling differs by library**: `urllib` raises
  `urllib.error.HTTPError` on 4xx/5xx responses, which you have to
  catch (task 3); `requests` never raises on its own for a bad status
  code — you have to check `response.status_code` explicitly (task 7).
  Same requirement, two different underlying philosophies.
- **`response.json()`** (task 8) parses the body as JSON and raises
  `ValueError` (specifically `json.JSONDecodeError`, a subclass) if
  the body isn't valid JSON — that's the exact exception task 8 is
  built around catching to print `Not a valid JSON`.
- **Basic Authentication** (task 10) is passed to `requests` as a
  tuple: `auth=(username, password)`. GitHub no longer accepts a real
  account password there — you need a personal access token (scoped
  to at least `read:user`) generated from GitHub's developer settings,
  used in place of the password.

## Author

David-Harold
