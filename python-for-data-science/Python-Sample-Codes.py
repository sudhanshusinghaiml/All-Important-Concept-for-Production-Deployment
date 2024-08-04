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