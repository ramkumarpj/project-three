# Import dependencies
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

# Create an instance of MongoClient
mongo = MongoClient(port=27017)

# Assign the FinanceDB database to a variable name
db = mongo['FinanceDB']

# Assign the collection to a variable
finance = db['finance']
companies = db['companies']

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/companyName")
def companyName():
    types = companies.companyName.unique()

    all_companyName = list(np.ravel(types))

    return jsonify(all_companyName)

@app.route("/api/v1.0/Baker Hughes Holdings LLC")
def BHH():
    #Query all Baker Hughes Holding LLC data
    query = {"companyName": 'Baker Hughes Holdings LLC'}

    results = companies.find(query)

    return jsonify(results)

@app.route("/api/v1.0/Alphabet Inc.")
def AI():
    #Query all Alphabet Inc. data
    query = {"companyName": 'Alphabet Inc.'}

    results = companies.find(query)

    return jsonify(results)

@app.route("/api/v1.0/Kraft Heinz Co")
def KHC():
    #Query all Kraft Heinz Co data
    query = {"companyName": 'Kraft Heinz Co'}

    results = companies.find(query)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()
    print("session closed")