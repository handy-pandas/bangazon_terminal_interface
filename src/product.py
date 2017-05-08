"""
Terminal Interface configuration for the Product table interaction in the database
"""

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
        """

        products_list = [(1, 'ball', '12.99')]
        return products_list

