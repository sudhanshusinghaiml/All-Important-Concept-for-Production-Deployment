# ================================================================================================================
""" 
    Code for Data Mining using Principal Component Analysis 
"""

# Apply PCA taking all features
from sklearn.decomposition import PCA
all_pca = PCA(n_components= 8, random_state = 42)
all_pca_transformed = all_pca.fit_transform(df_smoking_scaled) 

# Extract eigen vectors
# np.set_printoptions(linewidth=np.inf)
print(all_pca.components_)
# Check the eigen values
# Note: This is always returned in descending order
all_pca.explained_variance_

# Check the cumlative explained variance ratio to find a cut off for selecting the number of PCs
all_pca.explained_variance_ratio_

# Extract eigen vectors
# np.set_printoptions(linewidth=np.inf)
print(all_pca.components_)
# ===============================================================================================================

X2_train, X2_test, y2_train, y2_test = train_test_split(X, Y, test_size=0.30 , random_state=1)
X2_constant = sm.add_constant(x)

X2_train_const, X2_test_const, y2_train_const, y2_test_const = train_test_split(X2_constant, Y, test_size=0.30 , random_state=1)
ols_model = sm.OLS(y2_train_const,X2_train_const).fit()
ols_model.summary()

# ===============================================================================================================

# How to run multiple Regression models and compare the score
# ============================================================

dtr = tree.DecisionTreeRegressor(random_state=123)
regression_model = LinearRegression()


models=[regression_model,dtr]

rmse_train=[]
rmse_test=[]
scores_train=[]
scores_test=[]

for i in models:  # Computation of RMSE and R2 values 
    i.fit(x_train,y_train)
    scores_train.append(i.score(x_train, y_train))
    scores_test.append(i.score(x_test, y_test))
    rmse_train.append(np.sqrt(mean_squared_error(y_train,i.predict(x_train))))
    rmse_test.append(np.sqrt(mean_squared_error(y_test,i.predict(x_test))))
        
print(pd.DataFrame({'Train RMSE': rmse_train,'Test RMSE': rmse_test,'Training Score':scores_train,'Test Score': scores_test},index=['Linear Regression','Decision Tree Regressor']))
            
# =============================================================================================================

# How to run multiple Classifier models and compare the score
# ============================================================

dtc = DecisionTreeClassifier()
lda= LinearDiscriminantAnalysis()
lor= LogisticRegression()


models=[dtc,lda,lor]

accuracy_train=[]
accuracy_test=[]


for i in models:  # Computation of RMSE and R2 values 
    i.fit(x_train,y_train)
    accuracy_train.append(accuracy_score(y_train,i.predict(x_train)))
    accuracy_test.append(accuracy_score(y_test,i.predict(x_test)))
        
print(pd.DataFrame({'Train Accuracy': accuracy_train,'Test Accuracy': accuracy_test},
            index=['Decision Tree Classifier','LDA','Logistic Regression']))
# =============================================================================================================

lr_trained_metrics = []
lda_trained_metrics = []
lr_test_metrics = []
lda_test_metrics = []

lr_trained_metrics.append(accuracy_score(y_train,grid_search1.predict(X_train)))
lr_trained_metrics.append(precision_score(y_train,grid_search1.predict(X_train)))
lr_trained_metrics.append(recall_score(y_train,grid_search1.predict(X_train)))
lr_trained_metrics.append(f1_score(y_train,grid_search1.predict(X_train)))

lr_test_metrics.append(accuracy_score(y_test,grid_search1.predict(X_test)))
lr_test_metrics.append(precision_score(y_test,grid_search1.predict(X_test)))
lr_test_metrics.append(recall_score(y_test,grid_search1.predict(X_test)))
lr_test_metrics.append(f1_score(y_test,grid_search1.predict(X_test)))

lda_trained_metrics.append(accuracy_score(y_train,grid_search2.predict(X_train)))
lda_trained_metrics.append(precision_score(y_train,grid_search2.predict(X_train)))
lda_trained_metrics.append(recall_score(y_train,grid_search2.predict(X_train)))
lda_trained_metrics.append(f1_score(y_train,grid_search2.predict(X_train)))

lda_test_metrics.append(accuracy_score(y_test,grid_search2.predict(X_test)))
lda_test_metrics.append(precision_score(y_test,grid_search2.predict(X_test)))
lda_test_metrics.append(recall_score(y_test,grid_search2.predict(X_test)))
lda_test_metrics.append(f1_score(y_test,grid_search2.predict(X_test)))
        
lr_lda_metrics = pd.DataFrame({'LR Trained Data Metrics': lr_trained_metrics,'LR Test Data Metrics': lr_test_metrics,'LDA Trained Data Metrics': lda_trained_metrics,'LDA Test Data Metrics': lda_test_metrics}, 
                              index=['AccuracyScore','PrecisionScore','RecallScore','F1 Score'])

lr_lda_metrics


# =============================================================================================================

# Hyperparameter Tuning Using GridSearchCV on Regressor
# =====================================================
param_grid = {
    'max_depth': [10,15,20,25,30],#[3,5,7,9]
    'min_samples_leaf': [3, 15,30],#1-4% of train data [42 to 168]
    'min_samples_split': [15,30,35,40,50],#3 time of nodes
}

dtr=tree.DecisionTreeRegressor(random_state=123)

grid_search = GridSearchCV(estimator = dtr, param_grid = param_grid, cv = 3)


grid_search.fit(x_train,y_train)

print(grid_search.best_params_)

# =============================================================================================================

# Hyperparameter Tuning Using GridSearchCV on Classifier
# =====================================================

param_grid = {
    'max_depth': [10,15,20,25,30],
    'min_samples_leaf': [3, 15,30],
    'min_samples_split': [15,30,35,40,50],
    'criterion' :['gini', 'entropy']
}

dtr=tree.DecisionTreeClassifier()

grid_search = GridSearchCV(estimator = dtr, param_grid = param_grid, cv = 3)

grid_search.fit(x_train,y_train)

print(grid_search.best_params_)

# ============================================================================================================

# Hyperparameter Tuning Using RandomizedSearchCV on RandomForest
# ==============================================================

%%time
param_grid = {'n_estimators': [int(x) for x in np.linspace(start = 50, stop = 1000, num = 10)],
              'max_depth' : np.linspace(20, 80, 10, endpoint=True),
              'min_samples_leaf' : [10,20,60], # 1-3% of length of dataset
              'min_samples_split' : [1,3,5,10], # approx 3 times the min_samples_leaf
             }

RFR = RandomForestRegressor(random_state=123)

RF_random = RandomizedSearchCV(estimator = RFR, param_distributions = param_grid, cv = 10,return_train_score=True)

RF_random.fit(X_tr,y_train)
hyperparameter_RF=RF_random.best_params_
print("The best hyperparameter is {} with score of {}".format(hyperparameter_RF,RF_random.best_score_))
# ===============================================================================================================

from sklearn.model_selection import cross_val_score, GridSearchCV

hyperparameter_grid = {
    'solver': ['svd', 'lsqr', 'eigen']
}

lda_model=LinearDiscriminantAnalysis()

grid_search = GridSearchCV(estimator = lda_model, param_grid = hyperparameter_grid, cv = 3)

grid_search.fit(x_train,y_train)

print(grid_search.best_params_)

# ===============================================================================================================




