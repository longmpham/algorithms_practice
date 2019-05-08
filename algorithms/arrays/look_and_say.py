"""
	Look and say sequence

	wiki:
	sequence = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...]

	ie. look_and_say(4) = 1211 <--- index 3

	To generate a member of the sequence from the previous member,
	read off the digits of the previous member, 
	counting the number of digits in groups of the same digit. 

	For example:

	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	1211 is read off as "one 1, one 2, then two 1s" or 111221.
	111221 is read off as "three 1s, two 2s, then one 1" or 312211.


"""


def look_and_say(n):
	# find the number to the nth number.

	if n <= 0 or n >= 30: return 0

	# i have no idea... :(





print(look_and_say(5))



