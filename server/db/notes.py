# import db_utils
from .db_utils import *

# CRUD Operations
def create_note(title, content):
    """
    Creates a note, which has both a title and the text content.
    """
    query = """
    INSERT INTO notes (title, content)
    VALUES (%s, %s)
    """
    exec_commit(query, (title, content,))

def update_note_title(title, new_title):
    """
    Changes title of the note.
    """
    query = """
    UPDATE notes
    SET title=%s
    WHERE title=%s
    """
    exec_commit(query, (new_title, title,))    

def update_note_content(content, new_content):
    """
    Changes the content of the note.
    """
    query = """
    UPDATE notes
    SET content=%s
    WHERE content=%s
    """
    exec_commit(query, (new_content, content,))

def delete_note(title):
    """
    Deletes a note given a title. (Will have to switch to id instead of title, or make title a unique value)
    """
    query = """ 
    DELETE FROM notes
    WHERE title=%s
    """
    exec_commit(query, (title,))

# note-keeper specific functionalities
# def add_note_to_schedule(id, hour_of_day):
#     """
#     Assigns a note to a time of day to be completed.
#     """
#     return id, hour_of_day