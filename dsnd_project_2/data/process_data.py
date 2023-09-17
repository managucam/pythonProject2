"""In a Python script, process_data.py, write a data cleaning pipeline that:

Loads the messages and categories datasets
Merges the two datasets
Cleans the data
Stores it in a SQLite database"""

import pandas as pd
from sqlalchemy import create_engine

# load messages dataset
messages = pd.read_csv('messages.csv').set_index('id')
# messages.head()

# load categories dataset
categories = pd.read_csv('categories.csv').set_index('id')
# categories.head()

# merge datasets
df = messages.merge(categories, left_index=True, right_index=True)
# df.head()

# create a dataframe of the 36 individual category columns
categories = df['categories'].str.split(';', expand=True)
# categories.head()

# select the first row of the categories dataframe
row = categories.iloc[0,:]
# print(row)
# use this row to extract a list of new column names for categories.
# one way is to apply a lambda function that takes everything
# up to the second to last character of each string with slicing
category_colnames = row.str.split('-', expand=True)[0].values
# print(category_colnames)

# rename the columns of `categories`
categories.columns = category_colnames
# categories.head()

for column in categories:
    # set each value to be the last character of the string
    categories[column] = categories[column].str.slice(start=-1)

    # convert column from string to numeric
    categories[column] = categories[column].astype(int)
# categories.head()

# drop the original categories column from `df`
df.drop(['categories'], axis=1, inplace=True)
# df.head()

# concatenate the original dataframe with the new `categories` dataframe
df = df.merge(categories, left_index=True, right_index=True)
# df.head()

# check number of duplicates
duplicates = df[df.duplicated()]
# print(duplicates)

# drop duplicates
df = df.drop_duplicates()
# df.describe()

# check number of duplicates
duplicatesCheck = df[df.duplicated()]
# print(duplicatesCheck)

engine = create_engine('sqlite:///data1.db')
df.to_sql('data1', engine, index=False)

import sys


def load_data(messages_filepath, categories_filepath):
    pass


def clean_data(df):
    pass


def save_data(df, database_filename):
    pass


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories ' \
              'datasets as the first and second argument respectively, as ' \
              'well as the filepath of the database to save the cleaned data ' \
              'to as the third argument. \n\nExample: python process_data.py ' \
              'disaster_messages.csv disaster_categories.csv ' \
              'DisasterResponse.db')


if __name__ == '__main__':
    main()