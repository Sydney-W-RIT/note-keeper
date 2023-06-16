from server.db import flashcards
from server.db import db_utils
# from db_utils import exec_sql_file
import unittest

class Test_Flashcards(unittest.TestCase):
    def setUp(self):
        db_utils.exec_sql_file("sql/drop.sql")
        db_utils.exec_sql_file("sql/create.sql")
        db_utils.exec_sql_file("sql/seed.sql")

    def test_create_flashcard(self):
        flashcards.create_flashcard("Algorithm", "Process, Set of rules followed in problem-solving operation", "Computer Science")
        # self suggestion: perhaps use boolean and try/catch for creating to test more thoroughly
        expected = "Process, Set of rules followed in problem-solving operation"
        query = """
        SELECT solution 
        FROM flashcards
        WHERE term=%s
        """
        actual = db_utils.exec_get_one(query, ("Algorithm",))[0]
        self.assertEqual(actual, expected)

    def test_update_flashcard_term(self):
        flashcards.update_flashcard_term("Aglet", "aksdjbchak") # perhaps make this a bit more prim and proper
        query = """
        SELECT term
        FROM flashcards
        WHERE solution=%s
        """
        expected = "aksdjbchak"
        actual = db_utils.exec_get_one(query, ("Plastic at the end of a shoelace",))[0]
        self.assertEqual(actual, expected)

    def test_update_flashcard_solution(self):
        flashcards.update_flashcard_solution("Powerhouse of the cell", "Organelle")
        query = """
        SELECT solution
        FROM flashcards
        WHERE term=%s
        """
        expected = "Organelle"
        actual = db_utils.exec_get_one(query, ("Mitochondria",))[0]
        self.assertEqual(actual, expected)

    # IMPORTANT: update topic will *likely* need a secondary identifier, since you'll likely not want to change the topic for all cards of a topic
    # def test_update_flashcard_topic(self):
    #     flashcards.update_flashcard_topic("Computer Science", "Software Engineering")
    #     query = """
    #     SELECT term
    #     FROM flashcards
    #     WHERE topic=%s 
    #     """
    #     expected = "Software Engineering"
    #     actual = db_utils.exec_get_one(query, ("Computer Science",))
    #     self.assertEqual(actual, expected)

    def test_delete_flashcard(self):
        flashcards.delete_flashcard("Mitochondria")
        query = """
        SELECT solution
        FROM flashcards
        WHERE term=%s
        """
        expected = None
        actual = db_utils.exec_get_one(query, ("Mitochondria",))
        self.assertEqual(actual, expected)