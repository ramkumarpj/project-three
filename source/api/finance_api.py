##
# API code for Finance Data
##
# Import dependencies
import numpy as np 
from bson.json_util import dumps
from pymongo import MongoClient
from flask import Flask, request
import json

# Create an instance of MongoClient
mongo = MongoClient(port=27017)


# assign the FinanceDB database to a variable name
db = mongo['FinanceDB']

# assign the collection to a variable
finance = db['finance']

app = Flask(__name__)

# define sample finance query
sample_finance_query = {
    "finance_data_query" : {
        "dataType" : ["NetIncomeLoss"],
        "qtr" : 0,
        "year" : 2023,
        "cik" : [1551152, 4977]
    } 
}

#################################################
# Flask Routes
#################################################

# Home Route
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:</br>"
        f"/api/v1.0/finance/query</br>"
        f"Query String in POST Body : {sample_finance_query}"
    )


# Route to query finance data
@app.route("/api/v1.0/finance/query", methods=["POST"])
def finance_query():
    
    # Retrieve query provided in the body of the POST request
    finance_query = json.loads(request.data)
    print(finance_query)
    
    # Define query dictionary
    query = {}
    
    # Configure query variable according to the input query received 
    if 'dataType' in finance_query['finance_data_query']:
        query['dataType'] = { "$in" : finance_query['finance_data_query']['dataType'] }
    
    if 'qtr' in finance_query['finance_data_query']:
        query['qtr'] = finance_query['finance_data_query']['qtr']
    
    if 'year' in finance_query['finance_data_query']:
        query['year'] = finance_query['finance_data_query']['year']
    
    if 'cik' in finance_query['finance_data_query']:
        query['cik'] = { "$in" : finance_query['finance_data_query']['cik'] }
        
    print(query)
    
    # Query the database
    results = finance.find(query, {"_id" : 0})
    
    return dumps(results)
        

    
if __name__ == '__main__':
    app.run(debug=True, port=5001)

@app.teardown_appcontext
def shutdown_session(exception=None):
    mongo.close()
    print("session closed")