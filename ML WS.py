#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cam=pd.read_csv(r"C:\Users\SRUTHI\Downloads\labels_my-project-name_2023-08-03-02-41-44.csv")


# In[3]:


cam.head()


# In[4]:


cam.info()


# In[5]:


cam.sum()


# In[6]:


cam.describe()


# In[7]:


cam.isnull().sum()


# In[8]:


cam.dropna()


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
import cv2


# In[10]:


sns.pairplot(cam)


# In[11]:


k=sns.boxplot(data=cam)


# In[12]:


sns.jointplot(cam)


# In[13]:


sns.displot(cam)


# In[15]:


get_ipython().system('pip install matplotlib')


# In[16]:


testimg=img.imread(r"C:\Users\SRUTHI\Downloads\pa.jpg")
plt.imshow(testimg)


# In[18]:


Start_point=(4,4)
End_point=(220,220)
color=(255,0,0)
thickness=9


# In[19]:


testimg=cv2.rectangle(testimg,Start_point,End_point,color,thickness)


# In[ ]:


cv2.imshow("name",testimg)
cv2.waitKey(0)


# In[ ]:


for(x,y,w,h) in testimg:
    k=cv2.rectangle(cam,(x,y),(x+w),(y+h),(255,0,0),6)
gray=cv2.cvColor(cam,cv2.COLOR_BGR2GRAY)


# In[ ]:




