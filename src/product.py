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

    def retrieve_all_products():
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
        product_list = []
        with sqlite3.connect('bangazon.db') as conn:
            c = conn.cursor()

            c.execute("SELECT product_Id, title, price FROM Product")
            products_list = c.fetchall()
            """Print statement for developement testing."""
            # print(products_list)
            return products_list

"""
Below is for developmental purposes only. To allow for testing of the sql statements during testing.
"""
if __name__ == "__main__":
    Product.retrieve_all_products()
