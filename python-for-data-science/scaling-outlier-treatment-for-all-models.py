It's bad practice to remove data points simply to produce a better fitting model or statistically significant results. If the extreme value is a legitimate observation that is a natural part of the population you're studying, you should leave it in the dataset.

List of Machine Learning algorithms which are sensitive to outliers:
1- Linear Regression
2- Logistic Regression
3- Support Vector Machine
4- K- Nearest Neighbors
5- K-Means Clustering
6- Hierarchical Clustering
7- Principal Component Analysis

List of Machine Learning algorithms which are not sensitive to outliers:
1- Decision Tree
2- Random Forest
3- XGBoost
4- AdaBoost
5- Naive Bayes

K-means Clustering
===================
Outlier Treatment
------------------
Even though the outliers were about 2 percent of non-outliers which is common in real world data sets, they had a significant impact on clustering. The K-Means clustering algorithm is most sensitive to outliers as it uses the mean of cluster data points to find the cluster center. Hence it is better to identify and remove outliers before applying K-means clustering algorithm.


Logistic Regression
====================
Outlier Treatment
----------------
Logistic Regression models are not much impacted due to the presence of outliers because the sigmoid function tapers the outliers. But the presence of extreme outliers may somehow affect the performance of the model and lowering the performance.

Scaling
-------
Feature scaling is not required for Logistic Regression, but it can be beneficial in a number of scenarios.

LDA - Linear Discriminant Analysis
==================================
Outlier Treatment
-----------------
Although outliers exists as per the boxplot, by looking at the data distribution in describe(), the values are not too far away. Treating the outliers by converting them to min/max values will cause most variables to have values to be the same. So, outliers are not treated in this case.

Scaling
-------
Linear Discriminant Analysis (LDA) finds it's coefficients using the variation between the classes (check this), so the scaling doesn't matter either


Decision Tree Classifier - CART Model
======================================
Outlier Treatment
-----------------
Decision Trees are not sensitive to noisy data or outliers since extreme values or outliers never cause much reduction in the Residual Sum of Squares(RSS) because they are never involved in the split. Decision Trees are generally robust to outliers. Due to their tendency to overfit, they are prone to sampling errors.

Decision trees classification is not impacted by the outliers in the data as the data is split using scores which are calculated using the homogeneity of the resultant data points.

Scaling
--------
Decision trees and ensemble methods do not require feature scaling to be performed as they are not sensitive to the the variance in the data.



Gaussian Naive Bayes
======================
Outlier Treatment
-----------------
In Gaussian Naive Bayes, outliers will affect the shape of the Gaussian distribution and have the usual effects on the mean etc. So depending on our use case, it makes sense to remove outlier.

Scaling
-------
For naive bayes algorithm while calculating likelihoods of numerical features it assumes the feature to be normally distributed and then we calculate probability using mean and variance of that feature only and also it assumes that all the predictors are independent to each other. Scale doesn’t matter. Performing a features scaling in this algorithms may not have much effect.


K- Nearest Neighbhor Algorithm
===============================
Outlier Treatment
------------------
The proposed kNN method detects outliers by exploiting the relationship among neighborhoods in data points. The farther a data point is beyond its neighbors, the more possible the data is an outlier. Due to this, KNN will perform exceptionally well on the training dataset but will misclassify many points on the test dataset (unseen data). This is considered as overfitting, and therefore, KNN is sensitive to outliers.

One of the many issues that affect the performance of the kNN algorithm is the choice of the hyperparameter k. If k is too small, the algorithm would be more sensitive to outliers

Scaling
--------
KNN performance usually requires preprocessing of data to make all variables similarly scaled and centered. 
So, we must apply zscore on continues columns and see the performance for KNN Algorithm.

Convert the features into z scores as we do not know what units / scales were used and store them in new dataframe. It is always adviced to scale numeric attributes in models that calculate distances.


