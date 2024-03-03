##
# API code for Company Data
##
# Import dependencies
from pymongo import MongoClient
from bson.json_util import dumps
from flask import Flask
import numpy as np

# Create an instance of MongoClient
mongo = MongoClient(port=27017)

# Assign the FinanceDB database to a variable name
db = mongo['FinanceDB']

# Assign the collection to a variable
companies = db['companies']

# Initialize Flask app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Default Home route
@app.route("/")
def home():
     
     print("request received for home route")
     
     print("""List all available api routes.""")
     
     return (
        f"Available Routes:</br>"
        f"/api/v1.0/company/all</br>"
        f"/api/v1.0/company/ticker/</br>"
        f"/api/v1.0/company/name/</br>"
        f"/api/v1.0/company/sector/</br>"
        f"/api/v1.0/company/subindustry/</br>"
        f"/api/v1.0/company/hqlocation/</br>"
        f"/api/v1.0/company/cik/</br>"
        )

# Route to look up all the companies in the collection
@app.route("/api/v1.0/company/all")
def all_companies():
    result = companies.find({}, {"_id" : 0})
    return dumps(result)

# Route to look up a company by ticker symbol
@app.route("/api/v1.0/company/ticker/<string:ticker>")
def company_by_ticker(ticker: str):
      
    query = {"ticker": ticker.upper()}
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

# Route to look up companies by name
@app.route("/api/v1.0/company/name/<string:name>")
def company_by_name(name: str):
    
    query = {"companyName": { "$regex" : name, "$options" : "i"}}
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

# Route to look up companies by sector
@app.route("/api/v1.0/company/sector/<string:sector>")
def company_by_sector(sector: str):
    
    query = {"sector": { "$regex" : sector, "$options" : "i"}}
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

# Route to look up companies by sub industry
@app.route("/api/v1.0/company/subindustry/<string:subindustry>")
def company_by_subindustry(subindustry: str):
    
    query = {"subIndustry": { "$regex" : subindustry, "$options" : "i"}}
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

# Route to look up companies by HQ Location
@app.route("/api/v1.0/company/hqlocation/<string:hqlocation>")
def company_by_hqlocation(hqlocation: str):
    
    query = {"hqLocation": { "$regex" : hqlocation, "$options" : "i"}}
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

# Route to look up a company by CIK ID
@app.route("/api/v1.0/company/cik/<int:cik>")
def company_by_cik(cik: int):
    
    query = {"cik": cik }
    results = companies.find(query, {"_id" : 0})
    return dumps(results)

if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    mongo.close()
    print("session closed")