import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

tesla = pd.read_csv('Tesla_Stock.csv')
ford = pd.read_csv('Ford_Stock.csv')
gm = pd.read_csv('GM_Stock.csv')

tesla['Open'].plot()
ford['Open'].plot()
gm['Open'].plot()

plt.show()
