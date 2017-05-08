"""
Terminal Interface configuration for the Customer table interaction in the database
"""
class Customer(object):
    """
    This class is to handle interactions with the database through sqlite

    Methods:
        add_customer_to_database: used to insert the customer information into the database.
        retrieve_customer_from_database_by_name: used to retrieve the customer information from the database by name.
        retrieve_customer_from_database_by_id: used to retrieve the customer information from the database by id.

    Author:
        Adam Myers
    """

    def __init__(self):
        pass

    def add_customer_to_database(self, customer):
        pass

    def retrieve_customer_from_database_by_all_attributes(self, new_customer):
        return new_customer

    def retrieve_customer_from_database_by_id(self, id):
        pass

    def retrieve_all_customers(self):
        """
        Makes a query to db and brings back all current customers

        Returns:
            customer_list (LIST): List of Tuples representing all customers

        Author: 
            Taylor Perkins
        """
        customer_list = [(1)]
        return customer_list



