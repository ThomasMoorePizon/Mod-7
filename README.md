# Mod-7
Mod 7 Homework
1.  Try the code below and revise it to current time. 
import sys
for line in sys.stdin:
data = line.strip().split("\t")
if len(data) == 6:
date, time, store, item, cost, payment = data
print "{0}\t{1}".format(item, cost)

First, I coded this up with some users input verification in inputexample.py
Then I adjusted the code to print the time out in inputexampletime.py
I also wrote a program to get the current time fct.py

2.  Add the timedelta to the datetime and subtract 60 second and added 2 year . (Hit: timedelta(seconds=60))  For each condition, state the code and output.
from datetime import timedelta  
#Add 1 day  

I built code to use datetime to get the current date time, time 60 seconds ago, and 2 years in the future. It looks like timedelta takes days but not years - this could be an issue with leap year? I will research more on this. This is in timedelta.py

3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
>>> from datetime import timedelta
>>> d = timedelta(microseconds=-1)
>>> (d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

I built code to create the timedelta object in timedeltaobject.py. The main thing is to check on how to do leap years - or does 365 days always become 1 year in this function?

4. Write a function that takes two arguments (feet and inches) with this time object
 from datetime import datetime 
# get current date 
>>>datetime_object = datetime.now() 
>>>print(datetime_object) 
>>> print('Type :- ',type(datetime_object)) 
Add function that takes two argument

Finally, I wrote a function the take feet and inches and then creates a time object. This is in feettime.py. We could develop this function to connect these feet and inches to the time object - maybe timing ao objects movements?
