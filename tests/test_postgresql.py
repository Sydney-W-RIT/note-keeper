import unittest
from server.db import db_utils


class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        result = db_utils.exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))


if __name__ == '__main__':
    unittest.main()