"""
 1. Label Encoding ---> Binary categorical variables and Ordinal variables
 2. One-Hot Encoding ---> Non-ordinal categorical variables with low to mid cardinality (< 5-10 levels)
 3. Target encoding ---> Categorical variables with > 10 levels

"""
# ================================================
#  Enoding and Different Type of Encoding methods
# ================================================
# Data Preparation for Encoding
# =============================

# Updating categorical and numerical columns in the list

    cat=[]
    num=[]
    for i in df.columns:
        if df[i].dtype=="object":
            cat.append(i)
        elif df[i].dtype=="int" & df[i].dtype=="float":
            num.append(i)
    print(cat) 
    print(num)

# On-hot Encoding (Dummy Encoding)
# ================================
    # Method - 1
    # ===========
    
    """
        One Hont Encoder doesnot accept DataFrame. It accepts series and transforms it to codes 
    """
    
    from sklearn.preprocessing import LabelEncoder
    label_encoder_geography = LabelEncoder()
    geography_series = label_encoder_geography.fit_transform(df['Geography'])
    
    from sklearn.preprocessing import OneHotEncoder

    ohe = OneHotEncoder(handle_unknown = 'ignore', sparse=False)
    ohe_geography= ohe.fit_transform(geography_series.reshape(df.shape[0],1))
    ohe_geography.astype(int)
    
    encoded_colum_name = ['Country_' + i for i in label_encoder_geography_mapping.keys()]
    encoded_colum_name
    
    df = pd.concat([df, pd.DataFrame(ohe_geography.astype(int), columns= encoded_colum_name)], axis=1)
    df.drop('Geography',axis=1, inplace=True)
    df.head(10)
    df.tail(10)
    

    #Method - 2
    #===========
    
    """
    One-Hot-Encoding is used to create dummy variables to replace the categories in a categorical variable into features of each category and represent it using 1 or 0 based on the presence or absence of the categorical value in the record.
    
    This is required to do since the machine learning algorithms only works on the numerical data. That is why there is a need to convert the categorical column into numerical one.
    
    get_dummies is the method which creates dummy variable for each categorical variable.
    
    It is considered a good practice to set parameter drop_first as True whenever get_dummies is used. It reduces the chances of multicollinearity which will be covered in coming courses and the number of features are also less as compared to drop_first=False
    """
    
    cat = ["MARITAL STATUS", "SEX","EDUCATION","JOB","USE","CAR TYPE","CITY"]
    
    df2 = pd.get_dummies(df, columns=cat,drop_first=True)
    
    df2.head()
    
  
    dummies = pd.get_dummies(df[["MARITAL STATUS", "SEX","EDUCATION","JOB","USE","CAR TYPE","CITY"]], columns=["MARITAL STATUS", "SEX","EDUCATION","JOB","USE","CAR TYPE","CITY"], prefix=["married", "sex","Education","Job","Use","cartype","city"],drop_first=True)
    
    dummies.head()
    
    columns=["MARITAL STATUS", "SEX","EDUCATION","JOB","USE","CAR TYPE","CITY"]
    df = pd.concat([df, dummies], axis=1)
    
    # drop original column "fuel-type" from "df"
    df.drop(columns, axis = 1, inplace=True)

    # Method -3 
    # =============
    '''one hot encoding for categorical features: Fuel Type'''
    vectorizer=CountVectorizer()
    
    X_train_Fuel_Type = vectorizer.fit_transform(X_train['Fuel_Type'].values)
    #fit will happen on train  data then we use the fitted CountVectorizer to convert the text to vector
    
    X_test_Fuel_Type = vectorizer.transform(X_test['Fuel_Type'].values)


#Label / Ordinal Encoding
#=========================
    """
    There are two types of categorical data
    
    Ordinal: Order based like 'good','bad','worst' or Clothing sizes
    Nominal: Without any order or ranks like city names, Genders, etc
    
    You are free to use any encoding technique as long as it works.
    
    Also, rememeber that on Official Site of Scikit-learn's Label Encoder it is mentioned that "This transformer should be used to encode target values, i.e. y, and not the input X.
    
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
    
    """

    # Method - 1
    # ===========
    
    from sklearn.preprocessing import LabelEncoder
    label_encoder_gender = LabelEncoder()
    df['Gender'] = label_encoder_gender.fit_transform(df['Gender'])
    
    label_encoder_gender.classes_
    
    label_encoder_gender_mapping = dict(zip(label_encoder_gender.classes_, label_encoder_gender.transform(label_encoder_gender.classes_)))

    label_encoder_gender_mapping
    
    df.head(10)

    # Method - 2
    # ===========
    for feature in attrition_train_df.columns: 
        if attrition_train_df[feature].dtype == 'object': 
            print('\n')
            print('feature:',feature)
            print(pd.Categorical(attrition_train_df[feature].unique()))
            print(pd.Categorical(attrition_train_df[feature].unique()).codes)
            attrition_train_df[feature] = pd.Categorical(attrition_train_df[feature]).codes
            
    attrition_train_df.info()


