import unittest
from backend.internal_utils import *
from backend.db_entry import *

class TestDBEntry(unittest.TestCase):

    def test_get_db(self):
        self.assertIsNotNone(get_db())

class TestInternalUtils(unittest.TestCase):

    def test_user_can_purchase(self):
        uid = get_all_elements()['727bd015fc214a4b']['user_ids'][2]
        rid = get_all_elements()['727bd015fc214a4b']['reward_ids'][0]
        self.assertTrue(can_user_claim_reward(uid, rid))
