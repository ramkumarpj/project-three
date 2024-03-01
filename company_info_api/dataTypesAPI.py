# Import dependencies
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

# Create an instance of MongoClient
mongo = MongoClient(port=27017)

#################################################
# Database Setup
#################################################
engine = create_engine("json://data/output/finance_data.json")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with = engine)

# reflect the tables
print(Base.classes.keys())

finance = Base.classes.finance
companies = Base.classes.companies

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/dataTypes")
def dataType():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(finance.dataType).unique()

    session.close()

    # Convert list of tuples into normal list
    all_dataTypes = list(np.ravel(results))

    return jsonify(all_dataTypes)


@app.route("/api/v1.0/SalesRevenueGoodsNet")
def SRGN():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'SalesRevenueGoodsNet').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/SalesRevenueServicesNet")
def SRSN():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'SalesRevenueServicesNet').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/RevenueFromContractWithCustomerIncludingAssessedTax")
def RevenueFromContract():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'RevenueFromContractWithCustomerIncludingAssessedTax').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/GrossProfit")
def GrossProfit():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'GrossProfit').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/OperatingIncomeLoss")
def OperatingIncomeLoss():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'OperatingIncomeLoss').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/NetIncomeLoss")
def NetIncomeLoss():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'NetIncomeLoss').all()

    session.close()
    
    return jsonify(results)


@app.route("/api/v1.0/ResearchAndDevelopmentExpense")
def ResearchAndDevelopmentExpense():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'ResearchAndDevelopmentExpense').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/ShareBasedCompensation")
def ShareBasedCompensation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'ShareBasedCompensation').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/Depreciation")
def Depreciation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'Depreciation').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/AllocatedShareBasedCompensationExpense")
def ASBCE():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'AllocatedShareBasedCompensationExpense').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/CostsAndExpenses")
def CostsAndExpenses():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'CostsAndExpenses').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/GeneralAndAdministrativeExpense")
def GeneralAndAdministrativeExpense():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'GeneralAndAdministrativeExpense').all()

    session.close()
    
    return jsonify(results)


@app.route("/api/v1.0/InterestExpense")
def InterestExpense():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'InterestExpense').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/LeaseAndRentalExpense")
def LeaseAndRentalExpense():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'LeaseAndRentalExpense').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/MarketingAndAdvertisingExpense")
def MarketingAndAdvertisingExpense():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'MarketingAndAdvertisingExpense').all()

    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/OtherAccruedLiabilitiesCurrent")
def OtherAccruedLiabilitiesCurrent():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'OtherAccruedLiabilitiesCurrent').all()

    session.close()
    
    return jsonify(results)


@app.route("/api/v1.0/EntityCommonStockSharesOutstanding")
def EntityCommonStockSharesOutstanding():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'EntityCommonStockSharesOutstanding').all()

    session.close()
    
    return jsonify(results)


@app.route("/api/v1.0/EntityPublicFloat")
def EntityPublicFloat():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all SalesRevenueGoodsNet
    results = session.query(all_dataTypes = 'EntityPublicFloat').all()

    session.close()
    
    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()
    print("session closed")