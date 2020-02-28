import sys
"""This program use the built in time function to get the current time"""
import time
print("Unformatted local time")
data = time.localtime()
print (data)
year, mon, mday, hour, min, sec, wday, yday, isdst = data
print("The current time is:")
print("{0}:{1}".format(hour,min))


