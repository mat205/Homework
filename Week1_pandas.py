#TASK 1
import pandas as pd
#reading the csv to display the data
df = pd.read_csv (r'/Users/maiwasetembo/Downloads/GOOG.csv')
#saving csv to pandas
df.to_csv (r'/Users/maiwasetembo/Downloads/GOOG.csv', index=None)
#displaying the data
print(df)

import matplotlib.pyplot as plt
#plotting close prices for google
df['Close'].plot(grid=True,)
#displaying the plot
plt.show()

#TASK 2
df1 = pd.read_csv (r'/Users/maiwasetembo/Downloads/MSFT.csv')
#saving csv to pandas
df1.to_csv (r'/Users/maiwasetembo/Downloads/MSFT.csv', index=None)
#displaying the data
print(df1)

#plotting close prices for google
df1['Close'].plot(grid=True,)
#displaying the plot
plt.show()


