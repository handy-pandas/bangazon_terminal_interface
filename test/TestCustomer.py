import unittest

import sys; sys.path.append('../')
from src.customer import Customer
from bangazon_control import BangazonControl


class TestCustomer(unittest.TestCase):

    def test_if_customer_can_be_created_in_database(self):
        customer_management = Customer()
        control = BangazonControl()
        new_customer = control.create_customer(name='Nick Nash', address='123 Dumb Ave', city='StupidVille', state='Dumb Town', postal_code='12345-1234')
        customer_management.add_customer_to_database(new_customer)
        retrieved_customer = customer_management.retrieve_customer_from_database_by_all_attributes(new_customer)

        self.assertEqual(retrieved_customer['name'], new_customer['name'])
        self.assertEqual(retrieved_customer['address'], new_customer['address'])
        self.assertEqual(retrieved_customer['city'], new_customer['city'])
        self.assertEqual(retrieved_customer['state'], new_customer['state'])
        self.assertEqual(retrieved_customer['postal_code'], new_customer['postal_code'])




