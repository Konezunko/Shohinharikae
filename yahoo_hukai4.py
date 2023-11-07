#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from selenium.common.exceptions import NoSuchElementException


# In[2]:


from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager("118.0.5993.70").install()


# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)


# In[4]:


def click_element(xpath, timeout=20):
    try:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except StaleElementReferenceException:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()


# In[5]:


def replace_and_save(xpath, old_strings, new_string, timeout=10):
    textarea_element = browser.find_element(By.XPATH, xpath)
    textarea_content = textarea_element.get_attribute('value')
    for old_str in old_strings:
        if old_str in textarea_content:
            print(f'文字列 "{old_str}" が該当の場所に存在します。')
            new_text = textarea_content.replace(old_str, new_string)
            browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
            hozon = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
            hozon.click()


# In[6]:


def delete(xpath, strings_to_remove, timeout=10):
    textarea_element = browser.find_element(By.XPATH, xpath)
    textarea_content = textarea_element.get_attribute('value')
    for str_to_remove in strings_to_remove:
        if str_to_remove in textarea_content:
            print(f'文字列 "{str_to_remove}" が該当の場所に存在します。')
            textarea_content = textarea_content.replace(str_to_remove, "")
            browser.execute_script("arguments[0].value = arguments[1]", textarea_element, textarea_content)
            time.sleep(5)
    hozon = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
    hozon.click()


# In[7]:


def main():
    
    MAX_K_VALUE = 4
    MAX_J_VALUE = 5
    i = 19
    j = 2
    k = 1
    l=1
    while True:
        try:
            # ②～⑪の処理（省略）
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')
            time.sleep(5)

            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')
            time.sleep(5)
            
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/ul/li[{k}]/span/a')
            time.sleep(5)

            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/ul/li[{k}]/ul/li[{l}]/span/a')
            time.sleep(5)
            click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')
            time.sleep(5)
            
            
            try:
                cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
                cancel.click()
            except TimeoutException:
                print("キャンセルボタンが見つかりませんでした。処理を続行します。")

            time.sleep(3)

            replace_and_save('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
            time.sleep(5)

            delete('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', 'ALN')
            time.sleep(5)

            click_element('//*[@id="react-tabs-2"]/span')
            time.sleep(3)

            replace_and_save('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
            time.sleep(5)

            delete('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', 'ALN')
            time.sleep(5)

            l += 1
            time.sleep(3)
            browser.get(url)
            time.sleep(7)

        except NoSuchElementException as e:  
            print(f"kのXPath ({k}) が存在しないため、j ({j}) をインクリメントします")
            k += 1
            l = 1
            browser.get(url)
            time.sleep(7)

            if j > MAX_K_VALUE:
                print("kの最大値に到達しました。jをインクリメントします。")
                j += 1
                k = 1
                l = 1

        except Exception as e:  
            print(f"jのXPath ({j}) が存在しないため、j ({j}) をインクリメントします")
            k +=1
            l = 1
            browser.get(url)
            time.sleep(7)

            if j > MAX_J_VALUE:
                print("jの最大値に到達しました。終了します。")
                break


# In[ ]:


#ヤフーを起動する。
browser = webdriver.Chrome()
url = r'https://pro.store.yahoo.co.jp/pro.alnaturia'  # URLを適切に設定してください
browser.get(url)
# ユーザー名を入力
user_name = browser.find_element(By.XPATH,  '//*[@id="login_handle"]')
user_name.send_keys('alnaturia_murayama')  # 実際のユーザー名を設定してください

# 「次へ」ボタンをクリック
click_element('//*[@id="content"]/div[1]/div/form/div[1]/div[1]/div[2]/div/button')

# パスワードフィールドが利用可能になるまで待つ
password_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))

# パスワードを入力
password_field.send_keys('Megurarara99')  # 実際のパスワードを設定してください

# ログインボタンをクリック
click_element('//*[@id="content"]/div[1]/div/form/div[2]/div/div[1]/div[2]/div[3]/button')
#①商品・画像・在庫をクリック
click_element('//*[@id="ycWrHeader"]/div[2]/div/ul[2]/li[5]/a')

url = 'https://editor.store.yahoo.co.jp/RT/alnaturia/PageEdit/index?_c=ArZXCGUA7I2te5G6k4O4aErs7HbYReNYW8vun7pomn6xxf8ct-RxyWN-_zFkDd7Osqm3A1APiUKHdXjG8Jo8WicdJ-SWI3wfSS3X8HiROEa3LSoBi2YVVVK-spN6cpNGcMTKIb55'

time.sleep(5)
if __name__ =="__main__":
    main()


# In[ ]:




