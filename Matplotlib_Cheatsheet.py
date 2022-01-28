#!/usr/bin/env python
# coding: utf-8

# # Matplotlib_Cheatsheet

# In[1]:


get_ipython().system('pip install matplotlib')


# In[1]:


import matplotlib


# # Simple Plot-Line

# In[2]:


from matplotlib import pyplot as pt
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]
x1 = [2,4,6,8,10,12,14,16,18,20]
y2 = [1,3,5,7,9,11,13,15,17,19]
pt.plot(x,y,'r',label = 'Square')
pt.plot(x1,y2,'b',label = 'OddnEven')
pt.legend()
pt.title("Square Graph")
pt.xlabel("start")
pt.ylabel("Squares")


pt.show()


# # Bar Plot

# In[3]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]
x1 = [2,4,6,8,10,12,14,16,18,20]
y2 = [1,3,5,7,9,11,13,15,17,19]
pt.bar(x,x1,color='r',label = 'Square')
#pt.bar(x1,y2,color = 'g',label = 'OddnEven')
pt.legend()
pt.title("Square Graph")
pt.xlabel("start")
pt.ylabel("Squares")


pt.show()


# # Histograph

# In[4]:


x = [29,34,56,66,75,24,66,43,67]
y = [0,10,20,30,40,50,60,70,80]
pt.hist(x,y)
pt.title("Graph")
pt.xlabel("Age")
pt.ylabel("Range")
pt.grid()
pt.show()


# # Scatter Graph

# In[6]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [9,8,7,6,5,9,8,7,6,5]
pt.scatter(x,y,marker = '*',color = 'g')
pt.title("Graph")
pt.xlabel("Age")
pt.ylabel("Range")
pt.show()


# # Pie Chart

# In[9]:


x = [30,35,26,45,40]
y = ["Maths","Sci","Eng","SSt","Sans"]
c = ['r','b','g','y','m']
pt.pie(x,labels = y,colors = c, autopct = '%1.1f%%')
pt.title("Graph")
pt.show()


# # SubPlot

# In[27]:


x = [1,2,3,4,5,6,7,8,9]
y = [1,4,9,16,25,36,49,64,81]
x1 = [1,3,5,7,9,11,13,15,17,19]
y1 = [2,4,6,8,10,12,14,16,18,20]

pt.subplot(1,3,1)
pt.title("Plot 1")
pt.plot(x,y,'r')

pt.subplot(1,3,3)
pt.title("Plot 2")
pt.plot(x1,y1,'g')
pt.show()


# # A Small Project

# In[28]:


import pandas as pd


# In[29]:


data1 = pd.read_csv("dataset11.csv") #A small salary dataset to make visuals from it


# In[36]:


a = data1.iloc[:,:-1].values
a


# In[37]:


b = data1.iloc[:,-1].values
b


# In[38]:


pt.scatter(a,b,color = 'r')
pt.title("Salary Visuals")
pt.xlabel('Level')
pt.ylabel('Salary')
pt.show()


# In[39]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(a,b)


# In[43]:


pt.scatter(a,b,color = 'g')
pt.plot(a,lr.predict(a),'b')
pt.title("Linear Regression predicted plot")
pt.xlabel("Level")
pt.ylabel("Salary")
pt.show()


# In[ ]:




