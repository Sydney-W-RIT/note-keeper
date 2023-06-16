# import psycopg2
from .db_utils import *

# CRUD Operations
def create_flashcard(term, solution, topic):
    """
    Creates a flashcard, which has both a term and solution and a topic it is associated with.
    """
    query = """
    INSERT INTO flashcards (term, solution, topic)
    VALUES (%s, %s, %s)
    """
    exec_commit(query, (term, solution, topic,))

def update_flashcard_term(term, new_term):
    """
    Changes term of the flashcard.
    """
    query = """
    UPDATE flashcards
    SET term = %s
    WHERE term = %s
    """
    exec_commit(query, (new_term, term,))

# might want to change to given term instead of given solution, since you don't usually identify a flashcard by the solution
def update_flashcard_solution(solution, new_solution):
    """
    Changes the solution of the flashcard.
    """
    query = """
    UPDATE flashcards
    SET solution = %s
    WHERE solution = %s
    """
    exec_commit(query, (new_solution, solution,))

# again, might want to change to given term, especially if term is made a unique identifier
# *DECISION*: either a) add term as a secondary identifier or b) get rid of functionality entirely
# def update_flashcard_topic(topic, new_topic):
#     """
#     Changes the topic associated with the flashcard.
#     """
#     query = """
#     UPDATE flashcards
#     SET topic = %s
#     WHERE topic = %s
#     """
#     exec_commit(query, (new_topic, topic,))

def delete_flashcard(term):
    """
    Deletes a flashcard given a term. (Will have to switch to id instead of term, or make term a unique value)
    """
    query = """
    DELETE FROM flashcards 
    WHERE term = %s
    """
    exec_commit(query, (term,))

# note-keeper specific functionalities
