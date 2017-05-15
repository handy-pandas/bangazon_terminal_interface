import unittest
from unittest.mock import patch

import sys; sys.path.append('../')
from bangazon_control import BangazonControl


class TestViewContentsOfOrder(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.control = BangazonControl()

    def test_can_view_contents_of_current_order(self):

        with patch('sqlite3.connect'):
            with patch('sqlite3.connect.cursor'):
                with patch('sqlite3.connect.cursor.fetchall', return_value=[(1, )]):
                    current_products = self.control.retrieve_all_products()
                    product_seller_id = current_products[0][3]

                    self.assertIsNotNone(product_seller_id)

