# import db_utils

# CRUD Operations
def create_flashcard(term, solution, topic):
    """
    Creates a flashcard, which has both a term and solution and a topic it is associated with.
    """
    return term, solution, topic

def update_flashcard_term(term):
    """
    Changes term of the flashcard.
    """
    return term

def update_flashcard_solution(solution):
    """
    Changes the solution of the flashcard.
    """
    return solution

def update_flashcard_topic(topic):
    """
    Changes the topic associated with the flashcard.
    """
    return topic

def delete_flashcard(term):
    """
    Deletes a flashcard given a term. (Will have to switch to id instead of term, or make term a unique value)
    """
    return term

# note-keeper specific functionalities
