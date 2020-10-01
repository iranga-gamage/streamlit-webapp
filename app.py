from google.cloud import bigquery
import pandas as pd
import streamlit as st
import numpy as np


"# Streamlit Demo1"


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def load_bigquery_data():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
    """
    query_job = client.query(query) 

    names = []
    counts = []

    for row in query_job:
        names.append(row[0])
        counts.append(row["total_people"])

    df = pd.DataFrame( { "Name" : pd.Series(names), "Count": pd.Series(counts)})
    return df

def main():
    
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text('Loading data...done!')

    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

    st.bar_chart(hist_values)

    df = load_bigquery_data()

    df

if __name__ == "__main__":
    main()
