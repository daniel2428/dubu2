import sqlite3
from config import DB_PATH
from db import queries


def init_db():
    """
    Initialize the database and create the necessary tables if they do not exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the tasks table
    cursor.execute(queries.CREATE_TASKS_TABLE)

    # Create the categories table
    cursor.execute(queries.CREATE_CATEGORIES_TABLE)

    # Create the tags table
    cursor.execute(queries.CREATE_TAGS_TABLE)

    # Create the task_tags table
    cursor.execute(queries.CREATE_TASK_TAGS_TABLE)

    conn.commit()
    conn.close()


def get_tasks():
    """
    Retrieve all tasks from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(queries.SELECT_TASKS)
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def add_task_db(task):
    """
    Add a new task to the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(queries.INSERT_TASK, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def update_task_db(task_id, new_task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()
    

def delete_task_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()


