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
        queries (Dictionary): 

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
            order by ord.order_Id, cu.customer_Id, pro.price DESC
            group by pro.title  
            limit 4
            """)

        query_1 = c.fetchall()

        c.execute("""
            select 'Totals:', count(ord.order_Id), count(cu.customer_Id), sum(pro.price) 
            from Product pro 
            join ProductOrder po on pro.product_Id = po.product_Id 
            join Orders ord on po.order_Id = ord.order_Id 
            join Customer cu on ord.customer_Id = cu.customer_Id 
            group by ord.order_Id, cu.customer_Id, pro.price
            limit 1
            """)

        query_2 = c.fetchall()

        queries = { 'Popularity': query_1, 'Totals': query_2 }

        return queries

def proper_spacing_product(title):

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

    string = string[::-1]
    broken_up = [ string[start:start+3] for start in range(0, len(string), 3) ]
    joined = ','.join(broken_up)
    return joined[::-1]

"""
Below is for developmental purposes only. To allow for retrieval before having functionality of menu options.
"""
if __name__ == "__main__":
    #create_popularity_view(database='../bangazon.db')
    # Product 18 characters with one constant space (so 17 available)
    # Order 11 characters
    # Customer 11 characters
    # Revenue 15 characters

    test1 = 'spacingtest'
    test2 = 1234
    test3 = 2134
    test4 = 1234.01
    test22 = 'a'
    test33 = 'asdflkjasdflkjasdf'

    test1 = proper_spacing_product(test1)
    test22 = proper_spacing_product(test22)
    test33 = proper_spacing_product(test33)

    test2 = proper_spacing_order_and_customer(test2)
    test3 = proper_spacing_order_and_customer(test3)
    test4 = proper_spacing_revenue(test4)

    total1 = 123123
    total2 = 1235324
    total3 = 45345324234.01

    total1 = proper_spacing_order_and_customer(total1)
    total2 = proper_spacing_order_and_customer(total2)
    total3 = proper_spacing_revenue(total3)




    print("Product           Orders     Customers  Revenue")
    print("*******************************************************")
    print("{} {}{}${}".format(test1, test2, test3, test4))
    print("{} {}{}${}".format(test22, test2, test3, test4))
    print("{} {}{}${}".format(test33, test2, test3, test4))
    print("*******************************************************")
    print("Totals:           {}{}${}".format(total1, total2, total3))



