#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[16]:


get_ipython().system('pip install chromedriver-install')


# In[25]:


get_ipython().system('pip install bs4 selenium')


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv
import time 


# In[15]:


#this is checing code for single url single page, ran successfully in compiler
jobs = []
work=[]
max_page = 9  #went for lower numers of pages due to computer issues
max_digit = 3
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
time.sleep(10)  #giving each file request to have 10s of reloading time for server

for i in range(1, max_page + 1):  #initiating pages from 1 to final page
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i) #this checks for pages, if pages doesnt exist it gives 0
  url = "https://www.naukri.com/interior-design-jobs-/" + page_num + "?xt=catsrch&qf[]=2"  #gives the changing url,  final value "2" can be changesd to other values to get for differnt secors
  print(url)
  driver.get(url)
  

  all_links = driver.find_elements_by_class_name('jobTuple') #checking for job posting node which isgenerall common

  loop1 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/a')  #moving from nonde in specific direction to get required values 
  loop2 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/div/a') # same as above and also for below ones
  loop3 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div[1]/ul/li[1]/span')
  loop4 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/ul/li[2]/span')
  loop5 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/ul/li[3]/span')
  loop6 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[2]')
  loop7=  driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/ul')
  loop8 =  driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[3]/div[2]/span')

  #jobs.append(loop2[i].text)
  for i in range(len(all_links)): #now initaiting in loop to give all values 
      job =(loop1[i].text)
  #print(job)
      company = (loop2[i].text)
      experience = (loop3[i].text)
      salary = (loop4[i].text)
      location = (loop5[i].text)
  #print(location)
      description = (loop6[i].text)
      tags = (loop7[i].text)
      print(tags)
      date = (loop8[i].text)
driver.close() #closing the scraping session 

 


# In[9]:


#code for multiple pages for single url
#ran successfullfy for limied number of pages,befoynd certain number my computer faced memory issues
max_page = 9  #went for lower numers of pages due to computer issues
max_digit = 3

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
time.sleep(10)
with open('task22.csv', 'w') as f:  #initiating csv file to write the scraped values
    f.write("'job_title, company,experience,salary,location,description,tags,date \n")
    
for i in range(1, max_page + 1):  #loop for different pages of url
    page_num = (max_digit - len(str(i))) * "0" + str(i)
    url = "https://www.naukri.com/interior-design-jobs-/" + page_num + "?xt=catsrch&qf[]=2"  #last part of url can be modified to run for multiple urls
    print(url)
    
    driver.get(url)
    all_links = driver.find_elements_by_class_name('jobTuple')
    print(all_links)
    loop1 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/a')
    loop2 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/div/a')
    loop3 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div[1]/ul/li[1]/span')
    loop4 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/ul/li[2]/span')
    loop5 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[1]/div/ul/li[3]/span')
    loop6 = driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[2]')
    loop7=  driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/ul')
    loop8 =  driver.find_elements_by_xpath('//*[@class="jobTuple bgWhite br4 mb-8"]/div[3]/div[2]/span')

    num_page_items = len(all_links) #writing the calues of scrapped values into csv
    with open('task22.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(loop1[i].text + "," + loop2[i].text + "\n")



driver.close() #closinng the process
    
    


# In[ ]:




