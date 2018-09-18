
# coding: utf-8

# In[18]:


subject=["Americans", "Indians"]
verb=["Play","Watch"]
obj=["baseball","Cricket"]
sentence_list=[(sub+" "+vb+" "+ob)for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print(sentence)



# In[20]:


def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print "division by zero!"
except Exception, err:
    print 'Caught an exception'
finally:
    print 'In finally block for cleanup'



# In[33]:


import numpy as np
x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)   
np.column_stack([x**(N-1-i) for i in range(N)])
x = np.array([1, 2, 3, 5])
np.vander(x)
np.vander(x, increasing=True)

