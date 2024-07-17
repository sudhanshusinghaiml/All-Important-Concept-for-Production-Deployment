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

## =======================================================================================
'''
    Code to add subplot to display boxplot for all numerical columns.
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
    Code to add subplot to display boxplot for all numerical columns.
'''
# ----------------------------------------------------------------------------------------
cols=election_df.dtypes[election_df.dtypes!='object'].index #taking only numerical attributes
fig = plt.figure(figsize = (12,7)) #figure size
ax = fig.gca() #this function adds as many as subplots as required depending upon number of columns
election_df[cols].hist(ax=ax) #histogram for numerical columns where axis ax is passed 
plt.show()

## ========================================================================================
'''
    Code to Plot ROC and AUC Curve for training and test data adjacent to each other.
'''
# ----------------------------------------------------------------------------------------
fig = plt.figure(figsize=(10,4))
fig.suptitle('ROC Curve for Logistic Regression')
lr_train_prob = lr_model.predict_proba(X_train)
lr_train_prob = lr_train_prob[:,1]
lr_auc = roc_auc_score(y_train, lr_train_prob)
print('Training data AUC Score: %.3f' % lr_auc)
fpr, tpr, thresholds = roc_curve(y_train, lr_train_prob)
plt.subplot(1,2,1)
plt.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
plt.plot(fpr, tpr, marker='.')

lr_test_prob = lr_model.predict_proba(X_test)
lr_test_prob = lr_test_prob[:,1]
lr_auc = roc_auc_score(y_test, lr_test_prob)
print('Test data AUC Score: %.3f' % lr_auc)
fpr, tpr, thresholds = roc_curve(y_test, lr_test_prob)
plt.subplot(1,2,2)
plt.plot([0, 1], [0, 1], linestyle='--')
# plot the roc curve for the model
plt.plot(fpr, tpr, marker='.')
# show the plot
plt.show()

## =====================================================================================
'''
    Code to show basic plot with values on top of barplot.
'''
# --------------------------------------------------------------------------------------

def add_labels_on_y_axis(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha='center')
    
plt.figure(figsize=(12,6))
sns.barplot(data = temp, x= 'SubArea', y = 'Count')
add_labels_on_y_axis(temp['SubArea'],temp['Count'])
plt.title('No of Houses in each Sub Area')
plt.xticks(rotation=90)
plt.show()

## =====================================================================================
'''
    Plot the distribution plot for all the integer and float variables
'''

fig = plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace=0.7, top=0.95, wspace= 0.3, bottom=0.1)
fig.tight_layout()
for idx, col in enumerate(modified_df.select_dtypes(include=['int64','float64']).columns):
    ax1 = fig.add_subplot(4,3,idx+1)
    sns.histplot(data = modified_df, x = col, kde = True)
    
plt.suptitle('Distibution plot for Continuous variables')
plt.show()

## ======================================================================================
'''
    Code to plot heatmap using mask.
'''
# --------------------------------------------------------------------------------------
plt.figure(figsize=(12,6))
sns.heatmap(modified_df.corr(), annot=True, cmap='rainbow', mask=np.triu(modified_df.corr(),+1))
plt.title('Heatmap of all Variables')
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
'''
    Code to plot Pareto Chart in python
'''

from matplotlib.ticker import PercentFormatter

#define aesthetics for plot
bar_color = 'steelblue'
line_color = 'red'
line_size = 4

plt.figure(figsize=(12,4))
#create basic bar plot
fig, ax1 = plt.subplots()
ax1.bar(product_line_df['PRODUCTLINE'], product_line_df['Count'], color=bar_color)

#add cumulative percentage line to plot
ax2 = ax1.twinx()
ax2.plot(product_line_df['PRODUCTLINE'], product_line_df['Cumulative_Count'], color=line_color, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax1.tick_params(axis='y', colors=bar_color)
ax2.tick_params(axis='y', colors=line_color)

for label in ax1.containers:
    ax1.bar_label(label)

for x_val, y_val in zip (range(len(product_line_df)), round(product_line_df['Cumulative_Count'],2)):
    ax2.text(x=x_val-0.20, y=y_val+0.125, s=y_val, fontsize=10, color="black", ha="center", va="center")
    
plt.suptitle('Product line Pareto Chart', fontsize=12)

#display Pareto chart
plt.show();

## =============================================================================================
'''
    Code to plot important features in Classification Models
'''

# Sort the important features in descending order.
dt_sorted_index = lp_gs_xgb_model.best_estimator_.feature_importances_.argsort()
dt_important_features_values = lp_gs_xgb_model.best_estimator_.feature_importances_[dt_sorted_index][::-1]

# Get the feature names.
dt_feature_names = X_train_lp.columns[dt_sorted_index]

# Plotting the important features.
fig, ax = plt.subplots(figsize=(12,5))
ax.bar(dt_feature_names, dt_important_features_values)
for label in ax.containers:
    ax.bar_label(label, fmt='%.2f')
ax.set_xlabel('Feature Importance')
ax.set_ylabel('Feature Name')
ax.set_title('Feature Importance of GridSearchCV')
ax.set_xticks(dt_sorted_index)
ax.set_xticklabels(dt_feature_names, rotation=45, ha='right')
plt.show();

## =============================================================================================
'''
    Code to plot confusion matrix in Classification Models
'''

lr_train_cm=confusion_matrix(y_train, y_logistic_train_predict)
lr_test_cm=confusion_matrix(y_test, y_logistic_test_predict)

disp_lr_train = ConfusionMatrixDisplay(confusion_matrix=lr_train_cm, display_labels=logistic_model.classes_)
disp_lr_train.plot()
plt.grid(False)
plt.show()

## =============================================================================================
'''
    Code to plot ROC AUC Curve for Classification Models
'''

# predict probabilities
lr_mb_train_predicted = mb_lr_model.predict_proba(X_train_mb)

# keep probabilities for the positive outcome only
lr_mb_train_prob_predicted = lr_mb_train_predicted[:,1]

# calculate AUC
lr_mb_auc_train = roc_auc_score(y_train_mb, lr_mb_train_prob_predicted)
print('AUC for train data for Logistic Regression: %.3f' % lr_mb_auc_train)

# predict probabilities
lr_mb_test_predicted = mb_lr_model.predict_proba(X_test_mb)

# keep probabilities for the positive outcome only
lr_mb_test_prob_predicted = lr_mb_test_predicted[:,1]

# calculate AUC
lr_mb_auc_test = roc_auc_score(y_test_mb, lr_mb_test_prob_predicted)
print('AUC for test data for Logistic Regression: %.3f' % lr_mb_auc_test)

# calculate roc curve
lr_mb_train_fpr, lr_mb_train_tpr, lr_mb_train_thresholds = roc_curve(y_train_mb, lr_mb_train_prob_predicted)
lr_mb_test_fpr, lr_mb_test_tpr, lr_mb_test_thresholds = roc_curve(y_test_mb, lr_mb_test_prob_predicted)
plt.plot([0, 1], [0, 1], linestyle='--')

# plot the roc curve for the model
plt.plot(lr_mb_train_fpr, lr_mb_train_tpr, color='g')
plt.plot(lr_mb_test_fpr, lr_mb_test_tpr, color='r')
plt.show();

## =============================================================================================