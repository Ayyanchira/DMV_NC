
############## Reading data from csv #################

# import csv, json

# f = open('Spl_1.csv', 'rU')
# reader = csv.DictReader(f, fieldnames = ("Question", "option1", "option2", "option3", "option4", "correctAnswer"))

# store = []
# questions = []

# for row in reader:
# 	question = {"Question": row["Question"],
# 	"option1": row["option1"],
# 	"option2": row["option2"],
# 	"option3": row["option3"],
# 	"option4": row["option4"],
# 	"correctAnswer": row["correctAnswer"]}
# 	store.append(question)


# # if row["Question"] not in questions:
# #       questions.append(row["Question"])
# #       store.append(question)


# f = open( 'data.json', 'w')
# out = json.dumps(store, indent=4)
# f.write(out)


############## Reading data from excel #################


import xlrd, json
import random

class dataCollection:

	def __init__(self, book):

		self.book = xlrd.open_workbook(book)
		self.store = []


	def getQuestions(self, questionType):

		if questionType == 1:

			sh1 = self.book.sheet_by_index(0)
			rand = random.sample(range(1,sh1.nrows), 15)
			#print(rand)

			for rx in rand:
				question = {"Question": sh1.row(rx)[1].value,
				"option1": sh1.row(rx)[2].value,
				"option2": sh1.row(rx)[3].value,
				"option3": sh1.row(rx)[4].value,
				"option4": sh1.row(rx)[5].value,
				"correctAnswer": sh1.row(rx)[6].value}
				self.store.append(question)	
			return self.store

		if questionType == 2:

			sh2 = self.book.sheet_by_index(1)
			rand = random.sample(range(1,sh2.nrows), 15)

			for rx in rand:
				question = {"Question": sh2.row(rx)[1].value,
				"option1": sh2.row(rx)[2].value,
				"option2": sh2.row(rx)[3].value,
				"option3": sh2.row(rx)[4].value,
				"option4": sh2.row(rx)[5].value,
				"correctAnswer": sh2.row(rx)[6].value}
				self.store.append(question)
			return self.store

		if questionType == 3:

			sh3 = self.book.sheet_by_index(2)
			rand = random.sample(range(1,sh3.nrows), 15)

			for rx in rand:
				question = {"Question": sh3.row(rx)[1].value,
				"option1": sh3.row(rx)[2].value,
				"option2": sh3.row(rx)[3].value,
				"option3": sh3.row(rx)[4].value,
				"option4": sh3.row(rx)[5].value,
				"correctAnswer": sh3.row(rx)[6].value}
				self.store.append(question)
			return self.store





	
	













