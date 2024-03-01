#################################################
# Flask Routes
#################################################

@app.route("/api/finance/<dataType>")
def data(cik):
    session = Session(engine)

    data_type = dataType.replace(" ", "")
    sel = data.recordId, data.cik, data.value, data.qtr, data.year
    results = session.query(*sel).\
        filter(dataType = data_type)
    dataTypeList = list(np.ravel(results))
    return jsonify(dataTypeList)

    session.close()
about:blank#blocked