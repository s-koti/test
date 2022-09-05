
# coding: utf-8

# In[152]:


import numpy as np


# In[153]:


def DegreeOfProfanity(Tw,Sl):
    
    T= open(Tw, 'r').read() #tweets to strings
    tweets = T.splitlines()
    
    S = open(Sl, 'r').read() #slurs to strings
    slurs = S.splitlines() 
    
    #Initialise degree of profanity for each tweet as 0
    profanity=np.empty(len(tweets), dtype=int)
    for i in range(0,len(tweets)): 
        profanity[i]= 0  
    
    #Making our checking case insensitive
    tweets_lowercase=[x.lower() for x in tweets]
    slurs_lowercase=[x.lower() for x in slurs]

    #Check each tweet for racial slurs
    for i in range(0,len(tweets_lowercase)): 
        for j in range(0,len(slurs_lowercase)):
            profanity[i] = profanity[i] + tweets_lowercase[i].count(slurs_lowercase[j])
            
    for i in range(0, len(tweets_lowercase)):
        print("The degree of profanity of tweet \"",tweets[i],"\" is: ", profanity[i])


# In[154]:


DegreeOfProfanity('tweets.txt','slurs.txt')

