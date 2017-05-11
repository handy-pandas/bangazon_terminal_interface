import unittest
from unittest.mock import *

import sys; sys.path.append('../')
from src.payment_type import PaymentType
from src.customer import Customer
from bangazon_control import BangazonControl


class TestCustomerClass(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.control = BangazonControl()

  def test_query_retrieve_all_customers(self):
    with patch('sqlite3.connect'):
      with patch('sqlite3.connect.cursor'):
        with patch('sqlite3.connect.cursor.fetchall', return_value=[()]):

          customers = self.control.retrieve_all_customers()

          self.assertIsNotNone(customers)  

############ Example #############
"""
def test_existing_name():
    with patch('what.sqlite3') as mocksql:
        mocksql.connect().cursor().fetchall.return_value = ['John', 'Bob']

  with patch('micro.plus', side_effect=ValueError('Does not Work')):

  with patch('micro.plus', return_value=4):
"""
##################################



  # def test_if_customer_is_active(self):    
  #   self.control.save_all_customers()
  #   self.control.set_active_customer(1)    

  #   self.assertEqual(self.control.active_customer, 1)

  # def test_if_customer_can_be_created_in_database(self):    
  #   new_customer = self.control.create_customer(name='Nick Nash', address='123 Dumb Ave', city='StupidVille', state='Dumb Town', postal_code='12345-1234')
  #   self.control.add_customer_to_database(new_customer)
  #   retrieved_customer = self.control.retrieve_customer_from_database_by_all_attributes(new_customer)

  #   self.assertEqual(retrieved_customer['name'], new_customer['name'])
  #   self.assertEqual(retrieved_customer['address'], new_customer['address'])
  #   self.assertEqual(retrieved_customer['city'], new_customer['city'])
  #   self.assertEqual(retrieved_customer['state'], new_customer['state'])
  #   self.assertEqual(retrieved_customer['postal_code'], new_customer['postal_code'])






