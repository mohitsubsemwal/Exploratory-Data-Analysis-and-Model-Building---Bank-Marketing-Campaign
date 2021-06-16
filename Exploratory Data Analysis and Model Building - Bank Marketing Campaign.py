#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis and Model Building - Bank Marketing Campaign

# **Data Description**
# 
# This is the classic marketing bank dataset uploaded originally in the UCI Machine Learning Repository. The dataset gives you information about a marketing campaign of a financial institution in which you will have to analyze in order to find ways to look for future strategies in order to improve future marketing campaigns for the bank.
# 
# 

# **What is a Term Deposit?**
# 
# A Term deposit is a deposit that a bank or a financial institurion offers with a fixed rate (often better than just opening deposit account) in which your money will be returned back at a specific maturity time. For more information with regards to Term Deposits please 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#create data drame to read data set
df = pd.read_csv('bank.csv')


# In[3]:


df.head()


# In[4]:


# check the df structe
df.info()


# In[5]:


# find number of rows and column
df.shape


# In[6]:


# describe df numerical columns
df.describe()


# In[7]:


for col in df.select_dtypes(include='object').columns:
    print(col)
    print(df[col].unique())


# **Data Description**
# 
# This is the classic marketing bank dataset uploaded originally in the UCI Machine Learning Repository. The dataset gives you information about a marketing campaign of a financial institution in which you will have to analyze in order to find ways to look for future strategies in order to improve future marketing campaigns for the bank.
# 
# **Feature**
# 1. age | int64 | age in years
# 2. job | object | type of job (categorical: ['admin.' 'technician' 'services' 'management' 'retired' 'blue-collar'
#  'unemployed' 'entrepreneur' 'housemaid' 'unknown' 'self-employed'
#  'student'])
# 3. marital | object | marital status (categorical: ['married' 'single' 'divorced'])
# 4. education | Object | education background (categorical: ['secondary' 'tertiary' 'primary' 'unknown'])
# 5. default | Object | has credit in default?  (categorical: ['no' 'yes'])
# 6. balance | int64 | Balance of the individual
# 7. housing | object | has housing loan? (categorical: ['yes' 'no'])
# 8. loan | object | has personal loan? (categorical: ['no' 'yes'])
# 9. contact | object | contact communication type (categorical: ['unknown' 'cellular' 'telephone'])
# 10. day | int64 | last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
# 11. month | object | last contact month of year (categorical: ['may' 'jun' 'jul' 'aug' 'oct' 'nov' 'dec' 'jan' 'feb' 'mar' 'apr' 'sep'])
# 12. duration | int64 | last contact duration, in seconds (numeric)
# 13. campaign | int64 | number of contacts performed during this campaign and for this client
# 14. pdays | int64 | number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
# 15. previous | int64 | number of contacts performed before this campaign and for this client
# 16. poutcome | object | outcome of the previous marketing campaign (categorical: ['unknown' 'other' 'failure' 'success'])
# 
# **Label**
# 1. deposit | object | has the client subscribed a term deposit? (binary: 'yes','no')

# # Exploratory Data Analysis

# - Find Unwanted Columns
# - Find Missing Values
# - Find Features with one value
# - Explore the Categorical Features
# - Find Categorical Feature Distribution
# - Relationship between Categorical Features and Label
# - Explore the Numerical Features
# - Find Discrete Numerical Features
# - Relation between Discrete numerical Features and Labels
# - Find Continous Numerical Features
# - Distribution of Continous Numerical Features
# - Relation between Continous numerical Features and Labels
# - Find Outliers in numerical features
# - Explore the Correlation between numerical features
# - Find Pair Plot
# - Check the Data set is balanced or not based on target values in classification

# **1. Find Unwanted Columns**

# **Take-away**:
# - these is no unwanted column present in given dataset to remove

# **2. Find Missing Values**

# In[8]:


# find missing values
features_na = [features for features in df.columns if df[features].isnull().sum() > 0]
for feature in features_na:
    print(feature, np.round(df[feature].isnull().mean(), 4),  ' % missing values')
else:
    print("No missing value found")


# **Take-away**:
# - No missing value found

# **3. Find Features with One Value**

# In[9]:


for column in df.columns:
    print(column,df[column].nunique())


# **Take-away**:
# - No feature with only one value

# **4. Explore the Categorical Features**

# In[10]:


categorical_features=[feature for feature in df.columns if ((df[feature].dtypes=='O') & (feature not in ['deposit']))]
categorical_features


# In[11]:


for feature in categorical_features:
    print('The feature is {} and number of categories are {}'.format(feature,len(df[feature].unique())))


# **Take-away**:
# - there are 9 categorical features
# - feature job and month has highest number of categorical values

# **5. Find Categorical Feature Distribution**

# In[12]:


