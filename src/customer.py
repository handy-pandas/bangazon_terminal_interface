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

    def retrieve_customer_from_database_by_name(self, name):
        return { 'name': 'Nick Nash'}

    def retrieve_customer_from_database_by_id(self, id):
        pass



