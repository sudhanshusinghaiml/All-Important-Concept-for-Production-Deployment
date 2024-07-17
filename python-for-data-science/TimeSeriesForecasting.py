'''
	Libraries used for Basic - Time Series Analysis
'''
# ----------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
    For decomposing  time-series into Trends, Seasonality and Residual
'''
from statsmodels.tsa.seasonal import seasonal_decompose

# ========================================================================
'''
    We are trying to tell pandas that we are going to work with time series data.
    It is recommended that we make our time series reference as the index.
'''

df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'])
df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'], index_col = 'Year-Month')
df2 = pd.read_csv('daily-total-female-births.csv', parse_dates = ['Date'], index_col = 'Date')
df_1 = pd.read_csv("Beer Australia.csv",parse_dates=True,index_col=0)

date = pd.date_range(start='1/1/1956', end='1/1/1996', freq='M')
df['Time_Stamp'] = pd.DataFrame(date)
df.head()
df.set_index(keys='Time_Stamp',drop=True,inplace=True)
df.drop(labels = ['Quarter','Year'],axis =1, inplace = True)
df.head()

# ========================================================================
'''
    Plotting Time-Series using PyLab - Increase the figure size
'''

from pylab import rcParams
rcParams['figure.figsize'] = 12, 6
df1.plot()
plt.show()

df.plot(figsize=(15,8),grid=True);

# =======================================================================

'''
   Decompose the time series using additive method
''' 

df1_add_decompose = seasonal_decompose(df1, model = 'additive', period = 12)
df1_add_decompose.plot()
plt.show()

'''
    Decompose the time series using multiplicative method
'''

df1_mul_decompose = seasonal_decompose(df1, model = "multiplicative")
df1_mul_decompose.plot()
plt.show()

# =======================================================================

'''
   Let us inspect each component of df1_add_decompose. Since this is an additive model:
   Observed = Trend + Seasonal + Irregular should hold true
    35.142857 -3.077608 -1.065249
'''
df1_add_decompose.trend
df1_add_decompose.seasonal
df1_add_decompose.resid

# =======================================================================

'''
   Let us inspect each component of df1_mul_decompose. Since this is an additive model:
   Observed = Trend * Seasonal * Irregular should hold true
    35.14*.93*.952
'''
df1_mul_decompose.trend
df1_mul_decompose.seasonal
df1_mul_decompose.resid

# =======================================================================

'''
    Down Sampling - Here we decrease the frequency of the samples, such as from days to months. 
    The sales data is monthly, but we prefer the data to be quarterly. The year can be divided into 4 business quarters, 3 months a piece.
    The resample() function will group all observations by the new frequency.
    We need to decide how to create a new quarterly value from each group of 3 records. We shall use the mean() function to calculate the average monthly sales numbers for the quarter
'''
df1_q = df1.resample('Q').mean()

resample             = tseries.resample('Q')
quarterly_mean_sales = resample.mean()
print(quarterly_mean_sales.head())
quarterly_mean_sales.plot()
plt.show()

'''
    We can turn monthly data into yearly data. Down-sample the data using the alias, A for year-end frequency and this time use sum to calculate the total sales each year.
'''
resample = tseries.resample('A')
yearly_mean_sales = resample.sum()
print(yearly_mean_sales.head() )
yearly_mean_sales.plot()
plt.show()

# =======================================================================
'''
    Upsampling: Here we increase the frequency of the samples, such as from minutes to seconds.
'''
df1_d = df1.resample('D').ffill()
df1_h = df1.resample('H').interpolate()


from pandas import read_csv
from datetime import datetime
import matplotlib.pyplot as plt

def parser(x):
       return datetime.strptime('190'+x, '%Y-%m')

tseries = read_csv('shampoo-sales.csv', header = 0, index_col = 0, parse_dates = True, squeeze = True, date_parser = parser)
upsampled_ts = tseries.resample('D').mean()
print(upsampled_ts.head(36))

'''
    We will observe that the resample() function would create the rows by putting NaN values as new values for dates other than day 01.
    
    We can interpolate the missing values at this new frequency. The function, interpolate() of pandas library is used to interpolate the missing values. We use a linear interpolation which draws a straight line between available data, on the first day of the month and fills in values at the chosen frequency from this line.
'''

interpolated = upsampled_ts.interpolate(method = 'linear')
interpolated.plot()
plt.show()

'''
    Another common interpolation method is to use a polynomial or a spline to connect the values. This creates more curves and look more natural on many datasets.
    Using a spline interpolation requires you to specify the order (count of terms in the polynomial). Here, we are using 2.
'''

interpolated1 = upsampled_ts.interpolate(method = 'spline', order = 2)
interpolated1.plot()
plt.show()

# =======================================================================
'''
    Plot the distribution plot for quarterly comparison of the shipments.
'''

sns.distplot(x = df.loc[df.index.quarter==1]['Shipments'] )
sns.distplot(x = df.loc[df.index.quarter==2]['Shipments'] )
sns.distplot(x = df.loc[df.index.quarter==3]['Shipments'] )
sns.distplot(x = df.loc[df.index.quarter==4]['Shipments'] )
plt.grid()

sns.distplot(x = df.loc[df.index.quarter==1]['Shipments'], hist=False )
sns.distplot(x = df.loc[df.index.quarter==2]['Shipments'], hist=False )
sns.distplot(x = df.loc[df.index.quarter==3]['Shipments'], hist=False )
sns.distplot(x = df.loc[df.index.quarter==4]['Shipments'], hist=False )
plt.legend(['Q1','Q2','Q3','Q4'])
plt.grid()

# =======================================================================