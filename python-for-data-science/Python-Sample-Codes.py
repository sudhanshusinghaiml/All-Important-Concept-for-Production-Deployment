credit.AGE.replace(to_replace=-20, value=np.NaN, inplace= True)
credit.AGE.replace(to_replace=120, value=np.NaN, inplace= True)

df_auto['Gender'].replace(to_replace='Femal', value='Female', inplace=True)
df_auto['Gender'].replace(to_replace='Femle', value='Female', inplace=True)

data_df['Credit.History']=np.where(data_df['Credit.History'] =='very good', 'verygood', data_df['Credit.History'])
data_df['Credit.History']=np.where(data_df['Credit.History'] =='Poor', 'poor', data_df['Credit.History'])

df['referral_aptitude_reasoning_score']=df['referral_aptitude_reasoning_score'].replace('?',np.NAN)
df['referral_aptitude_numerical_score']=df['referral_aptitude_numerical_score'].replace('?',np.NAN)

df['referral_aptitude_reasoning_score']=df['referral_aptitude_reasoning_score'].astype('float64')
df['referral_aptitude_numerical_score']=df['referral_aptitude_numerical_score'].astype('float64')

user_data['rchar'] = user_data['rchar'].fillna(user_data['rchar'].median())
user_data['wchar'] = user_data['wchar'].fillna(user_data['wchar'].median())

user_data['runqsz']=np.where(user_data['runqsz']=='CPU_Bound',1,0)

credit.reset_index(drop=True, inplace=True)
credit.DEFAULT = np.where(credit.index.isin(list_anom1), 0, credit.DEFAULT)

==================================================================================
Rename Columns
===============

rankings_pd = pd.DataFrame(rankings)
# Before renaming the columns
print(rankings_pd)
rankings_pd.rename(columns = {'test':'TEST'}, inplace = True)
===================================================================================
Drop Duplicate rows
====================

# Below are quick example
# keep first duplicate row
df2 = df.drop_duplicates()

# Using DataFrame.drop_duplicates() to keep first duplicate row
df2 = df.drop_duplicates(keep='first')

# keep last duplicate row
df2 = df.drop_duplicates( keep='last')

# Remove all duplicate rows 
df2 = df.drop_duplicates(keep=False)

# Delete duplicate rows based on specific columns 
df2 = df.drop_duplicates(subset=["Courses", "Fee"], keep=False)

# Drop duplicate rows in place
df.drop_duplicates(inplace=True)

# Using DataFrame.apply() and lambda function 
df2 = df.apply(lambda x: x.astype(str).str.lower()).drop_duplicates(subset=['Courses', 'Fee'], keep='first')
2. drop_duplicates() Syntax & Examp

==================================================================================

'''
If this value is between:

-0.5 and 0.5, the distribution of the value is almost symmetrical
-1 and -0.5, the data is negatively skewed, and if it is between 0.5 to 1, the data is positively skewed. The skewness is moderate.
If the skewness is lower than -1 (negatively skewed) or greater than 1 (positively skewed), the data is highly skewed.
'''

##=======================================
##Outlier Treatment and Different Methods
##=======================================

##Method I - Z Score
##==================
df.referral_current_salary.describe()

df['referral_current_salary_zscore'] = ( df.referral_current_salary - df.referral_current_salary.mean() ) / df.referral_current_salary.std()
df['referral_current_salary_zscore'].describe()

# The values will range from -3 to +3. If the values is less than -3 and more than +3 then we need to impute it with
below formula to bring it within range.

# Let us calculate the value for referral_current_salary if ZScore has to be 3
referral_current_salary_impute_value = (3*df.referral_current_salary.std()) + df.referral_current_salary.mean()
round(referral_current_salary_impute_value,2)

df['referral_current_salary'] = np.where(df.index.isin(list1), round(referral_current_salary_impute_value,2), 
                                         df['referral_current_salary'])
                                         
df.referral_current_salary.describe()

##Method II- Boxplot method
##=========================
def get_outlier_range(cname):
    sorted(cname)
    q1, q3 = cname.quantile([0.25,0.75])
    IQR = q3-q1
    llimit = q1-(1.5 * IQR)
    hlimit = q3+(1.5 * IQR)
    return llimit, hlimit 
    
clist = ['Ad - Length', 'Ad- Width', 'Ad Size', 'Available_Impressions', 'Matched_Queries', 'Impressions', 'Clicks', 'Spend', 'Fee', 'Revenue', 'CTR', 'CPM','CPC']
for col in clist:
    lval, hval = get_outlier_range(df_ads_data[col])
    df_ads_data[col] = np.where(df_ads_data[col] >hval, hval, df_ads_data[col])
    df_ads_data[col] = np.where(df_ads_data[col] <lval, lval, df_ads_data[col])

## -------------------------
def get_outlier_range(df,cname):
    sorted(cname)
    llimit = df[cname].min()
    hlimit = df[cname].quantile(0.95)
    return llimit, hlimit