#check count based on categorical features
plt.figure(figsize=(15,80), facecolor='white')
plotnumber =1
for categorical_feature in categorical_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.countplot(y=categorical_feature,data=df)
    plt.xlabel(categorical_feature)
    plt.title(categorical_feature)
    plotnumber+=1
plt.show()


# **Take-away**:
# - client with job type as management records are high in given dataset and housemaid are very less
# - client who married are high in records in given dataset and divorced are less
# - client whoes education background is secondary are in high numbers in given dataset
# - defualt feature seems to be does not play importand role as it has value of no at high ratio to value yes which can drop
# - data in month of may is high and less in dec

# **6. Relationship between Categorical Features and Label**

# In[13]:


#check target label split over categorical features
#Find out the relationship between categorical variable and dependent variable
for categorical_feature in categorical_features:
    sns.catplot(x='deposit', col=categorical_feature, kind='count', data= df)
plt.show()


# In[14]:


#Check target label split over categorical features and find the count
for categorical_feature in categorical_features:
    print(df.groupby(['deposit',categorical_feature]).size())


# **Take-away**:
# - retired client has high interest on deposit
# - client who has housing loan seems to be not interested much on deposit
# - if pre campagin outcome that is poutcome=success then, there is high chance of client to show interest on deposit
# - in month of March, September, October and December, client show high interest to deposit
# - in month of may, records are high but client interst ratio is very less

# **7. Explore the Numerical Features**

# In[15]:


# list of numerical variables
numerical_features = [feature for feature in df.columns if ((df[feature].dtypes != 'O') & (feature not in ['deposit']))]
print('Number of numerical variables: ', len(numerical_features))

# visualise the numerical variables
df[numerical_features].head()


# **Take-away**:
# - there are 7 numerical features

# **8. Find Discrete Numerical Features**

# In[16]:


discrete_feature=[feature for feature in numerical_features if len(df[feature].unique())<25]
print("Discrete Variables Count: {}".format(len(discrete_feature)))


# **Take-away**:
# - there is no Discrete Variables in give dataset

# **9. Relation between Discrete numerical Features and Labels**
# - NA

# **10. Find Continous Numerical Features**

# In[17]:


continuous_features=[feature for feature in numerical_features if feature not in discrete_feature+['deposit']]
print("Continuous feature Count {}".format(len(continuous_features)))


# **Take-away**:
# - there are 7 continuous numerical features

# **11. Distribution of Continous Numerical Features**

# In[18]:


#plot a univariate distribution of continues observations
plt.figure(figsize=(20,60), facecolor='white')
plotnumber =1
for continuous_feature in continuous_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.distplot(df[continuous_feature])
    plt.xlabel(continuous_feature)
    plotnumber+=1
plt.show()


# **Take-away**: 
# - it seems age, days distributed normally
# - balance, duration, compaign, pdays and previous heavely skewed towards left and seems to be have some outliers.

# **12. Relation between Continous numerical Features and Labels**

# In[19]:


#boxplot to show target distribution with respect numerical features
plt.figure(figsize=(20,60), facecolor='white')
plotnumber =1
for feature in continuous_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.boxplot(x="deposit", y= df[feature], data=df)
    plt.xlabel(feature)
    plotnumber+=1
plt.show()


# **Take-away**:
# - client shows interest on deposit who had discussion for longer duration

# **13. Find Outliers in numerical features**

# In[20]:


#boxplot on numerical features to find outliers
plt.figure(figsize=(20,60), facecolor='white')
plotnumber =1
for numerical_feature in numerical_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.boxplot(df[numerical_feature])
    plt.xlabel(numerical_feature)
    plotnumber+=1
plt.show()


# **Take-away**:
# - age, balance, duration, compaign, pdays and previous has some outliers

# **14. Explore the Correlation between numerical features**

# In[21]:


## Checking for correlation
cor_mat=df.corr()
fig = plt.figure(figsize=(15,7))
sns.heatmap(cor_mat,annot=True)


# **Take-away**: 
# - it seems no feature is heavily correlated with other features

# **15. Check the Data set is balanced or not based on target values in classification**

# In[22]:


#total patient count based on cardio_results
sns.countplot(x='deposit',data=df)
plt.show()


# In[23]:


df['deposit'].groupby(df['deposit']).count()


# **Take-away**: 
# - given dataset seems to be balanced. 

# # Feature Engineering

# - Drop unwanted Features
# - Handle Missing Values
# - Handle Categorical Features
# - Handle Feature Scalling
# - Remove Outliers

# As per Exploratory Data Analysis EDA, 
# - no missing value found
# - no feature found with one value
# - 9 categorical features
# - defaut features does not play imp role
# - it seems some outliers found (age, balance, duration, compaign, pdays and previous has some outliers)

# In[24]:


df2=df.copy()


# In[25]:


df2.head()


# In[26]:


df2.shape


# In[29]:


