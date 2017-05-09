"""
Terminal Interface configuration to choose an active customer in the database
"""
import sqlite3

def ChooseActiveCustomer():
    """
        Selects the active customer from the blank table.

        Arguments:
            N/A

        Returns:
            N/A

        Author: 
            Talbot Lawrence
        """
    with sqlite3.connect('../bangazon.db') as conn:
        c = conn.cursor()

        try:
            c.execute("""SELECT * FROM Customer;""")

        except sqlite3.OperationalError:
            pass


# if __name__ == "__main__":
#     ChooseActiveCustomer()