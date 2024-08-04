from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso_model = Lasso(random_state=123)

param_grid = {'alpha': np.logspace(-4, 4, 50)}

# Perform grid search with cross-validation
lasso_grid_search = GridSearchCV(lasso_model, param_grid, cv=3, scoring='neg_mean_squared_error')

lasso_grid_search.fit(X_train_scaled, y_train2)

# Get the best model
best_lasso = lasso_grid_search.best_estimator_

lasso_train_predicted = lasso_grid_search.predict(X_train_scaled)

lasso_test_predicted = lasso_grid_search.predict(X_test_scaled)

lasso_train_rmse = np.sqrt(metrics.mean_squared_error(y_train2, lasso_train_predicted))
lasso_test_rmse = np.sqrt(metrics.mean_squared_error(y_test2, lasso_test_predicted))

lasso_train_mae = metrics.mean_absolute_error(y_train2, lasso_train_predicted)
lasso_test_mae = metrics.mean_absolute_error(y_test2, lasso_test_predicted)

lasso_train_r2 = metrics.r2_score(y_train2, lasso_train_predicted)
lasso_test_r2 = metrics.r2_score(y_test2, lasso_test_predicted)

print("RMSE for training data: {}".format(lasso_train_rmse))
print("RMSE for test data: {}".format(lasso_test_rmse)) 

print("\nMAE for training data: {}".format(lasso_train_mae))
print("MAE for test data: {}".format(lasso_test_mae))

print("\nR-Square for training data: {}".format(lasso_train_r2))
print("R-Square for test data: {}".format(lasso_test_r2))

best_lasso.coef_