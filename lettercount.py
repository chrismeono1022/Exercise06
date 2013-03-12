from sys import argv 

script, filename = argv

txt = open(filename)
book = txt.read()
txt.close()

lowercase_book = book.lower()

place_holder = [0] * 26

for letter in lowercase_book:
	position = ord(letter) - 97
	if position >= 0 and position <= 26:
		place_holder[position] += 1

for position in place_holder:
	print position