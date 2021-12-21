from sklearn.datasets import load_iris
data = load_iris()

import pandas as pd
df = pd.DataFrame(data.data) # feature
df.head()
print(data)
