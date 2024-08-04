''' 
    Code to add subplot automatically based on the number of columns
'''
# ------------------------------------------------------------------

cols=df.dtypes[df.dtypes!='object'].index #taking only numerical attributes
fig = plt.figure(figsize = (12,7)) #figure size
ax = fig.gca() #this function adds as many as subplots as required depending upon number of columns
df_filtered[cols].hist(ax=ax) #histogram for numerical columns where axis ax is passed 
plt.show()
##=======================================================================================

''' 
    Code to show basic subplot of 2 images adjacent to each other
'''
# -------------------------------------------------------------------
for idx, col in enumerate(df.drop(['ID','Brand'], axis=1).columns.values):
    fig = plt.figure(figsize=(12,4))
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.5, bottom=0.3)
    fig.suptitle(f'Boxplot and distribution plot for {col}')
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    sns.boxplot(x=df[col], ax=ax1)
    sns.histplot(x=df[col], kde=True, ax = ax2)
    plt.show()

## =====================================================================================
'''
    Code to show basic subplot of 4 images in 2X2 matrix form
'''
# --------------------------------------------------------------------------------------

fig = plt.figure(figsize=(15,15))
fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.5, bottom = 0.3)
fig.suptitle('Bivariate Analysis of Variables', fontsize=12)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

sns.boxplot(data=df_auto, x='Gender', y = 'Price', hue='Make', ax= ax1);
sns.boxplot(data=df_auto, x='Profession', y = 'Price', hue='Make',  ax= ax2);
sns.boxplot(data=df_auto, x='Marital_status', y = 'Price', hue='Make', ax= ax3);
sns.boxplot(data=df_auto, x='Education', y = 'Price',  ax= ax4);

ax1.legend(loc="upper right", title="Gender vs Price", title_fontsize="large")
ax2.legend(loc="upper right", title="Profession vs Price", title_fontsize="large")
ax3.legend(loc="upper center", title="Marital_status vs Price", title_fontsize="large")
ax4.title.set_text("Education vs Price")

## ========================================================================================
'''
    Code to show basic plot with font color and font size settings.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(20,10))
sns.set(font_scale=2)
font = {'family':'cursive','color':'green','size':20}

sns.barplot(data=df[df['Current Rank']==1], x ='Year', y = 'earnings ($ million)')

plt.title("Price of Car Vs Age of the Individual",fontdict=font)
plt.xlabel("Age",fontdict=font)
plt.ylabel("Price of Car",fontdict=font)
plt.xticks(rotation = 90)
plt.show();

## =======================================================================================
'''
    Functional Code to print Description and Display boxplot and distplot for a particular columns.
'''
# --------------------------------------------------------------------------------------

def univariateAnalysis_numeric(column):
    print("Description of " + column)
    print("============================================================================")
    print(pca_df[column].describe(),end=' ') 
    # end as space indicates that end of the exceution is a space and not new line
    
    fig = plt.figure(figsize=(15,4))
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace= 0.5, bottom = 0.3)
    ax1 = fig.add_subplot(1,2,1)
    # plt.figure()
    print("Distribution of " + column)
    print("============================================================================")
    sns.distplot(pca_df[column], kde=False, color='g', ax=ax1);
    # plt.show()
    
    ax2 = fig.add_subplot(1,2,2)
    # plt.figure()
    print("BoxPlot of " + column)
    print("============================================================================")
    sns.boxplot(x=pca_df[column], ax=ax2)
    plt.show()
    
## =======================================================================================
'''
    Code to subplot histplot and boxplot adjacent to each other for all numerical columns.
'''
# --------------------------------------------------------------------------------------

 for col in df.select_dtypes(exclude=['object']).columns:
    fig = plt.figure(figsize=(15,4))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    sns.boxplot(x=df[col], ax=ax1)
    ax1.title.set_text(f'Variable - {col} \n Skew Before Scaling:- {round(df[col].skew(),2)}')

    sns.histplot(data = df, x = col, kde = True)
    ax2.title.set_text(f'Variable - {col}')
    plt.show()
## =======================================================================================
'''
    Code to subplot histplot and boxplot adjacent to each other for all columns.
'''
# --------------------------------------------------------------------------------------

 for col in df_pca_census_data.columns:
    fig = plt.figure(figsize=(15,4))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    sns.boxplot(x=df_pca_census_data[col], ax=ax1)
    ax1.title.set_text(f'Variable - {col} \n Skew Before Scaling:- {round(df_pca_census_data[col].skew(),2)}')

    sns.boxplot(x=df_pca_census_scaled_data[col], ax = ax2)
    ax2.title.set_text(f'Variable - {col} \n Skew After Scaling:- {round(df_pca_census_scaled_data[col].skew(),2)}')
    plt.show()
## =======================================================================================
'''
    Code to subplot boxplot for all numerical columns and then hide the subplot which are empty.