#defaut features does not play imp role
df2.groupby(['deposit','default']).size()


# In[30]:


df2.drop(['default'],axis=1, inplace=True)


# In[31]:


df2.groupby(['deposit','pdays']).size()


# In[32]:


# drop pdays as it has -1 value for around 40%+ 
df2.drop(['pdays'],axis=1, inplace=True)


# In[33]:


# remove outliers in feature age...
df2.groupby('age',sort=True)['age'].count()
# these can be ignored and values lies in between 18 to 95


# In[34]:


# remove outliers in feature balance...
df2.groupby(['deposit','balance'],sort=True)['balance'].count()
# these outlier should not be remove as balance goes high, client show interest on deposit


# In[35]:


# remove outliers in feature duration...
df2.groupby(['deposit','duration'],sort=True)['duration'].count()
# these outlier should not be remove as duration goes high, client show interest on deposit


# In[36]:


# remove outliers in feature campaign...
df2.groupby(['deposit','campaign'],sort=True)['campaign'].count()


# In[37]:


df3 = df2[df2['campaign'] < 33]


# In[38]:


df3.groupby(['deposit','campaign'],sort=True)['campaign'].count()


# In[39]:


# remove outliers in feature previous...
df3.groupby(['deposit','previous'],sort=True)['previous'].count()


# In[40]:


df4 = df3[df3['previous'] < 31]


# In[41]:


cat_columns = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
for col in  cat_columns:
    df4 = pd.concat([df4.drop(col, axis=1),pd.get_dummies(df4[col], prefix=col, prefix_sep='_',drop_first=True, dummy_na=False)], axis=1)


# In[42]:


bool_columns = ['housing', 'loan', 'deposit']
for col in  bool_columns:
    df4[col+'_new']=df4[col].apply(lambda x : 1 if x == 'yes' else 0)
    df4.drop(col, axis=1, inplace=True)


# In[43]:


df4.head()


# # Split Dataset into Training set and Test set

# In[44]:


X = df4.drop(['deposit_new'],axis=1)
y = df4['deposit_new']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)


# In[46]:


len(X_train)


# In[47]:


len(X_test)


# # Model Selection

# In[49]:


# will try to use below two models that are RandomForestClassifier and XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV


# In[50]:


from sklearn.model_selection import cross_val_score
model_score =cross_val_score(estimator=RandomForestClassifier(),X=X_train, y=y_train, cv=5)
print(model_score)
print(model_score.mean())


# In[51]:


from sklearn.model_selection import cross_val_score
model_score =cross_val_score(estimator=XGBClassifier(),X=X_train, y=y_train, cv=5)
print(model_score)
print(model_score.mean())


# In[ ]:


#create param
model_param = {
    'RandomForestClassifier':{
        'model':RandomForestClassifier(),
        'param':{
            'n_estimators': [10, 50, 100, 130], 
            'criterion': ['gini', 'entropy'],
            'max_depth': range(2, 4, 1), 
            'max_features': ['auto', 'log2']
        }
    },
    'XGBClassifier':{
        'model':XGBClassifier(objective='binary:logistic'),
        'param':{
           'learning_rate': [0.5, 0.1, 0.01, 0.001],
            'max_depth': [3, 5, 10, 20],
            'n_estimators': [10, 50, 100, 200]
        }
    }
}


# In[ ]:


#gridsearch
scores =[]
for model_name, mp in model_param.items():
    model_selection = GridSearchCV(estimator=mp['model'],param_grid=mp['param'],cv=5,return_train_score=False)
    model_selection.fit(X,y)
    scores.append({
        'model': model_name,
        'best_score': model_selection.best_score_,
        'best_params': model_selection.best_params_
    })


# In[ ]:


scores


# # Model Building

# In[52]:


#as per above results, xgboost gives best result and hence selecting same to model building...
model_xgb = XGBClassifier(objective='binary:logistic',learning_rate=0.1,max_depth=10,n_estimators=100)


# In[53]:


model_xgb.fit(X_train,y_train)


# In[54]:


model_xgb.score(X_test,y_test)


# In[55]:


#get feature importances from the model
headers = ["name", "score"]
values = sorted(zip(X_train.columns, model_xgb.feature_importances_), key=lambda x: x[1] * -1)
xgb_feature_importances = pd.DataFrame(values, columns = headers)

#plot feature importances
fig = plt.figure(figsize=(15,7))
x_pos = np.arange(0, len(xgb_feature_importances))
plt.bar(x_pos, xgb_feature_importances['score'])
plt.xticks(x_pos, xgb_feature_importances['name'])
plt.xticks(rotation=90)
plt.title('Feature importances (XGB)')

plt.show()


# In[56]:


#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,model_xgb.predict(X_test))
cm


# In[57]:


#plot the graph
from matplotlib import pyplot as plt
import seaborn as sn
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('True Value')
plt.show()

