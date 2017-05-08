import unittest

import sys; sys.path.append('../')
from src.order import Order
from src.payment_type import PaymentType
from src.product_order import ProductOrder
from bangazon_control import BangazonControl
class TestOrder(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.control = BangazonControl()    
    self.order = Order()
    self.payment_type = PaymentType()
    self.product_order = ProductOrder()

  def test_if_order_exists_in_database(self):    
    customer_id = 1
    payment_type_id = None
    self.order.create_order_in_database(customer_id)

    customer_order = self.order.retrieve_order_by_attributes(customer_id, payment_type_id)

    self.assertEqual(customer_order['customer_id'], customer_id)
    self.assertEqual(customer_order['payment_type_id'], payment_type_id)

  def test_if_payment_type_can_be_created_in_database(self):        
    self.control.set_active_customer(1)
    new_payment_type = self.control.create_payment_type(self.control.active_customer, "visa", 1234567899999999)
    self.payment_type.add_payment_type_to_database(new_payment_type)
    retrieved_payment_type = self.payment_type.retrieve_payment_type_from_database_by_all_attributes(new_payment_type)

    self.assertEqual(new_payment_type["name"], retrieved_payment_type['name'])
    self.assertEqual(new_payment_type["account_number"], retrieved_payment_type['account_number'])















