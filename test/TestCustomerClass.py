
import unittest

import sys; sys.path.append('../')
from src.payment_type import PaymentType
from src.customer import Customer
from bangazon_control import BangazonControl


class TestCustomerClass(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.control = BangazonControl()
    self.customer_management = Customer()    

  def test_query_retrieve_all_customers(self):
    customers = self.customer_management.retrieve_all_customers()

    self.assertIsNotNone(customers)  

  def test_if_customer_is_active(self):    
    self.control.save_all_customers()
    self.control.set_active_customer(1)    

    self.assertEqual(self.control.active_customer, 1)

  def test_if_customer_can_be_created_in_database(self):    
    new_customer = self.control.create_customer(name='Nick Nash', address='123 Dumb Ave', city='StupidVille', state='Dumb Town', postal_code='12345-1234')
    self.customer_management.add_customer_to_database(new_customer)
    retrieved_customer = self.customer_management.retrieve_customer_from_database_by_all_attributes(new_customer)

    self.assertEqual(retrieved_customer['name'], new_customer['name'])
    self.assertEqual(retrieved_customer['address'], new_customer['address'])
    self.assertEqual(retrieved_customer['city'], new_customer['city'])
    self.assertEqual(retrieved_customer['state'], new_customer['state'])
    self.assertEqual(retrieved_customer['postal_code'], new_customer['postal_code'])






