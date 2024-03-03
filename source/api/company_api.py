# Import dependencies
from pymongo import MongoClient
from flask import Flask, jsonify
import numpy as np

# Create an instance of MongoClient
mongo = MongoClient(port=27017)

# Assign the FinanceDB database to a variable name
db = mongo['FinanceDB']

# Assign the collection to a variable
finance = db['finance']
companies = db['companies']

# Initialize Flask app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/company_name")
def company_name():
    types = companies.distinct("companyName")

    return jsonify(types)

@app.route("/api/v1.0/Baker_Hughes_Holdings_LLC")
def bhh():
    # Query all Baker Hughes Holding LLC data
    query = {"companyName": 'Baker Hughes Holdings LLC'}

    results = companies.find(query)

    return jsonify(list(results))

@app.route("/api/v1.0/Alphabet_Inc")
def ai():
    # Query all Alphabet Inc. data
    query = {"companyName": 'Alphabet Inc.'}

    results = companies.find(query)

    return jsonify(list(results))

@app.route("/api/v1.0/Kraft_Heinz_Co")
def khc():
    # Query all Kraft Heinz Co data
    query = {"companyName": 'Kraft Heinz Co'}

    results = companies.find(query)

    return jsonify(list(results))

if __name__ == '__main__':
    app.run(debug=True)
