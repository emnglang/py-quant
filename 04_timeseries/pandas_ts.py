
import pandas as pd
import matplotlib.pyplot as plt

mcdon = pd.read_csv('mcdonalds.csv')
mcdon['Adj. Close'].plot()
plt.show()

wmart = pd.read_csv('walmart.csv')
wmart['Adj Close'].plot()
plt.show()

