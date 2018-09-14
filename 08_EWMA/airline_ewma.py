
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('passengers.csv',index_col="Month")
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)

airline['6-month-SMA']=airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA']=airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot()

airline['EWMA12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline[['Thousands of Passengers','EWMA12']].plot()

plt.show()
