# Import dependencies
import numpy as np 
from bson.json_util import dumps
from pymongo import MongoClient
from flask import Flask, jsonify

# Create an instance of MongoClient
mongo = MongoClient(port=27017)


# assign the uk_food database to a variable name
db = mongo['FinanceDB']

# assign the collection to a variable
finance = db['finance']
companies = db['companies']

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:</br>"
        f"/api/v1.0/SalesRevenueGoodsNet</br>"
        f"/api/v1.0/SalesRevenueServicesNet</br>"
        f"/api/v1.0/RevenueFromContractWithCustomerIncludingAssessedTax</br>"
        f"/api/v1.0/GrossProfit</br>"
        f"/api/v1.0/OperatingIncomeLoss</br>"
        f"/api/v1.0/NetIncomeLoss</br>"
        f"/api/v1.0/ResearchAndDevelopmentExpense</br>"
        f"/api/v1.0/ShareBasedCompensation</br>"
        f"/api/v1.0/Depreciation</br>"
        f"/api/v1.0/AllocatedShareBasedCompensationExpense</br>"
        f"/api/v1.0/CostsAndExpenses</br>"
        f"/api/v1.0/GeneralAndAdministrativeExpense</br>"
        f"/api/v1.0/InterestExpense</br>"
        f"/api/v1.0/LeaseAndRentalExpense</br>"
        f"/api/v1.0/MarketingAndAdvertisingExpense</br>"
        f"/api/v1.0/OtherAccruedLiabilitiesCurrent</br>"
        f"/api/v1.0/EntityCommonStockSharesOutstanding</br>"
        f"/api/v1.0/EntityPublicFloat</br>"
    )

@app.route("/api/v1.0/SalesRevenueGoodsNet")
def SRGN():
    # Query all SalesRevenueGoodsNet datatypes
    query = {"dataType" : "SalesRevenueGoodsNet"}
    results = finance.find(query)
    all_results = dumps((results))
    return jsonify(all_results)

    

@app.route("/api/v1.0/SalesRevenueServicesNet")
def SRSN():
   # Query all SalesRevenueServiesNet datatypes
    query = {'dataType' : 'SalesRevenueServicesNet'}
    results = finance.find(query)
    all_results = dumps((results))
    return jsonify(all_results)

@app.route("/api/v1.0/RevenueFromContractWithCustomerIncludingAssessedTax")
def RevenueFromContract():
    # Query all RevenueFromContractWithCustomerIncludingAssessedTax datatypes
    query = {'dataType' : 'RevenueFromContractWithCustomerIncludingAssessedTax'}
    results = finance.find(query)
    all_results = dumps((results))
    return jsonify(all_results)

@app.route("/api/v1.0/GrossProfit")
def GrossProfit():
    # Query all GrossProfit datatypes
    query = {'dataType': 'GrossProfit'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/OperatingIncomeLoss")
def OperatingIncomeLoss():
    # Query all OperatingIncomeLoss datatypes
    query = {'dataType' : 'OperatingIncomeLoss'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/NetIncomeLoss")
def NetIncomeLoss():
    # Query all NetIncomeLoss datatypes
    query = {'dataType' : 'NetIncomeLoss'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)


@app.route("/api/v1.0/ResearchAndDevelopmentExpense")
def ResearchAndDevelopmentExpense():
    # Query all ResearchAndDevelopmentExpense datatypes
    query = {'dataType' : 'ResearchAndDevelopmentExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/ShareBasedCompensation")
def ShareBasedCompensation():
    # Query all ShareBasedCompensation datatypes
    query = {'dataType' : 'ShareBasedCompensation'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/Depreciation")
def Depreciation():
    # Query all Depreciation datatypes
    query = {'dataType' : 'Depreciation'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/AllocatedShareBasedCompensationExpense")
def ASBCE():
    # Query all AllocatedShareBasedCompensationExpense datatypes
    query = {'dataType' : 'AllocatedShareBasedCompensationExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/CostsAndExpenses")
def CostsAndExpenses():
    # Query all CostsAndExpenses datatypes
    query = {'dataType' : 'CostsAndExpenses'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/GeneralAndAdministrativeExpense")
def GeneralAndAdministrativeExpense():
    # Query all GeneralAndAdminstrativeExpense datatypes
    query = {'dataType' : 'GeneralAndAdministrativeExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)


@app.route("/api/v1.0/InterestExpense")
def InterestExpense():
   # Query all InterestExpense datatypes
    query = {'dataType ': 'InterestExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/LeaseAndRentalExpense")
def LeaseAndRentalExpense():
    # Query all LeaseAndRentalExpense datatypes
    query = {'dataType' : 'LeaseAndRentalExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/MarketingAndAdvertisingExpense")
def MarketingAndAdvertisingExpense():
    # Query all MarkertingAndAdvertisingExpense datatypes
    query = {'dataType' : 'MarketingAndAdvertisingExpense'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)

@app.route("/api/v1.0/OtherAccruedLiabilitiesCurrent")
def OtherAccruedLiabilitiesCurrent():
    # Query all OtherAccruedLiabilitiesCurrent datatypes
    query = {'dataType' : 'OtherAccruedLiabilitiesCurrent'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)


@app.route("/api/v1.0/EntityCommonStockSharesOutstanding")
def EntityCommonStockSharesOutstanding():
    # Query all EntityCommonStockSharesOutstanding datatypes
    query = {'dataType' : 'EntityCommonStockSharesOutstanding'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)


@app.route("/api/v1.0/EntityPublicFloat")
def EntityPublicFloat():
    # Query all EntityPublicFloat datatypes
    query = {'dataType' : 'EntityPublicFloat'}
    results = finance.find(query)
    all_results = dumps(results)
    return jsonify(all_results)


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("session closed")
    
if __name__ == '__main__':
    app.run(debug=True)