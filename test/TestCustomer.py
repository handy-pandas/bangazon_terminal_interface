import unittest

import sys; sys.path.append('../')
from src.customer import Customer
from bangazon_control import *

class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        customer_management = Customer()

    def test_if_customer_can_be_created_in_database(self):
        new_customer = customer_management.create_customer(name='Nick Nash', address='123 Dumb Ave', city='StupidVille', state='Dumb Town', postal_code='12345-1234')
        customer_management.add_customer_to_db(new_customer)
        retrieved_customer = customer_management.retreive_customer_from_database_by_name('Nick Nash')

        self.assertEqual(new_customer, { name: 'Nick Nash', address: '123 Dumb Ave', city: 'StupidVille', state: 'Dumb Town', postal_code: '12345-1234' })
        self.assertEqual(retrieved_customer.name, new_customer.name)




