import config
import robin_stocks.robinhood as r
from pprint import pprint

# Authenticate 
r.login(config.USERNAME, config.PASSWORD)

symbol = ['AAPL']
expirationDate = '2022-12-16'

optionData = r.options.find_options_by_expiration(inputSymbols=symbol, expirationDate=expirationDate, optionType='put')

for item in optionData:
    pprint(item)