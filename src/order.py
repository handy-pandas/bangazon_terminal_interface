"""
Terminal Interface configuration for the Order table interaction in the database
"""
class Order(object):
  """
  This class is to handle interactions with the order table through sqlite

  Methods: 
          create_order_by_database: simply creates the order in the database
          retrieve_order_by_attributes: it retrieves and returns the order by its attributes

  Author:
  Nick Nash
  Taylor Perkins
  Talbot Lawrence
  William Caldwell
  Adam Myers
  """

  def create_order_in_database(self, customer_id):
    pass

  def retrieve_order_by_attributes(self, customer_id=None, payment_type_id=None):
    return {'customer_id': 1, 'payment_type_id': None}

  def make_order_active(self, active_customer_id):
    """
    If an order exists, return it. Else, create it and return the pk

    Args:
        active_customer_id (Int): Id for active customer

    Returns:
        active_order_pk (Int): integer of active customer's order_id

    Author:
        Taylor Perkins
    """
    active_order_pk = 1
    return active_order_pk

  def get_specific_order(self, active_order_id):
    closed_order = [(1, 1, 1)]
    return closed_order[0][2]








