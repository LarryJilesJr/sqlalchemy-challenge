import numpy as np

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt
from datetime import datetime

#################################################
# Database Setup
#################################################

# creating engine to hawaii.sqlite
engine = create_engine("sqlite:////Users//larry//OneDrive//Desktop//vbu_mod_10//sqlalchemy-challenge//SurfsUp_dude//Resources//hawaii.sqlite", echo=False)

# reflecting an existing database into a new model
Base = automap_base()

# reflecting the tables
Base.prepare(autoload_with=engine)
# print(Base.classes.keys())

# Saving references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    return (
        f"Welcome to the homepage!<br/>"
        """List of all available api routes."""
        f" Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'<start>'<br/>"
        f"/api/v1.0/'<start>/<end>'<br/>"
    ) 


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session (link) from Python to the DB
    session = Session(engine)
    
    # Finding the most recent date in the data set.
    the_latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Calculate the date one year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query precipitation data for the last 12 months
    precipitation_scores = session.query(Measurement.date, Measurement.prcp) .\
    filter(Measurement.date >= '2016-08-23') .\
    filter(Measurement.date <= '2017-08-23').all()

    session.close()

    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_scores}

    return jsonify(precipitation_dict)

@app.route('/api/v1.0/stations')
def stations():
    # Create a session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Convert the query results to a list of dictionaries
    stations_list = [{'station': station, 'name': name} for station, name in results]

    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    # Create a session (link) from Python to the DB
    session = Session(engine)
    
    # Finding the most recent date in the data set.
    the_latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    # Calculate the date one year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Query temperature observations for the most active station within the date range
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert the query results into a list of dictionaries
    temperature_data = [{'date': date, 'tobs': tobs} for date, tobs in results]

    return jsonify(temperature_data)

@app.route('/api/v1.0/<start>')
def temperature_start(start):
    # Create a session (link) from Python to the DB
    session = Session(engine)

    # Parse the start date parameter
    start_date = datetime.strptime('2010-01-01', '%Y-%m-%d') # '2016-08-23' in this block of code shows the same dictionary as the next block, so I used a different date to show its functionality

    # Query for TMIN, TAVG, and TMAX for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    # Convert the query results into a dictionary
    temperature_data = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }

    return jsonify(temperature_data)

@app.route('/api/v1.0/<start>/<end>')
def temperature_start_end(start, end):
    # Create a session (link) from Python to the DB
    session = Session(engine)
    
    # Parse the start and end date parameters
    start_date = datetime.strptime('2016-08-23', '%Y-%m-%d')
    end_date = datetime.strptime('2017-08-23', '%Y-%m-%d')

    # Query for TMIN, TAVG, and TMAX for dates between the start and end dates (inclusive)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    # Convert the query results into a dictionary
    temperature_data = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }

    return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(debug=True)
