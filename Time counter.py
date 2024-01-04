import requests
import pandas as pd
import numpy as np
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(r)
r = r.split()
df = pd.DataFrame(r)
print(df.head())
