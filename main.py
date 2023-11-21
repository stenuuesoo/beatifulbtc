import requests
import pandas as pd

def fetch_bitcoin_data(api_key):
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    # Process the JSON data into a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Digital Currency Daily)'], orient='index')
    df = df.rename(columns={
        '1a. open (USD)': 'Open',
        '2a. high (USD)': 'High',
        '3a. low (USD)': 'Low',
        '4a. close (USD)': 'Close',
        '5. volume': 'Volume'
    }).astype(float)

    df.index = pd.to_datetime(df.index)
    return df

if __name__ == '__main__':
    # Replace 'your_api_key' with your actual Alpha Vantage API key
    api_key = 'N8IN2LVTV9ZJQ71V'
    bitcoin_df = fetch_bitcoin_data(api_key)
    print(bitcoin_df.head())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
