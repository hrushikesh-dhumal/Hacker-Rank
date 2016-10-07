import pandas as pd
df = pd.read_csv("trainingdata.txt" , sep=',', names={'time_charged', 'time_lasted'}, header=None)

df.describe()

import matplotlib.pyplot as plt
%matplotlib inline 


plt.scatter(df['time_charged'], df['time_lasted'])
plt.show()