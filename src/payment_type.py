import sqlite3

"""
Terminal Interface configuration for the Payment Type table interaction in the database
"""
class PaymentType(object):
  """
  This class is to handle interactions with the payment_type table through sqlite

  Methods:
    add_payment_type_to_database: Adds the user's payment types to the database
    retrieve_payment_type_from_database_by_all_attributes: Retrieves the active user's payment info from the database
    get_active_users_payment_types: etrieves the active user's payment info from the database

  Author:
    Nick Nash
    Taylor Perkins
    Talbot Lawrence
    William Caldwell
    Adam Myers
  """

  def add_payment_type_to_database(self, new_payment_type, database="bangazon.db"):
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
    with sqlite3.connect(database) as conn:
      c = conn.cursor()
      c.execute("INSERT INTO PaymentType VALUES (NULL, '{}', '{}', '{}')".format(new_payment_type['customer_id'], new_payment_type['account_number'], new_payment_type['name']))

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
    with sqlite3.connect("bangazon.db") as conn:
      c = conn.cursor()
      c.execute("SELECT PaymentType.name FROM PaymentType LEFT JOIN Customer ON PaymentType.customer_Id = Customer.customer_Id WHERE Customer.customer_Id is '{}'".format(active_customer_id))
      payments = c.fetchall()
    return payments


