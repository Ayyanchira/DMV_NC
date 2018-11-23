
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


f = open( 'data.json', 'w')
book = xlrd.open_workbook('Spl_1.xlsx')
sh1 = book.sheet_by_index(0)
sh2 = book.sheet_by_index(1)
sh3 = book.sheet_by_index(2)

store = []
questions = []

for rx in range(1,sh1.nrows):	
	question = {"Question": sh1.row(rx)[0].value,
	"option1": sh1.row(rx)[1].value,
	"option2": sh1.row(rx)[2].value,
	"option3": sh1.row(rx)[3].value,
	"option4": sh1.row(rx)[4].value,
	"correctAnswer": sh1.row(rx)[5].value}
	store.append(question)

easy = json.dumps(store, indent=4)
f.write(easy)
store = []

for rx in range(1,sh2.nrows):	
	question = {"Question": sh2.row(rx)[0].value,
	"option1": sh2.row(rx)[1].value,
	"option2": sh2.row(rx)[2].value,
	"option3": sh2.row(rx)[3].value,
	"option4": sh2.row(rx)[4].value,
	"correctAnswer": sh2.row(rx)[5].value}
	store.append(question)

medium = json.dumps(store, indent=4)
f.write(medium)
store = []

for rx in range(1,sh3.nrows):	
	question = {"Question": sh3.row(rx)[0].value,
	"option1": sh3.row(rx)[1].value,
	"option2": sh3.row(rx)[2].value,
	"option3": sh3.row(rx)[3].value,
	"option4": sh3.row(rx)[4].value,
	"correctAnswer": sh3.row(rx)[5].value}
	store.append(question)

hard = json.dumps(store, indent=4)
f.write(hard)
	
	













