#################################################
# Flask Routes
#################################################

@app.route("/api/finance/<cik>")
def revenue(company_name):
    session = Session(engine)

    company = company_name.replace(" ", "")
    sel = [company.value, company.qtr, company.year, company.cik, company.recordId]
    results = session.query(*sel).\
        filter(cik = company)
    company_data = list(np.ravel(results))
    return jsonify(company_data)

    session.close()

