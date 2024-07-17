# ========================================
# Scaling and Different Types of Scaling:
# ========================================

#Data Preparation for Scaling
#============================
# Updating categorical and numerical columns in the list

    categorical_variables=[]
    continuous_variables=[]
    for i in df.columns:
        if df[i].dtype=="object":
            categorical_variables.append(i)
        else:
            continuous_variables.append(i)
            
    print(categorical_variables) 
    print(continuous_variables)


# MinMaxScaler() Scaling:
# =======================
# Scaling the variables as continuous variables have different weightage using min-max technique.

    # Method -I
    # =========
    
        df[continuous_variables] = df[continuous_variables].apply(lambda x:(x-x.min()) / (x.max()-x.min()))

    # Method -II
    # ==========

        col_name = continuous_variables
        
        from sklearn import preprocessing
        mm_scaling = preprocessing.MinMaxScaler()
        df_mm_scaled = mm_scaling.fit_transform(df[col_name])
        df_mm_scaled = pd.DataFrame(df_mm_scaled, columns = col_name)


# RobustScaler() Scaling:
# =======================
    from sklearn import preprocessing
    
    col_name = continuous_variables
    
    rs_scaling = preprocessing.RobustScaler()
    df_rs_scaled = rs_scaling.fit_transform(df[col_name])
    df_rs_scaled = pd.DataFrame(df_rs_scaled, columns = col_name)


# StandardScaler() Scaling:
# =========================
# Scaling only continuous columns

    columns_to_scale = continuous_variables

    from sklearn.preprocessing import StandardScaler
    standard_scaler = StandardScaler()
    continuous_scaled_data = standard_scaler.fit_transform(df[columns_to_scale])
    continuous_scaled_data
    
    continuous_scaled_df = pd.DataFrame(continuous_scaled_data, columns= columns_to_scale)
    continuous_scaled_df.head(10)


# Z-Score Scaling:
# ================
    from scipy.stats import zscore
    
    columns_to_scale = continuous_variables
    
    data_scaled=df[columns_to_scale].apply(zscore)
    data_scaled.head()
    data_scaled.describe()
