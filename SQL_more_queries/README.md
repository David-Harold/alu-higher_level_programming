# SQL_more_queries

More SQL: users and privileges, column constraints (`NOT NULL`,
`DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`), subqueries, and
`JOIN`s (`INNER`, `LEFT`) across two schemas: `hbtn_0d_usa`
(states/cities) and `hbtn_0d_tvshows` (shows/genres).

## Description

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of `user_0d_1` and `user_0d_2` (`SHOW GRANTS`) |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges, password `user_0d_1_pwd` |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and `user_0d_2` with `SELECT`-only access to it |
| `3-force_name.sql` | Creates `force_name (id INT, name VARCHAR(256) NOT NULL)` |
| `4-never_empty.sql` | Creates `id_not_null (id INT DEFAULT 1, name VARCHAR(256))` |
| `5-unique_id.sql` | Creates `unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256))` |
| `6-states.sql` | Creates `hbtn_0d_usa` and `states (id ... PRIMARY KEY, name NOT NULL)` |
| `7-cities.sql` | Creates `cities`, with `state_id` as a `FOREIGN KEY` to `states.id` |
| `8-cities_of_california_subquery.sql` | Cities in California, via a subquery (no `JOIN` allowed) |
| `9-cities_by_state_join.sql` | All cities with their state name, via `JOIN` |
| `10-genre_id_by_show.sql` | Shows with at least one genre (`INNER JOIN`) |
| `11-genre_id_all_shows.sql` | All shows, `NULL` genre if none (`LEFT JOIN`) |
| `12-no_genre.sql` | Only shows with no genre linked |
| `13-count_shows_by_genre.sql` | Show count per genre, as `genre`/`number_of_shows`, sorted descending |
| `14-my_genres.sql` | All genres of the show "Dexter" |
| `15-comedy_only.sql` | All shows tagged "Comedy" |
| `16-shows_by_genre.sql` | Every show with every linked genre (or `NULL`), via `LEFT JOIN` |

## Requirements

- All scripts run on Ubuntu 20.04 LTS with MySQL 8.0 (or MariaDB
  equivalent): `cat X-script.sql | mysql -hlocalhost -uroot -p [database]`
- Every file ends with a new line and starts with a comment
  describing what it does; SQL keywords are uppercase
- `CREATE USER`/`CREATE DATABASE`/`CREATE TABLE` all use
  `IF NOT EXISTS` so scripts can be re-run safely
- Tasks 10-16 require importing the `hbtn_0d_tvshows` dump first:
  ```bash
  curl -o hbtn_0d_tvshows.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"
  mysql -hlocalhost -uroot -p < hbtn_0d_tvshows.sql
  ```

## Key concepts

- **`GRANT`/`SHOW GRANTS`** manage and inspect what a MySQL user can
  do; privileges can be scoped to `*.*` (everything), `db.*` (one
  database), or `db.table` (one table).
- **`NOT NULL`** forbids empty values outright; **`DEFAULT`** instead
  supplies a fallback value when none is given (so the column is never
  truly empty, but inserts without it still succeed) — that's the
  difference between `force_name` (task 3, hard requirement) and
  `id_not_null` (task 4, soft fallback).
- **`UNIQUE`** rejects duplicate values; **`PRIMARY KEY`** implies both
  `NOT NULL` and `UNIQUE`, plus marks the column as the table's main
  identifier — `AUTO_INCREMENT` is what makes `states.id` and
  `cities.id` fill themselves in.
- **`FOREIGN KEY ... REFERENCES`** ties `cities.state_id` to
  `states.id`, so MySQL rejects any city insert whose `state_id`
  doesn't correspond to a real state (referential integrity).
- **Subquery vs. `JOIN`**: task 8 filters `cities` using a subquery
  (`WHERE state_id = (SELECT id FROM states WHERE name = "California")`)
  because `JOIN` is disallowed there; task 9 does the equivalent with
  a `JOIN`, which is generally more efficient and is what's used
  everywhere else in this project.
- **`INNER JOIN` vs. `LEFT JOIN`**: `INNER JOIN` only keeps rows that
  match on both sides (used when a show *must* have a genre, e.g. task
  10), while `LEFT JOIN` keeps every row from the left table
  regardless of a match, filling in `NULL` where there's none (used
  when shows without a genre still need to show up, e.g. tasks 11, 16).
- **`GROUP BY` + `COUNT()`** (task 13) collapses rows per genre to
  count linked shows, and excluding un-linked genres happens
  automatically since `INNER JOIN` drops any genre with zero matches.

## Author

David-Harold
