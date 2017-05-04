import unittest

import sys; sys.path.append('../')
from src.customer import Customer

class TestCustomer(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.taylor = Customer(name="Taylor Unicorn", street_address="Nashville", city="1st Avenue", state="Nick", postal_code="12345-67894", phone_number="615-999-9999")
    self.taylor.save()

  def test_customer_has_name(self):
    self.assertEqual(self.taylor.name, 'Taylor Unicorn')

  def test_customer_has_street_address(self):
    self.assertEqual(self.taylor.street_address, 'Nashville')

  def test_customer_has_city(self):
    self.assertEqual(self.taylor.city, '1st Avenue')

  def test_customer_has_state(self):
    self.assertEqual(self.taylor.state, 'Nick')

  def test_customer_has_postal_code(self):
    self.assertEqual(self.taylor.postal_code, '12345-67894')

  def test_customer_has_phone_number(self):
    self.assertEqual(self.taylor.phone_number, '615-999-9999')

  def test_customer_exists_in_database(self):
    self.assertIsNotNone(self.taylor.id)








