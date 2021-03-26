# make class Booklist!
class Booklist():
	# Initialization function
	def __init__(self):
		# initialize books attribute
		self.books = []

	# method to add a book
	def add(self, title, author):
		# blank dict
		book = {}
		# add title/author to dict
		book['title'] = title
		book['author'] = author

		# append dict to books attribute (the list)
		self.books.append(book)

	def count_books(self):
    	return len(self.books)
  
	def remove_title(self, title):
    		# loop throubh books, remove the book if the title matches title passed in
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)

	# method for displaing book titles as a list, in alphabetical order
	def display_titles(self):
		# initialize blank list
		titles = []
		# loop through books attribute and add all titles to list
		for book in self.books:
			titles.append(book['title'])

		# sort titles alphabetically
		titles.sort()

		# print sorted titles
		return(titles)