import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
array = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
plt.plot(array, array2)
plt.show()

df.head()
