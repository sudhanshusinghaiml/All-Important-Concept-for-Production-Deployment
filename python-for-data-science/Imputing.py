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

from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)

company_impute_df = pd.DataFrame(imputer.fit_transform(company_impute_df), columns = company_impute_df.columns)

##=====================================================================================

