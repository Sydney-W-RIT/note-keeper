# import db_utils

# CRUD Operations
def create_note(title, content):
    """
    Creates a note, which has both a title and the text content.
    """
    return title, content

def update_note_title(title):
    """
    Changes title of the note.
    """
    return title

def update_note_content(content):
    """
    Changes the content of the note.
    """
    return content

def delete_note(title):
    """
    Deletes a note given a title. (Will have to switch to id instead of title, or make title a unique value)
    """
    return title

# note-keeper specific functionalities
def add_note_to_schedule(id, hour_of_day):
    """
    Assigns a note to a time of day to be completed.
    """
    return id, hour_of_day