# Binary Encoding
# ================
    """
    Binary encoding is a technique used to transform categorical data into numerical data by encoding categories as integers and then converting them into binary code.
    """
    
    from category_encoder import BinaryEncoder
    
    BinaryEncoder(cols=['player']).fit(df).transform(df)

# Custom Encoder
# ==========================
    ## How we can encode ordinal categorical features in Python 

    platform_mapper = {'Convinient':4, 'Inconvinient':1, 'manageable':3, 'need improvement':2, 'very convinient':5, 'very inconvinient':0}
    df['Platform_location'] = df['Platform_location'].replace(platform_mapper)
    df.head()


# Target Encoding
# ================
    """
    Target Encoding
    
    https://www.kaggle.com/code/ryanholbrook/target-encoding
    
    A target encoding is any kind of encoding that replaces a feature's categories with some number derived from the target.

    A simple and effective version is to apply a group aggregation from Lesson 3, like the mean. Using the Automobiles dataset, this computes the average price of each vehicle's make
    
    
        Use Cases for Target Encoding
        
        Target encoding is great for:
        =============================
            High-cardinality features:
            ==========================
            A feature with a large number of categories can be troublesome to encode: a one-hot encoding would generate too many features and alternatives, like a label encoding, might not be appropriate for that feature. A target encoding derives numbers for the categories using the feature's most important property: its relationship with the target.
        
            Domain-motivated features:
            ==========================
            From prior experience, you might suspect that a categorical feature should be important even if it scored poorly with a feature metric. A target encoding can help reveal a feature's true informativeness.
    """

    X = df.copy()
    y = X.pop('Rating')
    
    X_encode = X.sample(frac=0.25)
    y_encode = y[X_encode.index]
    X_pretrain = X.drop(X_encode.index)
    y_train = y[X_pretrain.index]
    
    
    from category_encoders import MEstimateEncoder
    
    # Create the encoder instance. Choose m to control noise.
    encoder = MEstimateEncoder(cols=["Zipcode"], m=5.0)
    
    # Fit the encoder on the encoding split.
    encoder.fit(X_encode, y_encode)
    
    # Encode the Zipcode column to create the final training data
    X_train = encoder.transform(X_pretrain)

    
    # Mean Encoding or Leave-One-Out Encoding
    # ========================================
    """
    This kind of target encoding is sometimes called a mean encoding. Applied to a binary target, it's also called bin counting. (Other names you might come across include: likelihood encoding, impact encoding, and leave-one-out encoding.
    """
    
    # Method - I
    # ==========
    autos["make_encoded"] = autos.groupby("make")["price"].transform("mean")

    autos[["make", "price", "make_encoded"]].head(10)
    
    # Method - II
    # ============
    
    surname_means = df.groupby(['Surname']).Exited.mean()
    surname_means.head()
    global_mean = surname_means.mean()
    
    ## Creating new encoded features for surname - Target (mean) encoding
    df['Surname_mean_churn'] = df.Surname.map(surname_means)
    df['Surname_mean_churn'].fillna(global_mean, inplace=True)
    
    """
        Trying Leave-One-Out Encoding
    """
    ## Calculate frequency of each category
    surname_freqs = df.groupby(['Surname']).size()
    surname_freqs.head()
    
    ## Create frequency encoding - Number of instances of each category in the data
    df['Surname_freqs'] = df.Surname.map(surname_freqs)
    df['Surname_freqs'].fillna(0, inplace=True)
    
    ## Create Leave-one-out target encoding for Surname
    df['Surname_enc'] = ((df.Surname_freqs * df.Surname_mean_churn) - df.Exited)/(df.Surname_freqs - 1)
    df.head(10)

    ## Fill NaNs occuring due to category frequency being 1 or less
    df['Surname_enc'].fillna((((df.shape[0] * global_mean) - df.Exited) / (df.shape[0] - 1)), inplace=True)
    df.head(10)
    
    ### Deleting the 'Surname' and other redundant column across the three datasets
    df.drop(['Surname_mean_churn'], axis=1, inplace=True)
    df.drop(['Surname_freqs'], axis=1, inplace=True)
    df.drop(['Surname'], axis=1, inplace=True)
    df.head(10)
# ============================================================================================================
