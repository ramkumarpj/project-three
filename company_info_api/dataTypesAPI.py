# Import dependencies
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

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

@app.route("/api/v1.0/dataTypes")
def dataType():
    types = finance.dataType.unique()

    # Convert list of tuples into normal list
    all_dataTypes = list(np.ravel(types))

    return jsonify(all_dataTypes)


@app.route("/api/v1.0/SalesRevenueGoodsNet")
def SRGN():
    # Query all SalesRevenueGoodsNet datatypes
    query = {"dataType" : 'SalesRevenueGoodsNet'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/SalesRevenueServicesNet")
def SRSN():
   # Query all SalesRevenueServiesNet datatypes
    query = {"dataType" : 'SalesRevenueServicesNet'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/RevenueFromContractWithCustomerIncludingAssessedTax")
def RevenueFromContract():
    # Query all RevenueFromContractWithCustomerIncludingAssessedTax datatypes
    query = {"dataType" : 'RevenueFromContractWithCustomerIncludingAssessedTax'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/GrossProfit")
def GrossProfit():
    # Query all GrossProfit datatypes
    query = {"dataType" : 'GrossProfit'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/OperatingIncomeLoss")
def OperatingIncomeLoss():
    # Query all OperatingIncomeLoss datatypes
    query = {"dataType" : 'OperatingIncomeLoss'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/NetIncomeLoss")
def NetIncomeLoss():
    # Query all NetIncomeLoss datatypes
    query = {"dataType" : 'NetIncomeLoss'}

    results = finance.find(query)
    
    return jsonify(results)


@app.route("/api/v1.0/ResearchAndDevelopmentExpense")
def ResearchAndDevelopmentExpense():
    # Query all ResearchAndDevelopmentExpense datatypes
    query = {"dataType" : 'ResearchAndDevelopmentExpense'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/ShareBasedCompensation")
def ShareBasedCompensation():
    # Query all ShareBasedCompensation datatypes
    query = {"dataType" : 'ShareBasedCompensation'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/Depreciation")
def Depreciation():
    # Query all Depreciation datatypes
    query = {"dataType" : 'Depreciation'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/AllocatedShareBasedCompensationExpense")
def ASBCE():
    # Query all AllocatedShareBasedCompensationExpense datatypes
    query = {"dataType" : 'AllocatedShareBasedCompensationExpense'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/CostsAndExpenses")
def CostsAndExpenses():
    # Query all CostsAndExpenses datatypes
    query = {"dataType" : 'CostsAndExpenses'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/GeneralAndAdministrativeExpense")
def GeneralAndAdministrativeExpense():
    # Query all GeneralAndAdminstrativeExpense datatypes
    query = {"dataType" : 'GeneralAndAdministrativeExpense'}

    results = finance.find(query)
    
    return jsonify(results)


@app.route("/api/v1.0/InterestExpense")
def InterestExpense():
   # Query all InterestExpense datatypes
    query = {"dataType" : 'InterestExpense'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/LeaseAndRentalExpense")
def LeaseAndRentalExpense():
    # Query all LeaseAndRentalExpense datatypes
    query = {"dataType" : 'LeaseAndRentalExpense'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/MarketingAndAdvertisingExpense")
def MarketingAndAdvertisingExpense():
    # Query all MarkertingAndAdvertisingExpense datatypes
    query = {"dataType" : 'MarketingAndAdvertisingExpense'}

    results = finance.find(query)
    
    return jsonify(results)

@app.route("/api/v1.0/OtherAccruedLiabilitiesCurrent")
def OtherAccruedLiabilitiesCurrent():
    # Query all OtherAccruedLiabilitiesCurrent datatypes
    query = {"dataType" : 'OtherAccruedLiabilitiesCurrent'}

    results = finance.find(query)
    
    return jsonify(results)


@app.route("/api/v1.0/EntityCommonStockSharesOutstanding")
def EntityCommonStockSharesOutstanding():
    # Query all EntityCommonStockSharesOutstanding datatypes
    query = {"dataType" : 'EntityCommonStockSharesOutstanding'}

    results = finance.find(query)
    
    return jsonify(results)


@app.route("/api/v1.0/EntityPublicFloat")
def EntityPublicFloat():
    # Query all EntityPublicFloat datatypes
    query = {"dataType" : 'EntityPublicFloat'}

    results = finance.find(query)
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()
    print("session closed")