# sqlalchemy-challenge

This repository contains analysis which was accomplished by working with a 
database using SQLAlchemy, querying data, and creating visualizations using 
Matplotlib.

These are the steps I took to accomplish my overall analysis:

1. Load in all dependencies, libraries and setups

2. Connected to the Database
Used this line of code:
# creating engine to hawaii.sqlite
engine = create_engine("sqlite:////Users/larry/OneDrive/Desktop/vbu_mod_10/sqlalchemy-challenge/SurfsUp_dude/Resources/hawaii.sqlite", echo=False)

4. Used SQLAlchemy's automap_base() to reflect the tables from the database.

5. Queried data from the database using SQLAlchemy's session and query methods.

6. Used Matplotlib to create visualizations such as histograms and bar plots.

7. Customized plots with titles, labels, legends, and other properties.

8. Lastly, I closed the SQLAlchemy session after finishing the operations.

Running the Code:
To run the code --> python session.py

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
