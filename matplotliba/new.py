import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')
s= pd.Series(data = [10, 5, 25, 20 ,19], index = [1,2,3,4,5])
paid= df[df['Type'] =='Paid'] 
paid = paid[paid['Price'] <= 12]
paid.plot(kind='pie')
plt.show()