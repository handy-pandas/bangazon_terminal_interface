"""
Terminal Interface configuration for the Order table interaction in the database
"""
import sqlite3

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
    """
    Add a row to the Orders table.

    Arguments:
      customer_id(int): the active customer primary key.

    Author:
      wocaldwell
    """
    with sqlite3.connect('bangazon.db') as conn:
      c = conn.cursor()
      c.execute("insert into Orders values (null, '{}', null)".format(customer_id))
      conn.commit()

  def retrieve_order_by_payment_type_none(self, customer_id):
    """
    Query the Orders table for a row that includes the active customer and no added payment type.

    Arguments:
      customer_id(int): the active customer primary key.

    Return:
      customer_order(list) a list of tuples that are the rows matching the active customer and pyment type null. This may return an empty list or a list with one item.

    Author:
      wocaldwell
    """
    with sqlite3.connect('bangazon.db') as conn:
      c = conn.cursor()
      c.execute("SELECT * FROM Orders WHERE customer_Id = '{}' AND payment_type_Id is null".format(customer_id))
      customer_order = c.fetchall()
    return customer_order

  def make_order_active(self, active_customer_id):
    """
    If an order exists, return it. Else, create it and return the pk

    Args:
        active_customer_id (Int): Id for active customer

    Returns:
        active_order_pk (Int): integer of active customer's order_id

    Author:
        Taylor Perkins
        wocaldwell
    """
    active_order = self.retrieve_order_by_payment_type_none(active_customer_id)

    if active_order == []:
      self.create_order_in_database(active_customer_id)
      active_order = self.retrieve_order_by_payment_type_none(active_customer_id)
      self.active_order_pk = active_order[0][0]

    else:
      self.active_order_pk = active_order[0][0]

    return self.active_order_pk

  def get_specific_order(self, active_order_id):
    """Summary

    Args:
      active_order_id (Int): The active order is the order that is currently attached to the customer

    Returns:
      closed_order (Int): integer for the order that the customer has built 

    Author:
      Nick Nash
    """
    with sqlite3.connect('bangazon.db') as conn:
      c = conn.cursor()
      c.execute("SELECT SUM(price) FROM Product LEFT JOIN ProductOrder ON ProductOrder.product_Id = Product.product_Id LEFT JOIN Orders ON Orders.order_Id = ProductOrder.order_Id WHERE Orders.order_Id = '{}'".format(active_order_id))
      current_order = c.fetchall()
    return current_order[0][0]

  def update_order(self, payment_type_id):
    """
    Updates current order's payement type id in the database

    Arguments:
      payment_type_id (Int): The current payment type's id the customer wants to use for purchasing order

    Returns:
      n/a

    Author:
      Adam Myers
    """
    with sqlite3.connect("bangazon.db") as conn:
      c = conn.cursor()

      c.execute("update Orders set payment_type_Id = '{}' where order_Id = '{}'".format(payment_type_id, self.active_order_pk))

      conn.commit()

  def retrieve_customers_current_order(self, database="bangazon.db"):
    """
    Retrieve customer's products for their current order

    Args:
      n/a

    Returns:
      products_on_current_order (List): list of the products on the current order

    Author:
      Adam Myers
    """
    with sqlite3.connect(database) as conn:
      c = conn.cursor()

      c.execute("select Product.title from Product left join ProductOrder on Product.product_Id = ProductOrder.product_Id where ProductOrder.order_Id = '{}'".format(self.active_order_pk))

      products_on_current_order = c.fetchall()

      return products_on_current_order

if __name__ == "__main__":
  test = Order()
  test.active_order_pk = 1
  print_me = test.retrieve_customers_current_order(database="../bangazon.db")
  print(print_me)


