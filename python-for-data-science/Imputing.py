"""
Imputing missing values with the median is particularly useful in some scenarios.

When to Impute with Median:

1. Skewed Distributions:
   - Reason: The median is a better measure of central tendency than the mean for skewed distributions because it is not affected by extreme values (outliers).
   - Example: Income data often has a long tail with very high values. Imputing missing income values with the median will prevent the outliers from skewing the imputed values.

2. Outliers:
   - Reason: The median is robust to outliers. If the dataset contains outliers, the mean could be distorted, but the median remains stable.
   - Example: Housing prices in a city where a few extremely high prices could distort the mean but not the median.

3. Non-Normal Distributions:
   - Reason: For non-normal distributions, the median can provide a more accurate central value than the mean.
   - Example: Age data in a population where the distribution might be non-symmetric.

"""

"""
Imputing missing values with the mean is a common technique used in some scenarios.

When to Impute with Mean:

1. Symmetrical (Normally Distributed) Data:
   - Reason: If the data is normally distributed (i.e., it follows a bell curve), the mean is a good measure of central tendency.
   - Example: Heights or weights of a large population where the distribution is approximately normal.

2. No Outliers:
   - Reason: The mean is sensitive to outliers. If your data does not contain significant outliers, mean imputation can be appropriate.
   - Example: Test scores in a controlled environment where extreme values are rare.

3. Consistency and Simplicity:
   - Reason: Mean imputation is straightforward and computationally simple. It provides a quick and consistent way to handle missing data.
   - Example: Financial data where values are generally stable and predictable over time.

4. Large Sample Size:
   - Reason: In large datasets, the impact of a few missing values is minimized, and the mean can provide a reasonable estimate.
   - Example: Sensor data collected over a long period with occasional missing readings.

"""

##===========================
##Imputing with Median Values
##===========================
df_numerical = df.select_dtypes(['int64','float64'])
df_categorical = df.select_dtypes(['object'])

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='median')
imputer

imr = imputer.fit(df_numerical)
imr

df_numerical = pd.DataFrame(imr.transform(df_numerical),columns=df_numerical.columns)
df_numerical

df2 = pd.concat([df_numerical, df_categorical], axis=1, join='inner')
##=====================================================================================

# Impute the Non-Object values using Median
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'median',verbose=0)#nil, null, NaN
imputer= imputer.fit(cars[non_objects])

cars[non_objects]=imputer.transform(cars[non_objects])

# Impute the Object values using Mode
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent',verbose=0)
imputer= imputer.fit(cars[objects])

cars[objects]=imputer.transform(cars[objects])

##=====================================================================================
"""
KNN Imputer - is best suited for Continuous Features only.
"""

from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)

company_impute_df = pd.DataFrame(imputer.fit_transform(company_impute_df), columns = company_impute_df.columns)

##=====================================================================================

