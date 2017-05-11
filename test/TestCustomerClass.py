import unittest
from unittest.mock import *

import sys; sys.path.append('../')
from bangazon_control import BangazonControl


class TestCustomerClass(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.control = BangazonControl()

  def test_query_retrieve_all_customers(self):
    with patch('sqlite3.connect'):
      with patch('sqlite3.connect.cursor'):
        with patch('sqlite3.connect.cursor.fetchall', return_value=['Nick Nash']):

          customers = self.control.retrieve_all_customers()

          self.assertIsNotNone(customers)  

  def test_if_customer_can_be_constructed_as_dictionary(self):    
    new_customer = self.control.create_customer(name='Nick Nash', address='123 Dumb Ave', city='StupidVille', state='Dumb Town', postal_code='12345-1234', phone_number='123451234')

    self.assertEqual(new_customer['name'], 'Nick Nash')
    self.assertEqual(new_customer['address'], '123 Dumb Ave')
    self.assertEqual(new_customer['city'], 'StupidVille')
    self.assertEqual(new_customer['state'], 'Dumb Town')
    self.assertEqual(new_customer['postal_code'], '12345-1234')
    self.assertEqual(new_customer['phone_number'], '123451234')







