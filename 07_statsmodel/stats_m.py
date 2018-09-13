import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])
df['trend'] = gdp_trend
df[['realgdp','trend']].plot()

plt.show()
