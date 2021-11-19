from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)


@app.route('/')
def index():
	return 'Server Works!'


@app.route('/count')
def get_count():
	return str(client.db['CS301'].count_documents({}))