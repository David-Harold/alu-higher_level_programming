# SQL_introduction

Introduction to SQL and relational databases: databases, tables,
`SELECT`/`INSERT`/`UPDATE`/`DELETE`, `WHERE`, `ORDER BY`, `GROUP BY`,
and aggregate functions, all in MySQL.

## Description

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases on the MySQL server |
| `1-create_database_if_missing.sql` | Creates the `hbtn_0c_0` database, without failing if it already exists |
| `2-remove_database.sql` | Deletes the `hbtn_0c_0` database, without failing if it doesn't exist |
| `3-list_tables.sql` | Lists all tables of the database passed as an argument to `mysql` |
| `4-first_table.sql` | Creates `first_table (id INT, name VARCHAR(256))`, without failing if it exists |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts `(89, "Best School")` into `first_table` |
| `8-count_89.sql` | Counts the records in `first_table` where `id = 89` |
| `9-full_creation.sql` | Creates `second_table (id, name, score)` and inserts 4 records |
| `10-top_score.sql` | Lists `score, name` from `second_table`, ordered by score (highest first) |
| `11-best_score.sql` | Same as above, filtered to `score >= 10` |
| `12-no_cheating.sql` | Sets Bob's score to `10`, matched by `name` only (not `id`) |
| `13-change_class.sql` | Deletes records from `second_table` where `score <= 5` |
| `14-average.sql` | Computes the average score across `second_table`, aliased as `average` |
| `15-groups.sql` | Counts records per score, aliased as `number`, sorted by count (descending) |
| `16-no_link.sql` | Lists `score, name` from `second_table`, excluding rows with a `NULL` name |

## Requirements

- All scripts run on Ubuntu 20.04 LTS with MySQL 8.0 (or MariaDB
  equivalent), executed as: `cat X-script.sql | mysql -hlocalhost -uroot -p [database]`
- Every file ends with a new line and includes a comment describing
  what it does
- Tasks 1, 2, 4, and 9 avoid `SELECT`/`SHOW` per the task constraints
  (using `IF NOT EXISTS` / `IF EXISTS` instead to make them safe to
  re-run)
- Task 5 avoids `DESCRIBE`/`EXPLAIN`, using `SHOW CREATE TABLE` instead

## Key concepts

- **`IF NOT EXISTS` / `IF EXISTS`** on `CREATE`/`DROP` statements make
  a script idempotent — safe to run multiple times without erroring
  out, which is what "should not fail" means throughout this project.
- **`SHOW CREATE TABLE`** returns a table's full `CREATE TABLE`
  statement (its exact schema), which is how task 5 gets a full
  description without using `DESCRIBE`.
- **`ORDER BY <column> DESC`** sorts descending (highest first);
  omitting `DESC` sorts ascending by default.
- **`GROUP BY`** collapses rows sharing the same value in a column
  (here, `score`) so an aggregate like `COUNT(*)` can be computed per
  group, rather than across the whole table.
- **`AVG()`** and **`COUNT()`** are aggregate functions — they reduce
  a set of rows down to a single computed value (or one value per
  group, when combined with `GROUP BY`).
- Filtering by `name = "Bob"` instead of an `id` (task 12) is a
  reminder that `UPDATE`/`DELETE` can target rows by any column, not
  just a primary key — useful, but risky if the column isn't unique.

## Author

David-Harold
