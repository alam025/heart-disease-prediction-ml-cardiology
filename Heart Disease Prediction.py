#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#  #Data Collection andd Processing

# In[2]:


#loading the csv data to pandas dataframe
heart_data = pd.read_csv('heart_disease_data.csv')


# In[3]:


#print first five rows of the data set
heart_data.head()


# In[4]:


#print last five rows of the dataset
heart_data.tail()


# In[5]:


heart_data.shape


# In[6]:


#getting some info sbout the data
heart_data.info()


# In[7]:

#Add preprocessing functions
#checking for missing values
heart_data.isnull().sum()


# In[8]:


#statistical measure about the data
heart_data.describe()


# In[10]:


#checking the distribution of Target Variable
heart_data['target'].value_counts()


# #1 Defective heart
# #0 Healthy Heart

# #Splitting the Features and Target

# In[11]:


X = heart_data.drop(columns='target',axis=1)
Y= heart_data['target']


# In[12]:


print(X)


# In[13]:


print(Y)


# In[22]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y, random_state=2)


# In[23]:


print(X.shape,X_train.shape,X_test.shape)


# #Model Training

# #Logistic Regression

# In[24]:

#Add core model code
model = LogisticRegression()


# In[25]:


# training the LogisticRegression model with Training data
model.fit(X_train,Y_train)

#Add evaluation code
# #Model Evaluation

# #Accuracy Score

# In[26]:


#accuract on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)


# In[27]:


print('Accuracy on Training data: ',training_data_accuracy)


# In[28]:


#accuract on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)


# In[29]:


print('Accuracy on Test data: ',test_data_accuracy)


# #Building a Predictive System

# In[34]:


input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)

#change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print("The Person does not have a Heart Disease")
else:
    print("The Person has Heart Disease")


# In[ ]:




