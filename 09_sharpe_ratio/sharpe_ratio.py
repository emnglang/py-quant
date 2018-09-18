
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('AAPL_CLOSE', index_col = 'Date', parse_dates = True)
cisco = pd.read_csv('CISCO_CLOSE', index_col = 'Date', parse_dates = True)
ibm = pd.read_csv('IBM_CLOSE', index_col = 'Date', parse_dates = True)
amzn = pd.read_csv('AMZN_CLOSE', index_col = 'Date', parse_dates = True)

stocks = pd.concat([aapl, cisco, ibm, amzn], axis=1)
stocks.columns = ['aapl', 'cisco', 'ibm', 'amzn']

log_ret = np.log(stocks/stocks.shift(1))

np.random.seed(101)
weights = np.array(np.random.random(4))

# expected return
print('Expected Return')
exp_ret = np.sum((log_ret.mean() * weights) * 252)
print(exp_ret)

# expectec vol
print('Expected Vol')
exp_vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
print(exp_vol)

# sharpe ratio
print('Sharpe Ratio')
SR = exp_ret/exp_vol
print(SR)


