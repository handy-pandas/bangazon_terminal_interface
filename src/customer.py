"""
Terminal Interface configuration for the Customer table interaction in the database
"""
class Customer(object):
    """
    This class is to handle interactions with the database through sqlite

    Methods:
        create_customer: used to create a dict() of the information pertaining to the customer.
        add_customer_to_database: used to insert the customer information into the database.
        retrieve_customer_from_database_by_name: used to retrieve the customer information from the database by name.
        retrieve_customer_from_database_by_id: used to retrieve the customer information from the database by id.

    Author:
        Adam Myers
    """

    def __init__(self):
        pass

    def create_customer(self, name, address, state, city, postal_code):
        """
        This method creates a dictionary that contains information about the customer and returns that dictionary.

        Arguments:
            name (String): Name of the customer.
            address (String): Address of the customer.
            state (String): State of which the customer lives.
            city (String): City the customer lives in.
            postal_code (String): Postal code that the customer lives in.

        Author:
            Adam Myers
        """
        new_customer = { name: name, address : address, state: state, city: city, postal_code: postal_code }
        return new_customer

    def add_customer_to_database(self, customer):
        pass

    def retrieve_customer_from_database_by_name(self, name):
        return { name: 'Nick Nash'}

    def retrieve_customer_from_database_by_id(self, id):
        pass



