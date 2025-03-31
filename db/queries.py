CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        task TEXT NOT NULL,
        created_at TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    );
"""

SELECT_TASKS = """
    SELECT id, title, task, created_at, completed FROM tasks;
"""

INSERT_TASK = """
    INSERT INTO tasks (title, task, created_at, completed) VALUES (?, ?, ?, 0);
"""

UPDATE_TASK = """
    UPDATE tasks SET title = ?, task = ? WHERE id = ?;
"""

DELETE_TASK = """
    DELETE FROM tasks WHERE id = ?;
"""

SELECT_ALL = """
    SELECT id, task, completed FROM tasks;
"""

SELECT_COMPLETED = """
    SELECT id, task, completed FROM tasks WHERE completed = 2;
"""

SELECT_IN_WORK = """
    SELECT id, task, completed FROM tasks WHERE completed = 1;
"""

SELECT_INCOMPLETE = """
    SELECT id, task, completed FROM tasks WHERE completed = 0;
"""

UPDATE_STATUS = """
    UPDATE tasks SET completed = ? WHERE id = ?;
"""

DELETE_COMPLETED = """
    DELETE FROM tasks WHERE completed = 2;
"""