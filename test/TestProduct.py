import unittest

import sys; sys.path.append('../')
from src.product import Product

class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.ball = Product(title='Basketball', price='9.89')

    def test_product_has_a_title(self):
        self.assertEqual(self.ball.title, 'Basketball')

    def test_product_has_a_price(self):
        self.assertEqual(self.ball.price, '9.89')

    def test_if_product_exists_in_database(self):
        self.assertIsNotNone(self.ball.id)

