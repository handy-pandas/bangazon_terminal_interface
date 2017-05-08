"""
Terminal Interface configuration for the Order table interaction in the database
"""
class Order(object):

	"""
	This class is to handle interactions with the order table through sqlite

	Methods: 
		create_order_by_database: simply creates the order in the database
		retrieve_order_by_attributes: it retrieves and returns the order by its attributes

	Author:
	Nick Nash
	Taylor Perkins
	Talbot Lawrence
	William Caldwell
	Adam Myers
	"""

	def create_order_in_database(self, customer_id):
		pass

	def retrieve_order_by_attributes(self, customer_id=None, payment_type_id=None):
		return {'customer_id': 1, 'payment_type_id': None}