from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge_model = Ridge(random_state=123)

param_grid = {'alpha': np.logspace(-4, 4, 50)}

# Perform grid search with cross-validation
ridge_grid_search = GridSearchCV(ridge_model, param_grid, cv=3, scoring='neg_mean_squared_error')

ridge_grid_search.fit(X_train_scaled, y_train2)

# Get the best model
best_ridge = ridge_grid_search.best_estimator_

ridge_train_predicted = best_ridge.predict(X_train_scaled)

ridge_test_predicted = best_ridge.predict(X_test_scaled)

ridge_train_rmse = np.sqrt(metrics.mean_squared_error(y_train2, ridge_train_predicted))
ridge_test_rmse = np.sqrt(metrics.mean_squared_error(y_test2, ridge_test_predicted))

ridge_train_mae = metrics.mean_absolute_error(y_train2, ridge_train_predicted)
ridge_test_mae = metrics.mean_absolute_error(y_test2, ridge_test_predicted)

ridge_train_r2 = metrics.r2_score(y_train2, ridge_train_predicted)
ridge_test_r2 = metrics.r2_score(y_test2, ridge_test_predicted)

print("RMSE for training data: {}".format(ridge_train_rmse))
print("RMSE for test data: {}".format(ridge_test_rmse)) 

print("\nMAE for training data: {}".format(ridge_train_mae))
print("MAE for test data: {}".format(ridge_test_mae))

print("\nR-Square for training data: {}".format(ridge_train_r2))
print("R-Square for test data: {}".format(ridge_test_r2))

best_ridge.coef_