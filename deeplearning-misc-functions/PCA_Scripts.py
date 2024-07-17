import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Assuming you have a dataset of images stored in a numpy array 'X', where each row represents a flattened image

# Step 1: Flatten each image into a 1D vector
X_flattened = X.reshape(X.shape[0], -1)

# Step 2: Standardize the data
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X_flattened)

# Step 3: Compute the covariance matrix
cov_matrix = np.cov(X_standardized, rowvar=False)

# Step 4: Compute eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 5: Select the top k eigenvectors
k = 100  # Number of principal components to retain
top_k_eigenvectors = eigenvectors[:, :k]

# Step 6: Project data onto principal components
X_projected = np.dot(X_standardized, top_k_eigenvectors)

# Optionally, you can use scikit-learn's PCA implementation
pca = PCA(n_components=k)
X_pca = pca.fit_transform(X_standardized)

# Visualize the explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_
plt.plot(np.cumsum(explained_variance_ratio))
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs. Number of Principal Components')
plt.show()