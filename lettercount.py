rom sys import argv
import string

script, filename = argv

text = open(filename)
book = text.read()
text.close()

book = book.replace('.', " ")
book = book.replace(',', " ")
book = book.replace('-', " ")
book = book.replace(':', " ")
book = book.replace('/', " ")
book = book.replace('$', " ")
book = book.replace('!', " ")
book = book.replace('?', " ")
book = book.replace(';', " ")
book = book.replace('(', " ")
book = book.replace("'", " ")	
book = book.replace(')', " ")

book_list = book.split()

book_dict = {}

for word in book_list: #for each word in our list of words from the book
	book_dict[word] = 0 #edit book_dictionary 
	

for word in book_list:
	book_dict[word] += 1

print book_dict



# length = len(book_list)

# a = dict(zip([book_list], [0 * length])

# print a 

# a = {}
#for word in book2: #for each word in the list of words from the book
#	a = dict(zip([word], [0 * length]) 


