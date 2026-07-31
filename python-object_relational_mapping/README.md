# python-object_relational_mapping

Connecting Python to MySQL two ways: raw SQL with `MySQLdb`, then the
same operations with zero SQL via the `SQLAlchemy` ORM.

## Description

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all `states`, raw `MySQLdb` |
| `1-filter_states.py` | Lists `states` starting with `N` |
| `2-my_filter_states.py` | Filters `states` by name via `str.format` — intentionally SQL-injectable, see task 3 |
| `3-my_safe_filter_states.py` | Same as above, but parameterized (injection-safe) |
| `4-cities_by_state.py` | Lists all `cities` with their state, one `JOIN` query |
| `5-filter_cities.py` | Lists city names for a given state, injection-safe |
| `model_state.py` | `State` model + shared `Base = declarative_base()` |
| `7-model_state_fetch_all.py` | Lists all `State` objects, via SQLAlchemy |
| `8-model_state_fetch_first.py` | Prints the first `State`, or `Nothing` |
| `9-model_state_filter_a.py` | Lists `State`s containing `a` |
| `10-model_state_my_get.py` | Prints a `State`'s id by name, or `Not found` |
| `11-model_state_insert.py` | Adds `State("Louisiana")`, prints new id |
| `12-model_state_update_id_2.py` | Renames the `State` with `id=2` |
| `13-model_state_delete_a.py` | Deletes every `State` containing `a` |
| `model_city.py` | `City` model (`id`, `name`, `state_id` FK to `states.id`) |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects with their state name |

## Requirements

- Ubuntu 20.04 LTS, Python 3 (3.8.5), `MySQLdb` 2.0.x, `SQLAlchemy` 1.4.x
- Code follows `pycodestyle` (2.7.\*)
- Every file starts with `#!/usr/bin/python3`, ends with a new line,
  and is executable
- Every module, class, and function has a real documentation sentence
- No script executes its logic on import (`if __name__ == "__main__"`)
- SQLAlchemy scripts never call `.execute()` directly — only ORM
  query methods

## Key concepts

- **`MySQLdb` vs `SQLAlchemy`**: tasks 0-5 write and send SQL strings
  by hand; tasks 7-14 never write SQL at all — `session.query(State)`
  replaces `SELECT * FROM states`, and SQLAlchemy generates the SQL
  underneath.
- **SQL injection, demonstrated live**: task 2 builds its query with
  `str.format`, so `Arizona'; TRUNCATE TABLE states ; SELECT * FROM
  states WHERE name = '` as input truncates the whole table. Task 3
  fixes it by passing values as a parameter tuple to `execute()`
  instead of interpolating them into the query string — `MySQLdb`
  escapes them properly.
- **One query only** (tasks 4 and 5): rather than looping and
  querying per-city for its state name, a single `JOIN` pulls both
  tables' data in one round trip.
- **Declarative models**: `State` and `City` both inherit from the
  same `Base = declarative_base()` defined once in `model_state.py`
  and imported everywhere else — `Base.metadata.create_all(engine)`
  only creates tables for classes that have actually been imported
  first, which is why every ORM script explicitly imports both
  `Base` and `State` (and `City`, for task 14) before calling it.
- **Foreign keys as plain columns**: `City.state_id` is declared with
  `ForeignKey("states.id")`, but no relationship attribute was added
  since the task only asks for the three raw columns — task 14 joins
  `City` and `State` directly in the query (`session.query(City,
  State.name).join(...)`) instead of using an ORM relationship.

## Author

David-Harold
