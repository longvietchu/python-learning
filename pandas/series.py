import pandas as pd

print(pd.__version__)
a = [5, 2, 8]

pd_series = pd.Series(a, index=["x", "y", "z"])

print(pd_series)
