# Linear Regression using sklearn
# ================================

# For Linear Regression
from sklearn.linear_model import LinearRegression

# For splitting the dataset into train and test data
from sklearn.model_selection import train_test_split

# statsmodels for Linear Regression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Splitting the Independent Variable and Target Variables
# =======================================================
    X = user_data.drop('usr',axis=1)
    Y = user_data['usr']
    # let's add the intercept to data
    X = sm.add_constant(X)
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.30, random_state=1)
    
    sklearn_model = LinearRegression()
    sklearn_model.fit(X_train,y_train)
    for idx, col_name in enumerate(X_train.columns):
        print("The coefficient for {} is {}".format(col_name, sklearn_model.coef_[idx]))
    
    # Let us check the intercept for the model
    intercept = sklearn_model.intercept_
    print("The intercept for our model is {}".format(intercept))


# R square for Linear Regression Data
# ===================================
    skl_accuracy1 = sklearn_model.score(X_train,y_train)
    skl_accuracy2 = sklearn_model.score(X_test,y_test)
    
    prediction_on_training_data = sklearn_model.fit(X_train,y_train).predict(X_train)
    prediction_on_test_data = sklearn_model.fit(X_train,y_train).predict(X_test)
    
    skl_rmse1 = np.sqrt(metrics.mean_squared_error(y_train,prediction_on_training_data))
    skl_rmse2 = np.sqrt(metrics.mean_squared_error(y_test,prediction_on_test_data))
    
    skl_mae1 = mean_absolute_error(y_train, prediction_on_training_data)
    skl_mae2 = mean_absolute_error(y_test, prediction_on_test_data)
    
    print(f'R Square on training data is {skl_accuracy1}')
    print(f'R Square on test data is {skl_accuracy2}')
    print(f'RMSE on training data is {skl_rmse1}')
    print(f'RMSE on test data is {skl_rmse2}')
    print(f'MAE on training data is {skl_mae1}')
    print(f'MAE on test data is {skl_mae2}')

# Linear Equation for Linear Regression using sklearn
# ====================================================
    intercept = sklearn_model.intercept_
    for idx, col_name in enumerate(X_train.columns):
        if idx == 0:
            print(f'usr = {intercept}', end='+ ')
        print(f'{round(sklearn_model.coef_[idx],7)}*({col_name})', end='+ ')
    
# ================================================================================

# Linear Regression using stats model
# =======================================
    ols_model = sm.OLS(y_train,X_train).fit()
    print(ols_model.summary())
    
    prediction_on_training_data = ols_model.predict(X_train)
    print(f'RMSE on training data is {np.sqrt(metrics.mean_squared_error(y_train,prediction_on_training_data))}')


# Check for multicollinearity - Variation Inflation Factor
# ========================================================
    """
        Variance Inflation factor: Variance inflation factors measure the inflation in the variances of the regression coefficients estimates due to collinearities that exist among the predictors. It is a measure of how much the variance of the estimated regression coefficient β_k is "inflated" by the existence of correlation among the predictor variables in the model.
        
        General Rule of Thumb:
        
        If VIF is 1, then there is no correlation among the kth predictor and the remaining predictor variables, and hence, the variance of β_k is not inflated at all.
        
        If VIF exceeds 5, we say there is moderate VIF, and if it is 10 or exceeding 10, it shows signs of high multi-collinearity. The purpose of the analysis should dictate which threshold to use
    
    """

    vif_series = pd.Series([variance_inflation_factor(X_train.values,i) for i in range(X_train.shape[1])], index=X_train.columns)
    print("VIF values: \n\n{}\n".format(vif_series))
    
    
    X_train2 = X_train.drop('pgscan',axis=1)
    ols_model2 = sm.OLS(y_train,X_train2).fit()
    print("R-squared:", np.round(ols_model2.rsquared,3),"\nAdjusted R-squared:",np.round(ols_model2.rsquared_adj, 3),)
    
    print(ols_model2.summary())
    
    # ==========================================================================================================

    """
    Since there is no effect on adj. R-squared after dropping the 'pgscan' column, we can remove it from the training set.
    
    VIF for all the features is less than 5. It means that we have reduced strong collinearity in the model
    
    There are no features with p-value greater than 0.05 so ols_model31 doesn't have any insignificant features
    
    After dropping the features causing strong multicollinearity and the statistically insignificant ones, our model performance hasn't dropped sharply (adj. R-squared has dropped from 0.795 to 0.792). This shows that the variables that were dropped did not have much predictive power.
    """

# Using the model for making predictions on the test data.
# ========================================================

    y_predicted_test= ols_model31.predict(X_test2)
    
    # let us create the dataframe with actual, fitted and residual values
    df_predicted = pd.DataFrame()
    
    df_predicted["Actual Values"] = y_train.values.flatten()  # actual values
    df_predicted["Fitted Values"] = ols_model31.fittedvalues.values  # predicted values
    df_predicted["Residuals"] = ols_model31.resid.values  # residuals
    
    df_predicted.head()
    
    # let's check the RMSE on the train and test data 
    ols_rmse1 = np.sqrt(mean_squared_error(y_train, df_predicted["Fitted Values"]))
    ols_rmse2 = np.sqrt(mean_squared_error(y_test, y_predicted_test))
    
    # let's check the MAE on the train and test data
    ols_mae1 = mean_absolute_error(y_train, df_predicted["Fitted Values"])
    ols_mae2 = mean_absolute_error(y_test, y_predicted_test)
    
    print(f'RMSE on training data is - {ols_rmse1}')
    print(f'RMSE on test data is - {ols_rmse2}')
    print(f'MAE on training data is - {ols_mae1}')
    print(f'MAE on test data is - {ols_mae2}')

