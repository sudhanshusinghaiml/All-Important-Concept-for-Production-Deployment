# For numpy Arrays 
import numpy as np

# For using pandas DataFrame
import pandas as pd

# For plotting charts
import matplotlib.pyplot as plt
import seaborn as sns

# For plotting in the current window
%matplotlib inline

# To import and initialize stopwords
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# WordCloud
from wordcloud import wordcloud, STOPWORDS
from collections import Counter

# For NLP Libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

# =====================================================================================================
# Get multiple outputs in the same cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# To supress future warnings
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

# Using display setting
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth',2000)
pd.options.display.float_format='{:.2f}'.format

# ====================================================================================================
"""
    Basic Exploration of Text
"""

# Word count in a text without using Lambda
tweets_df['TotalWords'] = [len(x.split()) for x in tweets_df['text'].tolist()]
tweets_df[['text','TotalWords']].head()

# Word count in a text
tweets_df['WordCount'] = tweets_df['text'].apply(lambda x: len(x.split()))
tweets_df[['text','TotalWords','WordCount']].head()

# Number of characters
tweets_df['NumberOfCharacter']= tweets_df['text'].apply(lambda x: len(x))
tweets_df[['text','TotalWords','WordCount','NumberOfCharacter']].head()

# Average Word Length
def average_word(sentence):
    words = sentence.split()
    return (sum(len(word) for word in words))/len(words)

tweets_df['AverageWord_Length'] = tweets_df['text'].apply(lambda x: average_word(x))
tweets_df[['text','TotalWords','WordCount','NumberOfCharacter','AverageWord_Length']].head()

# No of Stopwords
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

tweets_df['No_of_Stopwords'] = tweets_df['text'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
tweets_df[['text','No_of_Stopwords']].head()

# No of Special Characters
tweets_df['Hasgtags'] = tweets_df['text'].apply(lambda x: len([x for x in x.split() if x.startswith('@')]))
tweets_df[['text','Hasgtags']].head()

# Number of Numeric Characters
tweets_df['Numerics'] = tweets_df['text'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
tweets_df[['text','Numerics']].head()

# No of Uppercase characters
tweets_df['Upper_Character'] = tweets_df['text'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
tweets_df[['text','Upper_Character']].head()

# ====================================================================================================

"""
    
"""
from wordcloud import wordcloud, STOPWORDS