import unittest

import sys; sys.path.append('../')
from src.product import Product

class TestProduct(unittest.TestCase):

  def test_if_products_exists_in_database(self):
    product = Product()
    products = product.retrieve_all_products()

    self.assertIsNotNone(products)
