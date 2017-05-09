"""
Terminal Interface configuration for the Customer table interaction in the database
"""
import sqlite3

class Customer(object):
    """
    This class is to handle interactions with the database through sqlite

    Methods:
        add_customer_to_database: used to insert the customer information into the database.
        retrieve_customer_from_database_by_name: used to retrieve the customer information from the database by name.
        retrieve_customer_from_database_by_id: used to retrieve the customer information from the database by id.
        retrieve_all_customers: used to retrieve all customers from the customer table in the database.

    Author:
        Adam Myers
    """

    def __init__(self):
        pass

    def add_customer_to_database(self, customer):
        """
        This method inserts into Customer table in the database the information of name, address, city, state, postal_code

        Arguments:
            customer (Dictionary): needs to contain attributes of name, address, city, state, postal_code

        Author:
            Adam Myers
        """
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            c.execute("insert into Customer values (?, ?, ?, ?, ?, ?)",
            (None, customer['name'], customer['address'], customer['city'], customer['state'], customer['postal_code']))

            conn.commit()

    def retrieve_customer_from_database_by_all_attributes(self, customer):
        """
        This method retrieves the customer from the Customer database based on the name

        Arguments:
            customer (dictionary): containing attributes of name, address, state, city, postal_code.

        Returns:
            (Dictionary): containing attributes of name, address, state, city, postal_code from the database

        Author:
            Adam Myers
        """
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            c.execute("select * from Customer where Customer.name = '{}' and Customer.address = '{}' and Customer.state = '{}' and Customer.city = '{}' and Customer.postal_code = '{}' limit 1".format(customer['name'], customer['address'], customer['state'], customer['city'], customer['postal_code']))

            query = c.fetchall()
            query = query[0]
            queried_customer = { 'id': query[0], 'name': query[1], 'address': query[2], 'city': query[3], 'state': query[4], 'postal_code': query[5] }
            return queried_customer

    def retrieve_customer_from_database_by_id(self, customer_id):
        """
        This method retrieves the customer from the Customer database based on the name

        Arguments:
            id (Integer): customerId of the customer.

        Returns:
            (Dictionary): containing attributes of name, address, state, city, postal_code from the database

        Author:
            Adam Myers
        """
        query_from_database = None
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            c.execute("select * from Customer where Customer.customer_Id = '{}'".format(customer_id))

            query = c.fetchall()
            query = query[0]
            queried_customer = { 'id': query[0], 'name': query[1], 'address': query[2], 'city': query[3], 'state': query[4], 'postal_code': query[5] }
            return queried_customer

    def retrieve_all_customers(self):
        """
        This method makes a query to db and brings back all current customers

        Arguments:
            N/A

        Returns:
            customer_list (LIST): List of Dictionaries representing all customers from the database.

        Author: 
            Adam Myers
        """
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            c.execute("select * from Customer")
            queried_customers = c.fetchall()

            customer_list = list()

            for each_customer in queried_customers:
                customer = { 'id': each_customer[0], 'name': each_customer[1] }
                customer_list.append(customer)

            return customer_list



