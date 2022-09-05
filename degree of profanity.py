
# coding: utf-8

# In[59]:


import numpy as np


# In[60]:


def dof(Tw,Sl):
    
    T= open(Tw, 'r').read() #tweets to strings
    tweets = T.splitlines()
    
    S = open(Sl, 'r').read() #slurs to strings
    slurs = S.splitlines() 
    
    #Initialise degree of profanity for each tweet as 0
    prof=np.empty(len(tweets), dtype=int)
    for i in range(0,len(tweets)): 
        prof[i]= 0  

   
    #Making our checking case insensitive
    ltweets=[x.lower() for x in tweets]
    lslurs=[x.lower() for x in slurs]
    
    #Check each tweet for racial slurs
    for i in range(0,len(ltweets)): 
        for j in range(0,len(lslurs)):
             if(lslurs[j] in ltweets[i]):
                    prof[i] = prof[i]+1
            
    for i in range(0, len(ltweets)):
        print("The degree of profanity of tweet",i+1,"is: ", prof[i])


# In[61]:


dof('tweets.txt','slurs.txt')

