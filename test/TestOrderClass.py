import unittest
from unittest.mock import *

import sys; sys.path.append('../')
from bangazon_control import BangazonControl


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.control = BangazonControl()      

    def test_if_active_order_can_be_created_in_database(self):            
        with patch('sqlite3.connect'):
            with patch('sqlite3.connect.cursor'):
                with patch('sqlite3.connect.cursor.fetchall', return_value=[()]):
                    active_order_pk = self.control.make_order_active(1)

                    self.assertIsNotNone(active_order_pk)









