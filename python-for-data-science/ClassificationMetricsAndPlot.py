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