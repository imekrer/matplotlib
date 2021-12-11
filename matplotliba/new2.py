import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')
d = df.pivot_table(
    index = 'Content rating',
    columns = 'Type',
    values = 'Installs',
    aggfunc = 'mean'
)
d.plot(kind = 'barh')
plt.show()