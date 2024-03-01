from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/FinanceDB'
mongo = PyMongo(app)

@app.route('/api/finance/<company_data>', methods=['GET'])
def get_finance_data(company_data):
    # Assuming your collection is named 'company_data'
    company_data_collection = mongo.db.company_data

    # Query MongoDB for the finance data of the specified company
    company_data = company_data_collection.find_one({'companyName': company_data})

    if company_data:
        # Convert MongoDB ObjectId to str for JSON serialization
        company_data['cik'] = str(company_data['cik'])
        return jsonify({'status': 'success', 'data': company_data})
    else:
        return jsonify({'status': 'error', 'message': 'Company not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
