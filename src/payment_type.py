import sqlite3

"""
Terminal Interface configuration for the Payment Type table interaction in the database
"""
class PaymentType(object):
  """
  This class is to handle interactions with the payment_type table through sqlite

  Methods:

  Author:
  Nick Nash
  Taylor Perkins
  Talbot Lawrence
  William Caldwell
  Adam Myers
  """

  def __init__(self):
    with sqlite3.connect('../bangazon.db') as conn:
      self.c = conn.cursor()
      self.payment_type_table_needs_insert = True

  def add_payment_type_to_database(self, new_payment_type):
    """
    Add a payment type to the paymetent type table in the bangazon database.

    Arguments:
    new_payment_type(Dictionary), The attributes of the new payment type.

    Returns:
    N/A

    Author:
    wocaldwell
    Nick Nash
    """
    if self.payment_type_table_needs_insert:
      self.c.execute("INSERT INTO PaymentType VALUES (NULL, '{}', '{}', '{}')".format(new_payment_type['account_number'], new_payment_type['name'], new_payment_type['customer_id']))
    else:
      pass

  def retrieve_payment_type_from_database_by_all_attributes(self, new_payment_type):
    """
    Retrieve a payment type from the PaymentType table in the bangazon database.

    Arguments:
    new_payment_type(Dictionary) The attributes of the new payment type.

    Returns:
    new_payment_type(Dictionary) The attributes of the new payment type.

    Author:
    wocaldwell
    """
    return new_payment_type


  def get_active_users_payment_types(self, active_customer_id):
    """
    Gets the active user's payment types.

    Arguments:
    new_payment_type(Dictionary) The attributes of the new payment type.

    Returns:
    payment_types(List of Tuples) The payment types separated into tuples.

    Author:
    Nick Nash
    """
    payment_types = [(1, 1, 1234567890123456, 'Visa')]
    return payment_types





