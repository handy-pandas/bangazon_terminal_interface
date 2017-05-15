"""
Terminal Interface configuration for the Product table interaction in the database
"""
import sqlite3

class Product(object):
    """
    Description:
        This class is to handle interactions with the products table through sqlite

    Methods:
        retrieve_all_products: This is a simple query that brings back all products from Prodct table within bangazon db

    Author:
        Nick Nash
        Taylor Perkins
        Talbot Lawrence
        William Caldwell
        Adam Myers
    """
    def __init__(self):
        pass

    def retrieve_all_products(self):
        """
        This is a simple query that brings back all products from Prodct table within bangazon db

        Arguments:
            None

        Returns:
            products_list (LIST): List of tuples representing all products in db

        Author:
            Taylor Perkins
            wocaldwell
        """
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            c.execute("SELECT product_Id, title, price FROM Product")
            products_list = c.fetchall()
            return products_list

    def add_product(self, product_info, database='bangazon.db'):
        """
        This method allows users to add a product for a customer as the seller

        Arguments:
            product_info (Dictionary): dictionary contains the keys of 'price', 'title', 'seller_id' corresponding to the price of the product, title of the product and seller's customer primary key

        Returns:
            n/a

        Author:
            Adam Myers
        """
        with sqlite3.connect(database) as conn:
            c = conn.cursor()

            c.execute("insert into Product values ('{}', '{}', '{}', '{}')".format(None, product_info['price'], product_info['title'], product_info['seller_id']))

            conn.commit()

