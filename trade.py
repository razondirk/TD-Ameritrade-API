from tda import auth, client
import json
import config
import os

def run():
    os.chdir('C:/Users/razon/OneDrive/Documents/Vs/TDAmeritrade/TDAmeritrade/TDAmeritrade')
    try:
        c = auth.client_from_token_file(config.token_path, config.api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome(executable_path='C:/Users/razon/OneDrive/Documents/Vs/TDAmeritrade/TDAmeritrade/TDAmeritrade/chromedriver') as driver:
            c = auth.client_from_login_flow(
                driver, config.api_key, config.redirect_uri, config.token_path)

    #r = c.get_price_history('F',
    #        period_type=client.Client.PriceHistory.PeriodType.DAY,
    #        period=client.Client.PriceHistory.Period.FIVE_DAYS,
    #        frequency_type=client.Client.PriceHistory.FrequencyType.MINUTE,
    #        frequency=client.Client.PriceHistory.Frequency.EVERY_MINUTE)
    #assert r.ok, r.raise_for_status()
    #print(json.dumps(r.json(), indent=4))

    response = c.get_quote('F')
    print(response.json())

if __name__ == "__main__":
    run()