import unittest

import sys; sys.path.append('../')
from src.order import Order
from bangazon_control import BangazonControl
#customerid and paymenttypeid
class TestOrder(unittest.TestCase):

    def test_if_order_exists_in_database(self):
        order = Order()
        control = BangazonControl()
        customer_id = 1
        payment_type_id = None
        order.create_order_in_database(customer_id)

        customer_order = order.retrieve_order_by_attributes(customer_id, payment_type_id)

        self.assertEqual(customer_order['customer_id'], customer_id)
        self.assertEqual(customer_order['payment_type_id'], payment_type_id)