'''
# --------------------------------------------------------------------------------------

fig, ax = plt.subplots(5, 3, figsize = (20, 20))
ax = ax.flatten()

for i, col in enumerate(df_ads_data_num):
    sns.boxplot(x = df_ads_data[col], ax = ax[i])
fig.delaxes(ax[14])
fig.delaxes(ax[13])
plt.suptitle('Outlier Analysis using BoxPlots', fontsize = 12)
fig.tight_layout()

## =======================================================================================
'''
    Code to add subplot to display boxplot for all numerical columns.
'''
# --------------------------------------------------------------------------------------

fig = plt.figure(figsize=(18,6))
fig.subplots_adjust(hspace=0.5, top=0.8, wspace= 0.3, bottom = 0.1)
fig.tight_layout()
for i, col in enumerate(survey_df.select_dtypes(include=['float64','int64']).columns):
    ax1 = fig.add_subplot(1,3,i+1)
    sns.boxplot(x=survey_df[col], ax = ax1)
    ax1.title.set_text(f'Boxplot of- {col} \nSkew:- {round(survey_df[col].skew(),2)} & kurtosis is- {round(survey_df[col].kurtosis(),4)} ')
    
plt.suptitle('Boxplot of Variables for Outlier Analysis', fontsize=20)
plt.show()

## =======================================================================================
'''
    Code to plot lmplot using markers, font styles and colors.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(6,5))
sns.set(font_scale=1)
font = {'family':'cursive','color':'green','size':10}
sns.lmplot(data=df_auto, x='Age', y = 'Price', hue='Make', markers=['o','x','^']);
plt.title("Price Vs Age for each Make Type",fontdict=font);
plt.xlabel("Age",fontdict=font)
plt.ylabel("Price",fontdict=font)
plt.xticks(rotation = 90)
plt.show();

## =======================================================================================
'''
    Code to plot pairplot using corner, font styles and colors.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(30,30))
font = {'family':'cursive','color':'green','size':10}
sns.pairplot(user_data, corner=True);
plt.title("Pairplot of all Features",fontdict=font);
plt.show();

## =======================================================================================
'''
    Code to plot heatmap using mask, font styles and colors.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(30,30))
font = {'family':'cursive','color':'green','size':10}
sns.heatmap(user_data.corr(), annot=True, cmap='rainbow', mask = np.triu(user_data.corr(),+1));
plt.title("Heatmap of all Features",fontdict=font);
plt.show();

## ======================================================================================
'''
    Code to plot heatmap using mask.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(12,6))
sns.heatmap(modified_df.corr(), annot=True, cmap='rainbow', mask=np.triu(modified_df.corr(),+1))
plt.title('Heatmap of all Variables')
plt.show()


## =======================================================================================
'''
    Code to add subplot to display strip plot for all numerical columns.
'''
# ----------------------------------------------------------------------------------------
fig = plt.figure(figsize=(15,30))
fig.subplots_adjust(hspace=0.5, top=0.95, wspace= 0.3, bottom = 0.1)
fig.tight_layout()

for idx, col in enumerate(user_data.select_dtypes(include=['float64','int64']).columns):
    ax1 = fig.add_subplot(9,3,idx+1)
    sns.stripplot(y=user_data[col], x=user_data['runqsz'],ax=ax1,)
    ax1.set_ylabel(col)
    
plt.suptitle('Strip Plot Analysis', fontsize=25)
plt.show()

## =======================================================================================
'''
    Code to add subplot to display histogram for all numerical columns.
'''
# ----------------------------------------------------------------------------------------
cols=election_df.dtypes[election_df.dtypes!='object'].index #taking only numerical attributes
fig = plt.figure(figsize = (12,7)) #figure size
ax = fig.gca() #this function adds as many as subplots as required depending upon number of columns
election_df[cols].hist(ax=ax) #histogram for numerical columns where axis ax is passed 
plt.show()

## ========================================================================================

'''
    Code to show count plot with values on top of barplot.
'''
# --------------------------------------------------------------------------------------

fig = plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace=0.7, top=0.95, wspace= 0.3, bottom=0.1)
fig.tight_layout()
for idx, col in enumerate(cirrhosis_df.select_dtypes(include='object').columns):
    ax1 = fig.add_subplot(4,3,idx+1)
    sns.countplot(data = cirrhosis_df, x = col, ax = ax1)
    for label in ax1.containers:
        ax1.bar_label(label)

plt.suptitle('Distibution plot for selected features')
plt.show()

## =====================================================================================
'''
    Plot the histplot plot for all the integer and float variables
