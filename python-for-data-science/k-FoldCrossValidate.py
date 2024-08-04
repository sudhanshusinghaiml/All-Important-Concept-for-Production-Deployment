from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

k_fold = KFold(n_splits=5, shuffle=True, random_state=1234)

model_kfold = LinearRegression()

rmse_train_list = []
mae_train_list = []
r2_train_list = []

rmse_test_list = []
mae_test_list = []
r2_test_list = []

for training_data_index, test_data_index in k_fold.split(X_scaled):
    # Split the data into training and testing sets
    X_train = X_scaled.iloc[training_data_index] 
    X_test = X_scaled.iloc[test_data_index]
    y_train= y.iloc[training_data_index]
    y_test = y.iloc[test_data_index]

    # Training the model
    model_kfold.fit(X_train, y_train)

    # Predict the value for the left-out sample
    y_train_pred = model_kfold.predict(X_train)
    y_test_pred = model_kfold.predict(X_test)

    # Calculating performance metrics - RMSE
    sample_train_rmse = np.sqrt(metrics.mean_squared_error(y_train, y_train_pred))
    rmse_train_list.append(sample_train_rmse)
    
    sample_test_rmse = np.sqrt(metrics.mean_squared_error(y_test, y_test_pred))
    rmse_test_list.append(sample_test_rmse)

    
    # Calculating performance metrics - MAE
    sample_train_mae = metrics.mean_absolute_error(y_train, y_train_pred)
    mae_train_list.append(sample_train_mae)
    
    sample_test_mae = metrics.mean_absolute_error(y_test, y_test_pred)
    mae_test_list.append(sample_test_mae)

    
    # Calculating performance metrics - R2
    sample_train_r2 = metrics.r2_score(y_train, y_train_pred)
    r2_train_list.append(sample_train_r2)
    
    sample_test_r2 = metrics.r2_score(y_test, y_test_pred)
    r2_test_list.append(sample_test_r2)


kfold_train_mean_rmse = np.mean(rmse_train_list)
kfold_train_mean_mae = np.mean(mae_train_list)
kfold_train_mean_r2 = np.mean(r2_train_list)

kfold_test_mean_rmse = np.mean(rmse_test_list)
kfold_test_mean_mae = np.mean(mae_test_list)
kfold_test_mean_r2 = np.mean(r2_test_list)


print("RMSE for training data: {}".format(kfold_train_mean_rmse))
print("RMSE for test data: {}".format(kfold_test_mean_rmse)) 

print("\nMAE for training data: {}".format(kfold_train_mean_mae))
print("MAE for test data: {}".format(kfold_test_mean_mae))

print("\nR-Square for training data: {}".format(kfold_train_mean_r2))
print("R-Square for test data: {}".format(kfold_test_mean_r2))