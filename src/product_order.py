"""
Terminal Interface configuration for the ProductOrder table interaction in the database
"""
class ProductOrder(object):
  """
  This class is to handle interactions with the ProductOrder table in database through sqlite

  Methods:        

  Author:
      Adam Myers
  """

  def retrieve_products_by_active_order(self, active_order_id):

    products_in_active_order = [1, 2, 3, 4, 5]
    return products_in_active_order


