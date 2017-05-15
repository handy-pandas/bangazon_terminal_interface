import unittest
from unittest.mock import patch

import sys; sys.path.append('../')
from bangazon_control import BangazonControl


class TestViewContentsOfOrder(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.control = BangazonControl()

    def test_can_view_contents_of_current_order(self):
        self.control.active_order_pk = 1
        with patch('sqlite3.connect'):
            with patch('sqlite3.connect.cursor'):
                with patch('sqlite3.connect.cursor.fetchall', return_value=[(1, 'Apples'),(2, 'Cheap Joke')]):
                    current_products_on_order = self.control.retrieve_customers_current_order()

                    self.assertIsNotNone(current_products_on_order)

