import pymongo
from flask import Flask, redirect
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
	cursor = db.CS301.find({'milestones.stoneable.name': 'Zoho'}, {'_id': 0, 'twitter_username': 1, 'category_code': 1})
	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW3')
def homework3():
	cursor = db.CS301.find({}, {'_id': 0, 'twitter_username': 1})
	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW4')
def homework4():
	cursor = db.CS301.find({'founded_year': {'$gt': 2000}, 'number_of_employees': {'$gte': 5000}},
	{"_id": 0, "name": 1, "founded_year": 1, "number_of_employees": 1, "total_money_raised": 1})

	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW6')
def homework6():
	cursor = db.CS301.find({'founded_month': {'$exists': 'false'}}, {'_id': 1})
	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW7')
def homework7():
	return str(db.CS301.count_documents({'funding_rounds.raised_amount': {'$gt': 5000000}}))


@app.route('/HW9')
def homework9():
	cursor = db.CS301.find({'$or': [{'founded_year': {'$gt': 2012}}, {'founded_year': {'$lt': 1805}}]},
	{'_id': 0, 'name': 1, 'founded_year': 1}).sort(
		[('founded_year', pymongo.DESCENDING), ('name', pymongo.ASCENDING)])

	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW10')
def homework10():
	cursor = db.CS301.find({'founded_year': 1800, 'products.name': {'$exists': 'true'}},
	{'_id': 0, 'name': 1, 'homepage_url': 1, 'number_of_employees': 1, 'products.name': 1})

	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/HW12')
def homework12():
	return str(db.CS301.count_documents({'screenshots.attribution': None}))


@app.route('/HW13')
def homework13():
	cursor = db.CS301.find({}, {'_id': 0, 'number_of_employees': 1}).sort(
		[('number_of_employees', pymongo.DESCENDING)]).limit(1)

	return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/company/<companyName>')
def getCompanyInfo(companyName):
	if db.CS301.count_documents({'name': companyName}) < 1:
		return f'No company with the name \"{companyName}\" exists'
	else:
		cursor = db.CS301.find({'name': companyName}).limit(1)
		return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/list_companies_by_year/<yearFounded>')
def listCompaniesByYear(yearFounded):
	if len(yearFounded) != 4:
		return 'Year must be a four digit number'
	elif db.CS301.count_documents({'founded_year': int(yearFounded)}) < 1:
		return f'No companies founded in the year {yearFounded}'
	else:
		cursor = db.CS301.find({'founded_year': int(yearFounded)})
		return dumps(cursor, indent=2).replace('\n', '<br>')


@app.route('/count_companies_by_year/<yearFounded>')
def countCompaniesByYear(yearFounded):
	if len(yearFounded) != 4:
		return 'Year must be a four digit number'
	else:
		count = db.CS301.count_documents({'founded_year': int(yearFounded)})
		return f'There were {count} companies founded in {yearFounded}'


@app.route('/crunchbase/redirect/<companyName>')
def crunchbaseRedirect(companyName):
	company = db.CS301.find_one({'name': companyName})
	if company:
		return redirect(company['crunchbase_url'])
	else:
		return f'There is no company by the name {companyName}'