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

    def add_customer_to_database(self, customer, database='bangazon.db'):
        """
        This method inserts into Customer table in the database the information of name, address, city, state, postal_code

        Arguments:
            customer (Dictionary): needs to contain attributes of name, address, city, state, postal_code

        Returns:
            n/a

        Author:
            Adam Myers
        """
        with sqlite3.connect(database) as conn:
            c = conn.cursor()

            c.execute("insert into Customer values (?, ?, ?, ?, ?, ?, ?)",
            (None, customer['name'], customer['address'], customer['city'], customer['state'], customer['postal_code'], customer['phone_number']))

            conn.commit()

    def retrieve_customer_from_database_by_id(self, customer_id, database='bangazon.db'):
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
        with sqlite3.connect(database) as conn:
            c = conn.cursor()

            c.execute("select * from Customer where Customer.customer_Id = '{}'".format(customer_id))

            query = c.fetchall()
            query = query[0]
            queried_customer = { 'id': query[0], 'name': query[1], 'address': query[2], 'city': query[3], 'state': query[4], 'postal_code': query[5] }
            return queried_customer

    def retrieve_all_customers(self, database='bangazon.db'):
        """
        This method makes a query to db and brings back all current customers

        Arguments:
            n/a

        Returns:
            (List): List of Dictionaries representing all customers from the database.

        Author: 
            Adam Myers
        """

        # Connecting to the database
        with sqlite3.connect(database) as conn:

            # Creating a cursor
            c = conn.cursor()

            # Generating a query and executing that query
            c.execute("select * from Customer")

            # Fetching data from previously executed query
            queried_customers = c.fetchall()

            # Post processing
            for cust_index, each_customer in enumerate(queried_customers):
                customer = { 'id': each_customer[0], 'name': each_customer[1] }
                queried_customers[cust_index] = customer

            return queried_customers

"""
Below is for developmental purposes only. To allow for creation of the database prior to having a setup function run when the menu appears.
"""
if __name__ == "__main__":
    test = Customer()
    test_cust = { 'name': 'Bobby', 'address': '123 test me Ave', 'city': 'TestVille', 'state': 'WyTesting', 'postal_code':  '123123', 'phone_number':  '123123'}

    test.add_customer_to_database(test_cust, database='../bangazon.db')
    print_me = test.retrieve_all_customers(database='../bangazon.db')
    print_test_2 = test.retrieve_customer_from_database_by_id(1, database='../bangazon.db')

    print("Added customer 'Bobby' :)")
    print("All customers: {}".format(print_me))
    print("Customer by ID 1: {}".format(print_test_2))





    


