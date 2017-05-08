import unittest

import sys; sys.path.append('../')
from src.payment_type import PaymentType
from bangazon_control import BangazonControl


class TestActiveCustomer(unittest.TestCase):

    def test_if_customer_is_active(self):
        control = BangazonControl()
        active_customer = control.choose_active_customer()

        self.assertEqual(active_customer, 1)
        