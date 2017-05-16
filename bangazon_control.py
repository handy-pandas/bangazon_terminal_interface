import os
import sys
from src.customer import Customer
from src.order import Order
from src.payment_type import PaymentType
from src.product import Product
from src.product_order import ProductOrder
from src.create_database import CreateDatabase
from src.popularity_sql import *

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

    def __init__(self):
        self.active_customer = None
        self.active_order_pk = None
        self.display_menu = 0
        self.create_database = 0


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
        os.system('cls' if os.name == 'nt' else 'clear')
        new_customer = { 'name': name, 'address' : address, 'state': state, 'city': city, 'postal_code': postal_code, 'phone_number': phone_number }
        return new_customer

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
        os.system('cls' if os.name == 'nt' else 'clear')
        list_customer = self.retrieve_all_customers()
        counter = 1

        print("\nWhich customer will be active?\n")

        for each_customer in list_customer:
            print("{}. {}".format(counter, each_customer['name']))
            counter += 1

        selection = input('> ')
        try:
            selection = int(selection)
            if selection in range(1, counter):
                selection = selection-1
                self.active_customer = list_customer[selection]['id']
            else:
                print("That number is not on the list.")
                self.choose_active_customer()
        except ValueError:
            print('Numbers only, dorkus.')
            self.choose_active_customer()

        self.active_order_pk = None


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

    def display_products_and_add_to_cart(self):
        """
        Display all the products from the product table in the cli. When the customer selects a product from the list the product and active order id's are added to the database.
        Arguments:
            n/a

        Returns:
            n/a

        Author:
            wocaldwell
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        product_list = self.retrieve_all_products()
        counter = 1
        for product in product_list:
            print("{}. {}".format(counter, product[1]))
            counter += 1
        print("{}. {}".format(counter, "Done adding products"))
        product_selection = input('> ')

        try:
            product_selection = int(product_selection)
            if product_selection == counter:
                self.display_menu = 0
                return

            elif product_selection in range(1, counter):
                product_selection = product_selection-1
                self.add_product_id_and_order_id_to_product_order_table(self.make_order_active(self.active_customer), product_list[product_selection][0])
            else:
                print("That ain't on the list!!")

        except ValueError:
            print('Numbers only, dorkus.')

        self.display_products_and_add_to_cart()

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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Enter customer name")
        name = input("> ")

        name = self.remove_odd_characters(name)

        print("Enter street address")
        street_address = input("> ")

        street_address = self.remove_odd_characters(street_address)

        print("Enter city")
        city = input("> ")

        city = self.remove_odd_characters(city)

        print("Enter state")
        state = input("> ")

        state = self.remove_odd_characters(state)

        print("Enter postal code")
        postal_code = input("> ")

        postal_code = self.remove_odd_characters(postal_code)

        print("Enter phone number")
        phone_number = input("> ")

        phone_number = self.remove_odd_characters(phone_number)

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
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_menu = 1
        if self.create_database == 0:
            CreateDatabase()
            self.create_database = 1

        print('\n*********************************************************')
        print('**  Welcome to Bangazon! Command Line Ordering System  **')
        print('*********************************************************')
        print('1. Create a customer account\n2. Choose active customer\n3. Create a payment option\n4. Add product to shopping cart\n5. Complete an order\n6. Add a product from customer\n7. See product popularity\n8. Display Products On Active Order\n9. Leave Bangazon!')
        selection = input('> ')

        if selection == '1':
            self.menu_create_customer()

        if selection == '2':
            self.choose_active_customer()

        if selection == '3':
            if self.active_customer == None:
                self.choose_active_customer()
            self.display_create_payment_type()

        if selection == '4':
            if self.active_customer == None:
                self.choose_active_customer()
            self.display_products_and_add_to_cart()

        if selection == '5':
            if self.active_customer == None:
                self.choose_active_customer()
            self.complete_order()

        if selection == '6':
            self.display_add_product()

        if selection == '7':
            self.display_popularity()

        if selection == '8':
            if self.active_customer == None:
                print("You don't have an active customer")
                self.choose_active_customer()

            self.display_products_on_order()

        if selection == '9':
            sys.exit()

        self.display_menu = 0

    def display_add_product(self):
        """
        Displays menu prompts for adding a product from a customer

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Adam Myers
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        list_customer = self.retrieve_all_customers()
        product_information = dict()

        print("\nWhich customer will be adding this product?\n")

        for cust_index, each_customer in enumerate(list_customer):
            print("{}. {}".format(cust_index+1, each_customer['name']))

        customer = input("> ")

        try:
            customer = int(customer)-1
            product_information['seller_id'] = list_customer[customer]['id']
        except ValueError:
            print('Numbers only, please.')
            self.display_add_product()
            return

        print("\nWhat is the title of this product?\n")
        product_information['title'] = input("> ")

        product_information['title'] = self.remove_odd_characters(product_information['title'])

        print("\nWhat is the price of this product?\n")
        price = input("> ")

        price = self.remove_odd_characters(price, 'number')

        try:
            product_information['price'] = round(float(price), 2)
        except ValueError:
            print("Numbers only, please.")
            self.display_add_product()
            return

        self.add_product(product_information)

        print("\nProduct has been successfully added")
        input('Press Return to continue')

    def display_products_on_order(self):
        """
        Displays the products on the current order.

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Adam Myers
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        # Retrieves the current Order Id
        current_order = self.retrieve_order_by_payment_type_none(self.active_customer)

        # Handles the exception if there is no active order for that customer
        if current_order == []:
            print("\n***You don't have an Active Order from which to list products***\n***Please add a product to an order to create an Active Order***")
            input("\nPress Return to continue\n")
            return
        else:
            self.active_order_pk = current_order[0][0]

        # Retrieves products on the active order
        products_on_order = self.retrieve_customers_current_order()

        # Handles the exception if theres no products on the current order
        if products_on_order == []:
            print("\n***You don't have any products on order***\n")
            input("\nPress Return to continue\n")
            return

        # Displays products from the current order
        print("\n***Products on current order***\n")
        for each in products_on_order:
            print("{}".format(each[0]))

        input("\nPress Return to continue\n")


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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nEnter payment type (e.g. AMEX, VISA, Mastercard)")
        name = input("> ")

        name = self.remove_odd_characters(name)

        print("\nEnter account number")
        account_number = input("> ")

        new_payment_type = self.create_payment_type(self.active_customer, name, account_number)
        self.add_payment_type_to_database(new_payment_type)


    def complete_order(self):
        """
        Displays the order total and allows the customer to confirm the purchase.
        
        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Nick Nash
            Adam Myers
        """
        # self.get_specific_order(self.active_order_pk)
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.active_order_pk == None:
            current_order = self.retrieve_order_by_payment_type_none(self.active_customer)

            if current_order == []:
                input("\nPlease add some products to an order first. Press Return key to return to main menu.\n")
                return
            else:
                self.active_order_pk = current_order[0][0]

        active_order = self.get_specific_order(self.active_order_pk)
        products_on_order = self.retrieve_customers_current_order()

        print("\n*** Products on current order ***\n")
        for each in products_on_order:
            print("{}".format(each[0]))

        print("\nYour order total is ${}. Ready to purchase?".format(round(active_order, 2)))
        choice = input("(Y/N) > ")

        if choice == "Y" or choice =="y":
            list_of_payment_types = self.get_active_users_payment_types(self.active_customer)

            if list_of_payment_types == []:
                input("\nYou don't have a payment type stored, Press Return to create one.\n")
                self.display_create_payment_type()

            list_of_payment_types = self.get_active_users_payment_types(self.active_customer)

            print("\nChoose a payment option")
            counter = 1

            for payment in list_of_payment_types:
                print("{}. {}".format(counter, payment[1]))
                counter += 1

            chosen_payment = input("> ")

            try:
                chosen_payment = int(chosen_payment)

                if chosen_payment in range(1, counter):
                    self.update_order(list_of_payment_types[chosen_payment-1][0])

                    self.active_order_pk = None

                    input("\nYour order is complete! Press any key to return to main menu.\n")

                    self.display_menu = 0
                    return

                else:
                    print("\nPlease choose a valid option!\n")

            except ValueError:
                print("\nPlease select a number!\n")

        elif choice == "N" or choice == "n":
            print("\n")

        else:
            print("\nPlease input a valid choice!\n")
            self.complete_order()

    
    def display_popularity(self):
        """
        Displays popularity view of the popular products and their totals

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            Adam Myers
            Talbot Lawrence
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        queries = query_popularity_view()
        totals = { 'orders': 0, 'customers': 0, 'revenues': 0 }

        print("\nProduct           Orders     Customers  Revenue")
        print("*******************************************************")
        for each in queries['Popularity']:
            each = list(each)
            each[0] = proper_spacing_product(each[0])
            totals['orders'] += each[1]
            each[1] = proper_spacing_order_and_customer(each[1])
            totals['customers'] += each[2]
            each[2] = proper_spacing_order_and_customer(each[2])
            totals['revenues'] += each[3]
            each[3] = proper_spacing_revenue(each[3])
            print("{} {}{}${}".format(each[0], each[1], each[2], each[3]))

        print("*******************************************************")
        totals['orders'] = proper_spacing_order_and_customer(totals['orders'])
        totals['customers'] = proper_spacing_order_and_customer(totals['customers'])
        totals['revenues'] = proper_spacing_revenue(totals['revenues'])

        print("Totals:           {}{}${}".format(totals['orders'], totals['customers'], totals['revenues']))

        input("\nPress Return to Continue...\n")

    def remove_odd_characters(self, string, check_for_decimals=True):
        """
        Removed unwanted characters from a string to prep for sql insert.

        Arguments:
            string (String): String needing to be have removed odd characters
            check_for_decimals (Boolean): if anything other than True will remove '.' from string, if not will leave '.' in string

        Returns:
            string (String): After having removed odd characters.

        Author:
            Adam Myers
        """
        if check_for_decimals == True:
            for each in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '[', ']', '{', '}', '\\', "'", '"', '.', '<', '>', '/', '?', ':', ';']:
                if each in string:
                    string = string.replace(each, '')
        else:
            for each in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '[', ']', '{', '}', '\\', "'", '"', '<', '>', '/', '?', ':', ';']:
                if each in string:
                    string = string.replace(each, '')

        return string


if __name__ == '__main__':
    Bangazon = BangazonControl()
    while Bangazon.display_menu == 0:
        Bangazon.display_main_menu()




