
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np



import numpy as np


# #### Create an array of 10 zeros 



np.zeros(10)


# #### Create an array of 10 ones




np.ones(10)


# #### Create an array of 10 fives



np.ones(10) * 5


# #### Create an array of the integers from 10 to 50



arr_10_50 = np.arange(10,51)

arr_10_50


# #### Create an array of all the even integers from 10 to 50

# In[16]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[21]:


arr = np.arange(0,9)

arr.reshape(3,3)


# #### Create a 3x3 identity matrix

# In[22]:


np.eye(3,3)


# #### Use NumPy to generate a random number between 0 and 1

# In[25]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[26]:


np.random.randn(25)


# #### Create the following matrix:

# In[12]:





# In[13]:


import numpy as np
np.arange(0.01,1.01,.01).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[2]:





# In[14]:


import numpy as np

np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[14]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[16]:





# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[16]:


import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[2:,1:]


# In[21]:





# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[17]:


mat[:3,1].reshape(3,1)


# ### Now do the following

# #### Get the sum of all the values in mat

# In[22]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[19]:


mat.std()


# #### Get the sum of all the columns in mat

# In[22]:


mat.sum(axis =0)

