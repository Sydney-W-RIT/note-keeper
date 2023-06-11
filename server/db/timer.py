# import db_utils

# CRUD Operations
# timer is a pretty unchanging entity as well, will update however

# note-keeper specific functionalities
def start_session():
    """
    Sets start_time equal to CURRENT_TIMESTAMP or NOW(), and sets work_session to true. 
    If work_session is true the timer interval will be 25 minutes, and if it is false and therefore a break it will be 5 minutes,
    following the traditional Pomodoro study method. 
    """
    return None

def end_session():
    """
    Start time is 0 as the timer is not in use, work_session set to true as the next time the user uses the timer it will be to begin
    a Pomodoro work session.
    """
    return None