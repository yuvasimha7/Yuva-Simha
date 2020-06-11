#!/usr/bin/env python
# coding: utf-8

# In[8]:


import glob
import os
import codecs
from bs4 import BeautifulSoup as bs
import urllib
import urllib.request
import requests
from lxml.html import fromstring
import lxml.html as PARSER
import urllib
import gc
from collections import Counter
import re
import pandas as pd


# In[2]:


year = []   #initiating values which laterappended
file_name = []
high_competition = []
technology_competition = []
word1 = ['high competition','fierce competition','strong competition','extreme competition']  #specifying words and syninyms
word2= ['technology competition','technological competitors','technological rivals']


# In[3]:


path  = 'E:/ISB Ra work/10K' #path of our file


# In[4]:


for root, dirs, files in os.walk(path):  #from a given folder ir goes into the folders which as subfolders from 2010 to 2017
    i =root
    for name in files:   #if files exist then name of the file is assigned to name
        if name.endswith((".html", ".htm")):  #checking whether the files are html or not if not they dont get opened 
            counter = 0   #initiating the counter
            file_year = os.path.basename(os.path.normpath(root))  #creating column for year
            year.append (os.path.basename(os.path.normpath(root)))
            file_name.append(name)
            j=root+'\\'+name   #moving along the files
            #print(j)
            f = open(j, encoding="utf8")     #opening thefiles
            soup = bs(f)   #applying beautiful soup for rading html files 
            results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(word1)), recursive=True)  #checking for word 1
            
            high_competition.append(len(results1))  #adding total count
            results2 =soup.body.find_all(string=re.compile('.*{0}.*'.format(word2)), recursive=True)  #checking for word2
            
            technology_competition.append(len(results2)) #adding final count
            
            f.close()
            
            
            


# In[6]:


year,file_name,high_competition,technology_competition  #vizualizing the files


# In[10]:


df = pd.DataFrame(list(zip(year, file_name,high_competition,technology_competition)), 
               columns =['Year', 'File Name','High competition','Technological Competition'])  #merging them to form proper data frame 


# In[11]:


df


# In[13]:


df.to_csv (r'E:\ISB Ra work\Task1.csv', index = False, header=True) #downloading the file


# In[ ]:




