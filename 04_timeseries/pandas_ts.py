
import pandas as pd
import matplotlib.pyplot as plt

mcdon = pd.read_csv('mcdonalds.csv')
mcdon['Adj. Close'].plot()
plt.show()

