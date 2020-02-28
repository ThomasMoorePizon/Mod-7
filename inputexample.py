import sys
print ("Input: date, time, store, item, cost, payment")
"""This program takes in 6 items and prints out the 4th and 5th one labeled item and cost"""
print ("Type a blank line to exit")
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 1:
		sys.exit(1)
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		print("Item	Cost")
		print("{0}\t{1}".format(item, cost))
	else:
		print ("You do not enter the right number of items")
sys.exit()

