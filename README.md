# Disaster Response Pipeline Project

[GitHub repo](https://github.com/managucam/pythonProject2)

### Project summary
The project contains an ETL (Extract, Transform, Load) data pipeline and a machine learning pipeline categorizes these events so that messages are sent to an appropriate disaster relief agency.
Lastly, it includes a web app where emergency workers can input a new message and get classification results in several categories.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/messages.csv data/categories.csv data/data1.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/data1.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage
