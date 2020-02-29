import sys
"""This program uses the built in datetime function to get the current date/time"""
"""Then time is changed by subtracting 60 seconds"""
"""Then time is changed by adding 2 years"""
from datetime import *
print("Local date/time")
data = datetime.now()
print (data)
print("60 seconds ago it was:")
print(data + timedelta(seconds=-60))
print("In 2 years it will be:")
print(data + timedelta(days=365*2)) 



