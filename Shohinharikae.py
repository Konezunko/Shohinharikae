#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chromedriver_binary
get_ipython().system('pip install chromedriver-binary==116.0.5845.42.0')
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By


# In[ ]:


driver = webdriver.Chrome()
driver.get('https://bakema.jp/admin/login')
    #login_button=driver.find_element(By.XPATH,  '///*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
user_name=driver.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
user_name.send_keys('bakema')
pass_word=driver.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
pass_word.send_keys('Megurarara99')
log_btn=driver.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[3]/td/input')
log_btn.click()
shohin=driver.find_element(By.XPATH,  '//*[@id="headingproducts"]/h4/a')
shohin.click()
shohin=driver.find_element(By.XPATH,  '//*[@id="collapseproducts"]/ul/li[1]/a')
shohin.click()
shohin=driver.find_element(By.XPATH,  '//*[@id="search-toggle"]')
shohin.click()
b_cartid=driver.find_element(By.XPATH,  '//*[@id="SerchPanelWrap"]/div[1]/div[7]/input')
b_cartid.send_keys('11')

b_cartkensaku=driver.find_element(By.XPATH,  '//*[@id="SerchPanelWrap"]/div[2]/button')
b_cartkensaku.click()

kihonzyouhou=driver.find_element(By.XPATH,  '//*[@id="p11"]/div[1]/div/div[2]/a[1]')
kihonzyouhou.click()
'''shiborikomi=driver.find_element(By.XPATH,  '/html/body')
shiborikomi.click()
//*[@id="search-toggle"]'''


# In[ ]:


shohin=driver.find_element(By.XPATH,  '//*[@id="collapseproducts"]/ul/li[1]/a')
shohin.click()
shiborikomi=driver.find_element(By.XPATH,  '/html/body')
shiborikomi.click()

