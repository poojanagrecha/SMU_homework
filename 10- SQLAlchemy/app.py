import datetime as dt
import numpy as np
import pandas as pd
import json

#My SQL Class I wrote
from sqlHelper import SQLHelper
from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

sqlHelper = SQLHelper()

@app.route("/api/v1.0/precipitation")
def totalPrecipitation():
    data = sqlHelper.TotalPrecipitation()
    data = data.to_json(orient='records')
    data = json.loads(data)
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def stations(): 
    data = sqlHelper.TotalStations()
    return(jsonify(json.loads(data.to_json(orient='records')))) 

@app.route("/api/v1.0/tobs")
def stations_temp(temperature): 
    data = sqlHelper.activeTemp()
    return(jsonify(json.loads(data.to_json(orient='records')))) 

@app.route("/api/v1.0/temperature/<start>")
def get_temp_for_date(start): 
    data = sqlHelper.getTempInfoForDate(start)
    return(jsonify(json.loads(data.to_json(orient='records')))) 

@app.route("/api/v1.0/temperature/<start>/<end>")
def get_temp_for_date_range(start, end): 
    data = sqlHelper.getTempInfoForDateRange(start, end)
    return(jsonify(json.loads(data.to_json(orient='records')))) 

@app.route("/")
def home():
    return (
        f"Hawaii Climate Analysis!<br/>"

        f"""
        <ul>
            <li><a target="_blank" href='/api/v1.0/precipitation'>Total Precipitation</a></li>
            <li><a target="_blank" href='/api/v1.0/stations'>All Stations</a></li>
            <li><a target="_blank" href='/api/v1.0/tobs'>Temperature for Most Active Station</a></li>
            <li><a target="_blank" href='/api/v1.0/temperature/2017-08-23'>Temperature for Date</a></li>
            <li><a target="_blank" href='/api/v1.0/temperature/2016-09-23/2017-05-23'>Temperature for Date Range</a></li>
        </ul>
        """
    )


#################################################
# Flask Run
#################################################
if __name__ == "__main__":
    app.run(debug=True)
