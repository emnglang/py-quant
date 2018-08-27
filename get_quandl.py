import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

import quandl

mydata = quandl.get("EIA/PET_RWTC_D")
mydata.head()
mydata.plot(figsize=(12,6))

