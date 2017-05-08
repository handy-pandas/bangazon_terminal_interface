import unittest

import sys; sys.path.append('../')
from src.order import Order
from src.product import Product
from src.payment_type import PaymentType
from src.product_order import ProductOrder
from bangazon_control import BangazonControl
class TestOrder(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.control = BangazonControl()    
    self.order = Order()
    self.product = Product()
    self.payment_type = PaymentType()
    self.product_order = ProductOrder()
    self.control.set_active_customer(1)    

  def test_if_order_exists_in_database(self):    
    payment_type_id = None
    self.order.create_order_in_database(self.control.active_customer)

    customer_order = self.order.retrieve_order_by_attributes(customer_id, payment_type_id)

    self.assertEqual(customer_order['customer_id'], customer_id)
    self.assertEqual(customer_order['payment_type_id'], payment_type_id)

  def test_if_payment_type_can_be_created_in_database(self):            
    new_payment_type = self.control.create_payment_type(self.control.active_customer, "visa", 1234567899999999)
    self.payment_type.add_payment_type_to_database(new_payment_type)
    retrieved_payment_type = self.payment_type.retrieve_payment_type_from_database_by_all_attributes(new_payment_type)

    self.assertEqual(new_payment_type["name"], retrieved_payment_type['name'])
    self.assertEqual(new_payment_type["account_number"], retrieved_payment_type['account_number'])

  def test_complete_order(self):
    self.control.save_all_products()

    self.assertIsNotNone(self.control.products)    
    selected_product = 1
    self.control.add_product_to_order(selected_product)
    active_order = self.order.make_order_active(self.control.active_customer)
    current_products_in_order = self.product_order.retrieve_products_by_active_order(active_order)    

    self.assertIsNotNone(active_order)
    self.assertIn(selected_product, current_products_in_order)

    self.control.get_sum_of_products_for_current_order(active_order)
    payment_types = self.payment_type.get_active_users_payment_types(active_customer)
    payment_type_ids = [payment[0] for payment in payment_type_ids]
    payment_type_id = 1
    self.assertIn(payment_type_id, payment_type_ids)
    self.control.add_payment_type_to_order(active_order, payment_type_id)


















