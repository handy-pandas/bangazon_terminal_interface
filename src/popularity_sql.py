"""
Terminal Interface configuration for the popularity view from the menu.
"""
import sqlite3

def query_popularity_view(database='bangazon.db'):
    """
    Retrieves the popularity information from the database through sqlite

    Arguments:
        n/a

    Returns:
        queries (Dictionary): dictionary of both queries with keys of Totals and Popularity 

    Author:
        Adam Myers
        Talbot Lawrence
    """
    with sqlite3.connect(database) as conn:
        c = conn.cursor()

        c.execute("""
            select pro.title, count(ord.order_Id), count(cu.customer_Id), sum(pro.price) 
            from Product pro 
            join ProductOrder po on pro.product_Id = po.product_Id 
            join Orders ord on po.order_Id = ord.order_Id 
            join Customer cu on ord.customer_Id = cu.customer_Id 
            where ord.payment_type_Id is not null
            group by pro.title  
            order by ord.order_Id, cu.customer_Id, pro.price DESC
            limit 4
            """)

        query_1 = c.fetchall()

        c.execute("""
            select count(ord.order_Id), count(cu.customer_Id), sum(pro.price) 
            from Product pro 
            join ProductOrder po on pro.product_Id = po.product_Id 
            join Orders ord on po.order_Id = ord.order_Id 
            join Customer cu on ord.customer_Id = cu.customer_Id 
            where ord.payment_type_Id is not null
            """)

        query_2 = c.fetchall()

        queries = { 'Popularity': query_1, 'Totals': query_2 }

        return queries

def proper_spacing_product(title):
    """
    Formats the spacing of the product column for displaying in the terminal

    Arguments:
        title (String): title of the product for displaying

    Returns:
        title (String): title of the product for displaying formated for 18 characters

    Author:
        Adam Myers
        Talbot Lawrence
    """

    length = len(title)

    if length < 14:
        spaces_needed = 14 - length
        for each in range(0, spaces_needed + 3):
            title = title + " "

    elif length > 14:
        title = title[:14]
        title = title + "..."

    return title

def proper_spacing_order_and_customer(number):
    """
    Formats the spacing of the order column and customer column for displaying in the terminal

    Arguments:
        number (integer): integer representing the totals for respective fields of orders and customers

    Returns:
        number (integer): integer representing the totals for respective fields of orders and customers with proper spacing of 11 characters

    Author:
        Adam Myers
        Talbot Lawrence
    """

    number = str(number)

    length = len(number)

    if length < 11:
        spaces_needed = 11 - length
        for each in range(0, spaces_needed):
            number = number + " "

    elif length > 11:
        number = number[:11]

    return number

def proper_spacing_revenue(number):
    """
    Formats the spacing of the order revenue for displaying in the terminal

    Arguments:
        number (integer): integer representing the totals for revenue

    Returns:
        number (integer): integer representing the totals revenue with proper spacing of 15 characters

    Author:
        Adam Myers
        Talbot Lawrence
    """

    number = str(number)
    length = len(number)

    try:
        integer = number[:number.index('.')]
        change = number[number.index('.'):]

        if len(integer) > 3:
            integer = add_comma(integer)
            number = integer + change
    except ValueError:
        pass

    if length < 14:
        spaces_needed = 14 - length
        for each in range(0, spaces_needed):
            number = number + " "

    elif length > 14:
        number = number[:14]

    return number

def add_comma(string):
    """
    This method adds comma's for lengthy numbers

    Arguments:
        number (integer): integer

    Returns:
        number (string): string of a number with included properly spaced commas

    Author:
        Adam Myers
        Talbot Lawrence
    """

    string = string[::-1]
    broken_up = [ string[start:start+3] for start in range(0, len(string), 3) ]
    joined = ','.join(broken_up)
    return joined[::-1]





