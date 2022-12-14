import config
import robin_stocks.robinhood as r
from pprint import pprint

# Authenticate 
r.login(config.USERNAME, config.PASSWORD)

symbol = ['AAPL']
expirationDate = '2022-12-16'
strike = 145


# # Option Data by Expiration
# optionData = r.options.find_options_by_expiration(inputSymbols=symbol, expirationDate=expirationDate, optionType='put')

# for option in optionData:
#     if float(option['ask_price']) < 3.00:
#         print('Strike Price: {}, Bid: {}, Ask: {}, High: {}, Low: {}'.format(
#             option['strike_price'], option['bid_price'], option['ask_price'], option['high_price'], option['low_price']
#         ))


# # Option Data by Strike Price 
# strike_145 = r.options.find_options_by_strike(symbol, strike, optionType='put')

# strike_145 = sorted(strike_145, key=lambda x: x['expiration_date'])

# for option in strike_145:
#     print('Expiration Date: {}, Bid: {}, Ask: {}, High: {}, Low: {}'.format(
#         option['expiration_date'], option['bid_price'], option['ask_price'], option['high_price'], option['low_price']
#     ))

put = r.options.get_option_instrument_data('AAPL', expirationDate, strike, optionType='put')
pprint(put)
