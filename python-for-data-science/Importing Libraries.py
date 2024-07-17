# For numpy Arrays 
import numpy as np

# For using pandas DataFrame
import pandas as pd

# For plotting charts
import matplotlib.pyplot as plt
import seaborn as sns

# For plotting in the current window
%matplotlib inline

# Get multiple outputs in the same cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# To supress future warnings
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

# For scaling using zscore
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth',2000)
pd.options.display.float_format='{:.2f}'.format
# ===========================================================================================================
""" 
    Linear Regression
"""
# ===========================================================================================================

# -------------Linear Regression-----------------
from sklearn.linear_model import LinearRegression

# ---------Splitting the dataset--------------------
from sklearn.model_selection import train_test_split

# -----------------Statsmodels for Linear Regression----------------------
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# ===========================================================================================================
"""
    Logistic Regression, Linear Discriminant Analysis and Classification and Regression Tree
"""
# ===========================================================================================================


# ---------Logistic Regression---------------------
from sklearn.linear_model import LogisticRegression

# ---------Linear Discriminant Analysis-----------------------------
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# ---------Decision Tree Classifier -----------
from sklearn.tree import DecisionTreeClassifier

# ---------Evaluating Performance Metrics-------
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# ============================================================================================================
""" 
    Random Forest, Bagging, Out of Bagging Error, Adaptive Boosting and GradientBoosting
"""
# =============================================================================================================

# ----------------- Naive Bayes -----------------
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB

# ----------KNN Classification--------------------
from sklearn.neighbors import KNeighborsClassifier

# -------------CrossValidation--------------------
from sklearn.model_selection import cross_val_score, KFold

# ---------------RandomForest Classifier ----------
from sklearn.ensemble import RandomForestClassifier

# ------------Bagging Classifier -------------
from sklearn.ensemble import BaggingClassifier

# ----------------Adaptive Boosting------------
from sklearn.ensemble import AdaBoostClassifier

# ----------------Gradient Boosting-------------------
from sklearn.ensemble import GradientBoostingClassifier

# ------------Support Vector Machine-------------------
from sklearn.svm import SVC

# ----------Xtreme Gradient Boosting ------------------
from xgboost import XGBClassifier

# ----------Extra Trees Classifier ------------------
from sklearn.ensemble import ExtraTreesClassifier

# ----------Light GBM Classifier---------------------
from lightgbm import LGBMClassifier

# ------------Voting Classifier------------------------
from sklearn.ensemble import VotingClassifier

# ---------Evaluating Performance Metrics-------
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# DT does not take strings as input for the model fit step....
from sklearn.feature_extraction.text import CountVectorizer  
from IPython.display import Image  
#import pydotplus as pydot
from sklearn import tree
from os import system

# =========================================================================
"""
    Tuning the Models
"""
# =========================================================================

# ----------GridSearch Tuning --------------
from sklearn.model_selection import GridSearchCV

# ----------Randomized Search Tuning --------------
from sklearn.model_selection import RandomizedSearchCV

# ----------Make Pipeline------------
from sklearn.pipeline import Pipeline

# ---------SMOTE for OvrSampling----------------
from imblearn.over_sampling import SMOTE


# ==========================================================================
"""
    Splitting the train test data
"""

## Keeping aside a test/holdout set
df_train_val, df_test, y_train_val, y_test = train_test_split(df, y.ravel(), test_size = 0.2, random_state = 42)

## Splitting into train and validation set
df_train, df_val, y_train, y_val = train_test_split(df_train_val, y_train_val, test_size = 0.12, random_state = 42)

df_train.shape, df_val.shape, df_test.shape, y_train.shape, y_val.shape, y_test.shape
np.mean(y_train), np.mean(y_val), np.mean(y_test)

# ==========================================================================