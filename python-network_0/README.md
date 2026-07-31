# python-network_0

Introduction to HTTP and `curl`: methods, status codes, headers, and
request bodies, all driven from Bash scripts.

## Description

| File | Description |
| --- | --- |
| `0-body_size.sh` | Sends a request to a URL, prints the size (in bytes) of the response body |
| `1-body.sh` | Sends a `GET` request, prints the response body only if the status code is `200` |
| `2-delete.sh` | Sends a `DELETE` request, prints the response body |
| `3-methods.sh` | Sends an `OPTIONS` request, prints the list of HTTP methods the server accepts |
| `4-header.sh` | Sends a `GET` request with the header `X-HolbertonSchool-User-Id: 98`, prints the response body |
| `5-post_params.sh` | Sends a `POST` request with `email=test@gmail.com` and `subject=I will always be here for PLD`, prints the response body |

## Requirements

- Ubuntu 20.04 LTS, Bash
- All scripts use `curl`
- Every file starts with `#!/bin/bash`, ends with a new line, and is
  executable (`chmod +x *.sh`)
- Test against the web server running on port 5000 in the provided
  container, e.g. `./0-body_size.sh 0.0.0.0:5000`

## Key concepts

- **`curl -w`** (the `--write-out` flag) lets you extract metadata
  about a response — like `%{size_download}` (body size in bytes) or
  `%{http_code}` (status code) — without parsing the raw output
  yourself. That's the entire mechanism behind `0-body_size.sh`.
- **Status-code gating** (task 1): the response body and its status
  code arrive together in one `curl` call (`-w "\n%{http_code}"`
  appended to the body), then get split apart in the script — only
  printing the body when the trailing status line reads `200`.
- **`-X <METHOD>`** overrides the HTTP method `curl` uses (`DELETE` in
  task 2); without it, `curl` defaults to `GET`, or `POST`
  automatically once you pass `-d`.
- **`-D -`** dumps the response headers to stdout (`-` means "print
  headers to standard output" instead of a file), which is how task 3
  reads the `Allow` header returned by an `OPTIONS` request to learn
  which methods a route supports.
- **`-H "Header: value"`** attaches a custom request header (task 4);
  **`-d "key=value"`** (repeated) attaches URL-encoded form fields to
  a `POST` body (task 5) — `curl` switches to `POST` automatically as
  soon as `-d` is present, so no explicit `-X POST` is required
  (though it doesn't hurt to be explicit).

## Author

David-Harold
