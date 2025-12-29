GET_ALL_TODOS_SQL_QUERY:str = """SELECT * FROM todos"""
CREATE_TODOS_SQL_QUERY:str = """
INSERT INTO todos (title, description, due_date, status) VALUES (?, ?, ?, ?)
"""

CREATE_TODOS_TABLE_SQL_QUERY: str = """
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    deleted_at TEXT
);
"""


GET_TODO_BY_ID_SQL_QUERY:str = """
SELECT
    id,
    title,
    description,
    due_date,
    status,
    created_at,
    updated_at
FROM todos
WHERE id = ?;
"""

UPDATE_TODO_SQL_QUERY:str = """
UPDATE todos
SET
    title = ?,
    description = ?,
    due_date = ?,
    status = ?,
    updated_at = CURRENT_TIMESTAMP
WHERE id = ?;
"""


DELETE_TODO_SQL_QUERY:str = """
DELETE FROM todos
WHERE id = ?;
"""