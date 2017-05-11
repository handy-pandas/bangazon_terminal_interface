import unittest
from unittest.mock import *

import sys; sys.path.append('../')
from bangazon_control import BangazonControl

class TestProduct(unittest.TestCase):

  def test_if_products_exists_in_database(self):
    control = BangazonControl()

    with patch('sqlite3.connect'):
            with patch('sqlite3.connect.cursor'):
                with patch('sqlite3.connect.cursor.fetchall', return_value=[()]):
                    
                    products = control.retrieve_all_products()

                    self.assertIsNotNone(products)