# =================================
# Assumptions of Linear Regressions
# =================================
    """ 1. Linearity
    
    TEST FOR LINEARITY AND INDEPENDENCE
    Why the test?  - Linearity describes a straight-line relationship between two variables, predictor variables must have a linear relation with the dependent variable.
    
    How to check linearity?
    
    Make a plot of fitted values vs residuals. If they don't follow any pattern (the curve is a straight line), then we say the model is linear otherwise model is showing signs of non-linearity.
    
    How to fix if this assumption is not followed?
    
    We can try different transformations
    """
    # let us plot the fitted values vs residuals
    sns.set_style("whitegrid")
    sns.residplot(
        data=df_pred, x="Fitted Values", y="Residuals", color="purple", lowess=True
    )
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Fitted vs Residual plot")
    plt.show()
    
    # using square transformation
    X_train8["weight_sq"] = np.square(X_train8["weight"])
    
    # let's create a model with the transformed data
    ols_model32 = sm.OLS(y_train, X_train8)
    ols_model32 = ols_model31.fit()
    print(ols_model32.summary())
    
    
    # let us recreate the dataframe with actual, fitted and residual values
    df_pred = pd.DataFrame()
    
    df_predicted["Actual Values"] = y_train.values.flatten()  # actual values
    df_predicted["Fitted Values"] = ols_model32.fittedvalues.values  # predicted values
    df_predicted["Residuals"] = ols_model32.resid.values  # residuals
    
    df_pred.head()
    
    # let us plot the fitted values vs residuals
    sns.set_style("whitegrid")
    sns.residplot(
        data=df_pred, x="Fitted Values", y="Residuals", color="purple", lowess=True
    )
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Fitted vs Residual plot")
    plt.show()
    
# ======================================================
# 2. Multicollinearity - Already demonstrated using VIF
# ======================================================


# ===============
# 3. Normality - 
# ===============
    """
    Normality 
    =========
    What is the test? - Error terms/residuals should be normally distributed.
    
    If the error terms are not normally distributed, confidence intervals may become too wide or narrow. Once confidence interval becomes unstable, it leads to difficulty in estimating coefficients based on minimization of least squares.
    
    What does non-normality indicate? - It suggests that there are a few unusual data points which must be studied closely to make a better model.
    
    How to check the Normality? - It can be checked via QQ Plot - residuals following normal distribution will make a straight line plot, otherwise not. Another test to check for normality is the Shapiro-Wilk test.
    
    How to Make residuals normal? - We can apply transformations like log, exponential, arcsinh, etc as per our data.
    """
    
    sns.histplot(df_predicted["Residuals"], kde=True)
    plt.title("Normality of residuals")
    plt.show()
    
    # The QQ plot of residuals can be used to visually check the normality assumption. The normal probability plot of residuals should approximately follow a straight line.
    
    import pylab
    import scipy.stats as stats
    
    stats.probplot(df_predicted["Residuals"], dist="norm", plot=pylab)
    plt.show()
    
    """
    Most of the points are lying on the straight line in QQ plot

    The Shapiro-Wilk test can also be used for checking the normality. The null and alternate hypotheses of the test are as follows:

        Null hypothesis - Data is normally distributed.
        Alternate hypothesis - Data is not normally distributed.
    """
    
    stats.shapiro(df_predicted["Residuals"])
    
    """
    Since p-value < 0.05, the residuals are not normal as per shapiro test.
    Strictly speaking - the residuals are not normal. However, as an approximation, we might be willing to accept this distribution as close to being normal
    """
    
    
# =====================================
# 4. Autocorrelation of the Residuals
# =====================================

# =====================
# 5. Homoscedasticity 
# =====================
    """
    TEST FOR HOMOSCEDASTICITY
    =========================
    Homoscedacity - If the variance of the residuals are symmetrically distributed across the regression line , then the data is said to homoscedastic.
    
    Heteroscedacity - If the variance is unequal for the residuals across the regression line, then the data is said to be heteroscedastic. In this case the residuals can form an arrow shape or any other non symmetrical shape.
    
    Why the test? - The presence of non-constant variance in the error terms results in heteroscedasticity. Generally, non-constant variance arises in presence of outliers.
    
    How to check if model has Heteroscedasticity? - Can use the goldfeldquandt test. If we get p-value > 0.05 we can say that the residuals are homoscedastic, otherwise they are heteroscedastic.
    
    How to deal with Heteroscedasticity? - Can be fixed via adding other important features or making transformations.
    The null and alternate hypotheses of the goldfeldquandt test are as follows:
    
    Null hypothesis : Residuals are homoscedastic
    Alternate hypothesis : Residuals have hetroscedasticity
    """

    import statsmodels.stats.api as sms
    from statsmodels.compat import lzip
    name = ["F statistic", "p-value"]
    test = sms.het_goldfeldquandt(df_pred["Residuals"], X_train8)
    lzip(name, test)
    
    # Since p-value > 0.05 we can say that the residuals are homoscedastic

# ===========================================================================================
# Hyperparameter Tuning Using GridSearchCV on Regressor - ((Test it for Linear Regressoion))
# ===========================================================================================
param_grid = {
    'max_depth': [10,15,20,25,30],#[3,5,7,9]
    'min_samples_leaf': [3, 15,30],#1-4% of train data [42 to 168]
    'min_samples_split': [15,30,35,40,50],#3 time of nodes
}

dtr=tree.DecisionTreeRegressor(random_state=123)
grid_search = GridSearchCV(estimator = dtr, param_grid = param_grid, cv = 3)
grid_search.fit(x_train,y_train)
print(grid_search.best_params_)

# ============================================================================================