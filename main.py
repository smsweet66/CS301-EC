import pymongo
from flask import Flask
from bson.json_util import dumps

app = Flask(__name__)
db = pymongo.MongoClient('localhost', 27017).db


@app.route('/')
def index():
	return 'Server Works!'


@app.route('/HW1')
def homework1():
	return str(db.CS301.count_documents({}))


@app.route('/HW2')
def homework2():
	cursor = db.CS301.find({'milestones.stoneable.name': 'Zoho'}, {'_id':0,'twitter_username':1,'category_code':1})
	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


@app.route('/HW3')
def homework3():
	cursor = db.CS301.find({}, {'_id':0,'twitter_username':1})
	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


@app.route('/HW4')
def homework4():
	cursor = db.CS301.find({'founded_year': {'$gt': 2000}, 'number_of_employees': {'$gte': 5000}},
	{"_id":0,"name":1,"founded_year":1,"number_of_employees":1,"total_money_raised":1})

	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


# already uses loops, so the same as 4
@app.route('/HW5')
def homework5():
	cursor = ''
	for document in db.CS301.find({'founded_year': {'$gt': 2000}, 'number_of_employees': {'$gte': 5000}},
	{"_id":0,"name":1,"founded_year":1,"number_of_employees":1,"total_money_raised":1}):
		cursor += dumps(document, indent=1) + '\n'

	cursor = cursor.replace('\n', '<br>')
	return cursor


@app.route('/HW6')
def homework6():
	cursor = db.CS301.find({'founded_month': {'$exists':'false'}}, {'_id':1})
	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


@app.route('/HW7')
def homework7():
	return str(db.CS301.count_documents({'funding_rounds.raised_amount': {'$gt':5000000}}))


@app.route('/HW8')
def homework8():
	return str(db.CS301.find({'funding_rounds.raised_amount': {'$gt':5000000}}).count())


@app.route('/HW9')
def homework9():
	cursor = db.CS301.find({'$or': [{'founded_year': {'$gt':2012}}, {'founded_year': {'$lt':1805}}]},
	{'_id':0,'name':1,'founded_year':1}).sort([('founded_year', pymongo.DESCENDING), ('name', pymongo.ASCENDING)])

	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


@app.route('/HW10')
def homework10():
	cursor = db.CS301.find({'founded_year': 1800, 'products.name': {'$exists': 'true'}},
	{'_id':0,'name':1,'homepage_url':1,'number_of_employees':1,'products.name':1})

	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output


@app.route('/HW11')
def homework11():
	cursor = db.CS301.aggregate([{'$match': {'founded_year': 1800, 'products.name': {'$exists': 'true'}}},
	{'$project': {'_id':0,'name':1,'homepage_url':1, 'number_of_employees':1,"products.name":1}}])

	output = dumps(cursor, indent=1)
	output = output.replace('\n', '<br>')
	return output