'''

fig = plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace=0.7, top=0.95, wspace= 0.3, bottom=0.1)
fig.tight_layout()
for idx, col in enumerate(modified_df.select_dtypes(include=['int64','float64']).columns):
    ax1 = fig.add_subplot(4,3,idx+1)
    sns.histplot(data = modified_df, x = col, kde = True)
    
plt.suptitle('Distibution plot for Continuous variables')
plt.show()

##=======================================================================================
'''
    Code to increase the figure size using figsize
'''
# ---------------------------------------------------
#Increase the figure size
from pylab import rcParams
rcParams['figure.figsize'] = 12, 6
df1.plot()
plt.show()

# =======================================================================================

fig = plt.figure(figsize=(12,12))
fig.subplots_adjust(hspace=0.3, top=0.95, wspace= 0.3, bottom = 0.3)
fig.suptitle('Bivariate Analysis - Box plot', fontsize=12)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

sns.boxplot(y=transport_df['Distance'],x=transport_df['Transport'], hue=transport_df['Gender'], ax= ax1);
sns.boxplot(data=transport_df, y='Salary',x='Transport', hue=transport_df['Gender'], ax= ax2);
sns.boxplot(data=transport_df, y='Age',x='Transport',hue=transport_df['Gender'], ax= ax3);

ax1.title.set_text("Distance for Transport Type")
ax1.tick_params(axis='x', rotation=0)
ax2.title.set_text("Salary for Transport Type")
ax2.tick_params(axis='x', rotation=0)
ax3.title.set_text("Age for Transport Type")
ax3.tick_params(axis='x', rotation=0)

## ===============================================================================================
'''
    Code to find the correlation using python codes
'''
# ---------------------------------------------------

# Tables to understand the correlation of among different features in the dataset 
cleaned_df.corr()

correlation_threshold = 0.5

def high_cor_function(df):
    cor = df.corr()
    c1 = cor.stack().sort_values(ascending=False).drop_duplicates()
    high_cor = c1[c1.values!=1]    
    return (high_cor[high_cor>correlation_threshold])
    
correlated_df=pd.DataFrame(high_cor_function(cleaned_df))
correlated_df.reset_index(inplace=True)
correlated_df.columns=['X-Axis','Y-Axis','Values']
correlated_df.head()

fig = plt.figure(figsize=(15,4))
fig.subplots_adjust(hspace=0.5, top=0.85, wspace= 0.3, bottom = 0.1)
fig.tight_layout()

for i in range(0,len(correlated_df)):
    ax1 = fig.add_subplot(1,2,i+1)
    sns.scatterplot(x=cleaned_df[correlated_df.iloc[i,0]], y=cleaned_df[correlated_df.iloc[i,1]],ax=ax1)
    ax1.set_xlabel(correlated_df.iloc[i,0])
    ax1.set_ylabel(correlated_df.iloc[i,1])
    ax1.title.set_text(f'Correlation: {round(correlated_df.iloc[i,2],2)}')
    
plt.suptitle('Scatter Plot Analysis', fontsize=25)
plt.show();

## ==============================================================================================
'''
    Code for conditional boxplot
'''
# ---------------------------------------------------

for idx, col in enumerate(cleaned_df.select_dtypes(include=['int','float']).columns.values):
    fig = plt.figure(figsize=(12,4))
    fig.subplots_adjust(hspace=0.6, top=0.9, wspace=0.5, bottom=0.3)
    fig.suptitle(f'Boxplot for {col}')
    sns.boxplot(data = cleaned_df, y = col, x ='Taken_product', hue='preferred_device')
    
plt.suptitle('Distibution plot for Continuous variables')
plt.show();

## =============================================================================================
'''
    Code for Violin Plot
'''

fig = plt.figure(figsize=(15,30))
fig.subplots_adjust(hspace=0.5, top=0.95, wspace= 0.3, bottom = 0.1)
fig.tight_layout()

for idx, col in enumerate(user_data.select_dtypes(include=['float64','int64']).columns):
    ax1 = fig.add_subplot(9,3,idx+1)
    sns.violinplot(y=user_data[col], x=user_data['runqsz'],ax=ax1)
    ax1.set_ylabel(col)
    
plt.suptitle('Violin Plot Analysis', fontsize=25)
plt.show()

## =============================================================================================
'''
    Code to plot numbers on top of bars in the Plot
'''
plt.figure(figsize=(12,4))
ax = sns.countplot(data=df, x='PRODUCTLINE')
for label in ax.containers:
    ax.bar_label(label)
plt.xticks(rotation=45)
plt.suptitle('Productline Countplot', fontsize=12)
plt.show();

plt.figure(figsize=(12,4))
ax = sns.countplot(data=df, x='PRODUCTLINE', hue ='DEALSIZE')
for label in ax.containers:
    ax.bar_label(label)
plt.xticks(rotation=45)
plt.suptitle('Count of Orders based on Deal Size and Product Line', fontsize=12)
plt.show();

## =============================================================================================
