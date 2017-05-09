import sys
from src.customer import Customer
from src.order import Order
from src.payment_type import PaymentType
from src.product import Product
from src.product_order import ProductOrder
from src.create_database import CreateDatabase

"""
Terminal Interface configuration for the terminal interface for the user interaction.
"""
class BangazonControl(Customer, Order, PaymentType, Product, ProductOrder):
    """
    This class is to handle interactions with the user from the terminal

    Methods:
        create_customer: used to create a dict() of the information pertaining to the customer.

    Author:
        Adam Myers
    """

    def create_customer(self, name, address, state, city, postal_code, phone_number):
        """
        This method creates a dictionary that contains information about the customer and returns that dictionary.

        Arguments:
            name (String): Name of the customer.
            address (String): Address of the customer.
            state (String): State of which the customer lives.
            city (String): City the customer lives in.
            postal_code (String): Postal code that the customer lives in.

        Returns:
            new_customer (Dictionary): containing attributes of name, address, state, city, postal_code

        Author:
            Adam Myers
        """
        new_customer = { 'name': name, 'address' : address, 'state': state, 'city': city, 'postal_code': postal_code, 'phone_number': phone_number }
        return new_customer

    def set_active_customer(self, active_customer):
        """Summary

        Args:
            active_customer (Int): Index of active customer from list of all customers

        Returns:
            TYPE: Description
        """
        self.active_customer = active_customer

    def choose_active_customer(self):
        """
        Displays the choose active customer when the user selects option 2 .

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Talbot Lawrence
        """
        print("Which customer will be active?")
        list_customer = self.retrieve_all_customers()
        counter = 1
        for each_customer in list_customer:
            print("{}. {}".format(counter, each_customer['name']))
            counter += 1
        selection = input('> ')
        selection = int(selection)-1
        self.set_active_customer(list_customer[selection]['id'])
        # print(self.active_customer)
        # return 1

    def create_payment_type(self, customer_id, name, account_number):
        """
        This method creates a dictionary that contains information about the payment types and returns that dictionary.

        Arguments:
            name (String): Name of the payment type.
            account_number (Int): Account Number.

        Returns:
            new_payment_type (Dictionary): containing attributes of name and account_number

        Author:
            wocaldwell
        """
        new_payment_type = {'customer_id': customer_id, 'name': name, 'account_number': account_number}
        return new_payment_type

    def save_all_customers(self):
        pass

    def save_all_products(self):
        self.products = [(1, 12.99, 'ball')]

    def add_product_to_order(self, index_of_product):
        if self.active_customer:
            self.active_order = self.make_order_active(self.active_customer)
        pass

    def get_sum_of_products_for_current_order(self, active_order_id):
        pass

    def update_payment_type_for_order(self, active_order_id, payment_type_id):
        pass

    def menu_create_customer(self):
        """
        Handles the menu interaction for creating a customer

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Adam Myers
        """
        print("Enter customer name")
        name = input("> ")

        print("Enter street address")
        street_address = input("> ")

        print("Enter city")
        city = input("> ")

        print("Enter state")
        state = input("> ")

        print("Enter postal code")
        postal_code = input("> ")
        
        print("Enter phone number")
        phone_number = input("> ")

        new_customer = self.create_customer(name, street_address, state, city, postal_code, phone_number)
        self.add_customer_to_database(new_customer)

    def display_main_menu(self):
        """
        Displays the main menu when bangazon_control.py is run in the cli and directs to other features based on user input.

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            wocaldwell
        """
        CreateDatabase()
        print('*********************************************************')
        print('**  Welcome to Bangazon! Command Line Ordering System  **')
        print('*********************************************************')
        print('1. Create a customer account\n2. Choose active customer\n3. Create a payment option\n4. Add product to shopping cart\n5. Complete an order\n6. See product popularity\n7. Leave Bangazon!')
        selection = input('> ')
        if selection == '1':
            self.menu_create_customer()
        if selection == '2':
            self.choose_active_customer()
        if selection == '3':
            self.display_create_payment_type()
        if selection == '4':
            pass
        if selection == '5':
            pass
        if selection == '6':
            pass
        if selection == '7':
            sys.exit()
        self.display_main_menu()

    def display_create_payment_type(self):
        """
        Displays the create payment type menu for the customer to input their information.

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Nick Nash
        """
        print("\n\nEnter payment type (e.g. AMEX, VISA, Mastercard")
        name = input("> ")

        print("\nEnter account number")
        account_number = input("> ")

        customer_id = self.choose_active_customer()

        new_payment_type = self.create_payment_type(customer_id, name, account_number)
        self.add_payment_type_to_database(new_payment_type)


if __name__ == '__main__':
    Bangazon = BangazonControl()
    Bangazon.display_main_menu()
