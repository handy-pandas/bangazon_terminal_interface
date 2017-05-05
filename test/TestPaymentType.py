import unittest

import sys; sys.path.append('../')
from src.customer import Customer
from src.payment_type import PaymentType
from bangazon_control import BangazonControl


class TestPaymentType(unittest.TestCase):

    def test_if_payment_type_can_be_created_in_database(self):
        payment_type = PaymentType()
        control = BangazonControl()

        new_payment_type = control.create_payment_type("visa", 1234567899999999)
        payment_type.add_payment_type_to_database(new_payment_type)
        retrieved_payment_type = payment_type.retrieve_payment_type_from_database_by_all_attributes(new_payment_type)

        self.assertEqual(new_payment_type["name"], retrieved_payment_type['name'])
        self.assertEqual(new_payment_type["account_number"], retrieved_payment_type['account_number'])




