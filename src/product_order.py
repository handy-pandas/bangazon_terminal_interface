"""
Terminal Interface configuration for the ProductOrder table interaction in the database
"""
import sqlite3

class ProductOrder(object):
    """
    This class is to handle interactions with the ProductOrder table in database through sqlite

    Methods:
      add_product_id_and_order_id_to_product_order_table: Add the selected product id and active order id to the OrderProduct table.
    Author:
      Adam Myers
    """
    def add_product_id_and_order_id_to_product_order_table(self, active_order_id, product_id):
        """
        Add the selected product id and active order id to the OrderProduct table.

        Arguments:
            active_order_id(int): the primary key of the active order.
            product_id(int): the primary key product selected by the user.

        Returns:
            n/a

        Author:
            wocaldwell
        """
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()
            c.execute("insert into ProductOrder values (null, '{}', '{}')".format(active_order_id, product_id))
            conn.commit()

    def retrieve_products_by_active_order(self, active_order_id):

        products_in_active_order = [1, 2, 3, 4, 5]
        return products_in_active_order


