# sqlalchemy-challenge

This repository contains analysis which was accomplished by working with a 
database using SQLAlchemy, querying data, and creating visualizations using 
Matplotlib.

These are the steps I took to accomplish my overall analysis:

1. Load in all dependencies, libraries and setups

2. Connected to the Database
Used this line of code: 
# creating engine to hawaii.sqlite
engine = create_engine("sqlite:///..//SurfsUp_dude//Resources//hawaii.sqlite", echo=False)

3. Used SQLAlchemy's automap_base() to reflect the tables from the database.

4. Queried data from the database using SQLAlchemy's session and query methods.

5. Used Matplotlib to create visualizations such as histograms and bar plots.

6. Customized plots with titles, labels, legends, and other properties.

7. Lastly, I closed the SQLAlchemy session after finishing the operations.

# Part 2--> Hawaii Weather API

To run this API, you'll need the following dependencies installed in your Python environment:
Flask
SQLAlchemy
NumPy

You can install these dependencies using pip:
pip install Flask SQLAlchemy numpy

Running the Code:
To run the code --> python session.py

This API is built on top of an SQLite database containing weather data. The database schema consists of two tables: measurement and station. The measurement table contains data on precipitation and temperature, while the station table contains information about weather stations.

The API provides the following endpoints:

/api/v1.0/precipitation: Retrieves precipitation data for the last 12 months.
/api/v1.0/stations: Retrieves information about weather stations.
/api/v1.0/tobs: Retrieves temperature observations for the last 12 months from the most active weather station.
/api/v1.0/<start>: Retrieves minimum, average, and maximum temperatures for dates greater than or equal to the specified start date.
/api/v1.0/<start>/<end>: Retrieves minimum, average, and maximum temperatures for dates between the specified start and end dates (inclusive).

To run the API, execute the app.py script:
python app.py

The API will start running on localhost at port 5000 by default. 
You can access the endpoints using a web browser or tools like cURL or Postman.

**Adjust the code based on your specific database schema and requirements.
**Refer to the comments in the code for explanations and details.

--
**If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Make changes and commit (git commit -m 'Add new feature')
Push to the branch (git push origin feature/your-feature)
Create a pull request

--
**Source Data: 

Chat GPT Provider: OpenAI Model Version: GPT-3.5 Training Data: Diverse internet text Training Duration: Training duration was about 2-3 hours @article{openai2023, author = {OpenAI}, title = {ChatGPT: A Language Model by OpenAI}, year = {2023}, url = {https://www.openai.com}, }

Class Videos

BCS app within Slack app

Stackoverflow
