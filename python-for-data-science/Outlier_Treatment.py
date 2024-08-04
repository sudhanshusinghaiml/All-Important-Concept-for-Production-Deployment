'''
If this value is between:

-0.5 and 0.5, the distribution of the value is almost symmetrical
-1 and -0.5, the data is negatively skewed, and if it is between 0.5 to 1, the data is positively skewed. The skewness is moderate.
If the skewness is lower than -1 (negatively skewed) or greater than 1 (positively skewed), the data is highly skewed.
'''

"""
--> Outlier Treatment:
	Anamoly:
    - Errorneous Data - We will try to replace with the original data based on client discussion.
	
	Natural Outlier: 
	- We do not remove the data. We will discuss with Product Owners or Domain Expert to decide the action that we can take.
		
	- We can discard all the outlier values if business says these will not occur again(one time occurrence)
	- If outliers are valid, we can normalize the data using 
		- Standard Scaler(z-scaler). Ranges from -3 to +3
		- MinMax Scaler
		- Replace         (Doable only if domain-experts agree to it)
		- Box-Cox(lograthmics)
							  
	- If the outlier is natural and valid - We use Standard Scaler (-3 to 3)
	- If outlier is not legitimate - We use MinMax Scaler (0 to 1)


"""

##=======================================
##Outlier Treatment and Different Methods
##=======================================

##Method I - Z Score
##==================
df.referral_current_salary.describe()

df['referral_current_salary_zscore'] = ( df.referral_current_salary - df.referral_current_salary.mean() ) / df.referral_current_salary.std()
df['referral_current_salary_zscore'].describe()

# The values will range from -3 to +3. If the values is less than -3 and more than +3 then we need to impute it with below formula to bring it within range.

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