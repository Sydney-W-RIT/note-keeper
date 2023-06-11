# import db_utils

# CRUD Operations
# schedule is a pretty unchanging entity, will always have hours 1-24 etc

# note-keeper specific functionalities
def add_to_schedule(id, hour_of_day):
    """
    Adds note with corresponding id to the daily schedule at the time hour_of_day.
    """
    return id, hour_of_day