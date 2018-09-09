
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('walmart.csv')

df['Close: 20 Day Mean'] = df['Close'].rolling(20).mean()

df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(20).std())
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(20).std())

df[['Close', 'Close: 20 Day Mean', 'Upper', 'Lower']].plot(figsize=(16,6))

plt.show()


