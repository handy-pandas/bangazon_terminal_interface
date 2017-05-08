"""
Terminal Interface configuration for the terminal interface for the user interaction.
"""
class BangazonControl(object):
    """
    This class is to handle interactions with the user from the terminal

    Methods:
        create_customer: used to create a dict() of the information pertaining to the customer.

    Author:
        Adam Myers
    """

    def create_customer(self, name, address, state, city, postal_code):
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
        new_customer = { 'name': name, 'address' : address, 'state': state, 'city': city, 'postal_code': postal_code }
        return new_customer

    def set_active_customer(self, active_customer):
        """Summary

        Args:
            active_customer (Int): Index of active customer from list of all customers

        Returns:
            TYPE: Description
        """
        self.active_customer = 12

    def choose_active_customer(self):
        return 1

    def create_payment_type(self, name, account_number):
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
        new_payment_type = {'name': name, 'account_number': account_number}
        return new_payment_type
