import unittest
from unittest.mock import patch

import sys; sys.path.append('../')
from bangazon_control import BangazonControl


class TestViewContentsOfOrder(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.control = BangazonControl()

    def test_can_add_product_from_customer(self):

        with patch('sqlite3.connect'):
            with patch('sqlite3.connect.cursor'):
                with patch('sqlite3.connect.cursor.execute'):

                    product = { 'title': 'Balloons', 'price': 0.99, 'seller_id': 1}
                    self.control.add_product(product)


                with patch('sqlite3.connect.cursor.fetchall', return_value=[(1, 'Apples', 0.99, 1)]):

                    products = self.control.retrieve_all_products()
                    product_seller_id = products[0][3]

                    self.assertIsNotNone(product_seller_id)
