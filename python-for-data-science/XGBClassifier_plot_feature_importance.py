"""
	Feature Importance for XGBClassifier
"""

# Extract feature importance
importance_types = ['weight', 'gain', 'cover']
for importance_type in importance_types:
    # print(f"Feature importance ({importance_type}):")
    importance = xgb_classifier.get_booster().get_score(importance_type=importance_type)
    importance_df = pd.DataFrame(importance.items(), columns=['Feature', 'Importance']).sort_values(by='Importance', ascending=False)
    # print(importance_df)

# Function to Visualize feature importance
def plot_feature_importance(importance, title):
    importance_df = pd.DataFrame(importance.items(), columns=['Feature', 'Importance']).sort_values(by='Importance', ascending=False)
    plt.figure(figsize=(10, 6))
    plt.barh(importance_df['Feature'], importance_df['Importance'])
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()
	

# Plot each type of feature importance
for importance_type in importance_types:
    importance = xgb_classifier.get_booster().get_score(importance_type=importance_type)
    plot_feature_importance(importance, f"Feature importance ({importance_type})")
	

# Optionally, you can use the built-in plot_importance function from xgboost
xgb.plot_importance(xgb_classifier, importance_type='weight')
plt.show()

xgb.plot_importance(xgb_classifier, importance_type='gain')
plt.show()

xgb.plot_importance(xgb_classifier, importance_type='cover')
plt.show()

#====================================================================================================


# Sort the important features in descending order.
sorted_index = grid_search_xgb.best_estimator_.feature_importances_.argsort()
important_features_values = grid_search_xgb.best_estimator_.feature_importances_[sorted_index]

# Get the feature names.
feature_names = X_train_encoded.columns[sorted_index]

# Plotting the important features.
fig, ax = plt.subplots(figsize=(12,5))
ax.bar(feature_names, important_features_values)
for label in ax.containers:
    ax.bar_label(label, fmt='%.2f')
ax.set_xlabel('Feature Importance')
ax.set_ylabel('Feature Name')
ax.set_title('Feature Importance of GridSearchCV')
ax.set_xticks(sorted_index)
ax.set_xticklabels(feature_names, rotation=45, ha='right')
plt.show();