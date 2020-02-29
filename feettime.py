"""This program has a function the takes feet and inches and uses a time object"""
from datetime import datetime
def speed(feet,inches):
	datetime_object = datetime.now()
	print(datetime_object)
	print('Type :-',type(datetime_object))

speed(12,2)




