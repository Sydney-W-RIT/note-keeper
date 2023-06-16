from server.db import notes
from server.db import db_utils
import unittest

class Test_Notes(unittest.TestCase):
    def setUp(self):
        db_utils.exec_sql_file("sql/drop.sql")
        db_utils.exec_sql_file("sql/create.sql")
        db_utils.exec_sql_file("sql/seed.sql")

    def test_create_note(self):
        notes.create_note("To Do 6/15", "Physics Homework")
        query = """
        SELECT content
        FROM notes
        WHERE title=%s
        """
        expected = "Physics Homework"
        actual = db_utils.exec_get_one(query, ("To Do 6/15",))[0]
        self.assertEqual(actual, expected)

    def test_update_note_title(self):
        notes.update_note_title("Homework", "Homework 6/15")
        query = """
        SELECT title 
        FROM notes
        WHERE content=%s
        """
        expected = "Homework 6/15"
        actual = db_utils.exec_get_one(query, ("Physics, Web Engineering",))[0]
        self.assertEqual(actual, expected)

    def test_update_note_content(self):
        notes.update_note_content("Take cat for a walk", "Take duck for a walk")
        query = """
        SELECT content
        FROM notes
        WHERE title=%s
        """
        expected = "Take duck for a walk"
        actual = db_utils.exec_get_one(query, ("To Do",))[0]
        self.assertEqual(actual, expected)

    def test_delete_note(self):
        notes.delete_note("To Do")
        query = """
        SELECT content
        FROM notes
        WHERE title=%s
        """
        expected = None
        actual = db_utils.exec_get_one(query, ("To Do",))
        self.assertEqual(expected, actual)