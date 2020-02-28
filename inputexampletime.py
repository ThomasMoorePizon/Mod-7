import sys
print ("Input: date, time, store, item, cost, payment")
"""This program takes in 6 items and prints out the 2nd one labeled time"""
print ("Type a blank line to exit")
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 1:
		sys.exit(1)
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print("Time")
		print("{0}".format(time))
	else:
		print ("You do not enter the right number of items")
sys.exit()

