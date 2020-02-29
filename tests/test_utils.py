import unittest
from backend.internal_utils import *
from backend.db_entry import *

class TestDBEntry(unittest.TestCase):

    def test_get_db(self):
        self.assertIsNotNone(get_db())
#
# class TestInternalUtils(unittest.TestCase):
#
#     def test_

