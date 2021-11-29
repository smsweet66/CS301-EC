from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
db = MongoClient('localhost', 27017).db


@app.route('/')
def index():
	return 'Server Works!'


@app.route('/HW1')
def homework1():
	return str(db.CS301.count_documents({}))


@app.route('/HW2')
def homework2():
	output = ''
	for document in db.CS301.find({"milestones.stoneable.name": "Zoho"}, {"_id":0,"twitter_username":1,"category_code":1}):
		output += str(document) + '<br>'

	return output


@app.route('/HW3')
def homework3():
	output = ''
	for document in db.CS301.find({}, {"_id":0,"twitter_username":1}):
		output += str(document) + '<br>'

	return output

@app.route('/HW4')
def homework4():
	output = ''
	for document in db.CS301.find({'founded_year': {'$gt': 2000}, 'number_of_employees': {'$gte': 5000}},
	{"_id":0,"name":1,"founded_year":1,"number_of_employees":1,"total_money_raised":1}):
		output += str(document) + '<br>'

	return output



#already uses loops, so the same as 4
@app.route('/HW5')
def homework5():
	return homework4