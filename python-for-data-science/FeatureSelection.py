# Feature Selection
# =================
    """
        Feature selection is the process of selecting a subset of relevant features (variables, predictors) for use in model construction.
        
        The goal of feature selection techniques in machine learning is to find the best set of features that allows one to build optimized models of studied phenomena.
    """
    
# RFE - Recursive Feature Elimination
# ===================================
    """
        The sklearn.feature_selection module implements feature selection algorithms. It currently includes univariate filter selection methods and the recursive feature elimination algorithm.
        
        Given an external estimator that assigns weights to features (e.g., the coefficients of a linear model), the goal of recursive feature elimination (RFE) is to select features by recursively considering smaller and smaller sets of features. First, the estimator is trained on the initial set of features and the importance of each feature is obtained either through any specific attribute or callable. Then, the least important features are pruned from current set of features. That procedure is recursively repeated on the pruned set until the desired number of features to select is eventually reached.
    """
    
    # Creating feature-set and target for RFE model
    y = df_train['Exited'].values
    X = df_train[categorical_variables + continuous_variables]
    X.columns = categorical_variables + continuous_variables
    
    # =========================
    # Logistic Regression
    # =========================
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression
    
    lr_estimator = LogisticRegression()
    num_features_to_select = 10
    
    lr_rfe = RFE(estimator=lr_estimator, n_features_to_select= num_features_to_select) 
    lr_rfe = lr_rfe.fit(X.values, y)  
    print(lr_rfe.support_)
    print(lr_rfe.ranking_)
    
    mask = lr_rfe.support_.tolist()
    lr_selected_features = [b for a,b in zip(mask, X.columns) if a]
    lr_selected_features
    
    
    # =========================
    # Decision Tree Classifier
    # =========================

    from sklearn.feature_selection import RFE
    from sklearn.tree import DecisionTreeClassifier
    
    # for Decision Tree Classifier
    dt_estimator = DecisionTreeClassifier()
    num_features_to_select = 10
    
    # for Decision Tree Classifier
    dt_rfe = RFE(estimator=dt_estimator, n_features_to_select= num_features_to_select) 
    dt_rfe = dt_rfe.fit(X.values, y)  
    print(dt_rfe.support_)
    print(dt_rfe.ranking_)
    
    mask = dt_rfe.support_.tolist()
    dt_selected_features = [b for a,b in zip(mask, X.columns) if a]
    dt_selected_features