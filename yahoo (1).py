#!/usr/bin/env python
# coding: utf-8

# In[32]:


def yahoo():
    
    browser = webdriver.Chrome()
    url = r'https://pro.store.yahoo.co.jp/pro.alnaturia'  # URLを適切に設定してください
    browser.get(url)

    # ユーザー名を入力
    user_name = browser.find_element(By.XPATH,  '//*[@id="login_handle"]')
    user_name.send_keys('alnaturia_murayama')  # 実際のユーザー名を設定してください

    # 「次へ」ボタンをクリック
    next_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/form/div[1]/div[1]/div[2]/div/button')))
    next_button.click()

    # パスワードフィールドが利用可能になるまで待つ
    password_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))

    # パスワードを入力
    password_field.send_keys('Megurarara99')  # 実際のパスワードを設定してください

    # ログインボタンをクリック
    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/form/div[2]/div/div[1]/div[2]/div[3]/button')))
    login_button.click()
    
    #商品・在庫をクリック
    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ycWrHeader"]/div[2]/div/ul[2]/li[5]/a')))
    
    
    for i in range(2,26):
    #最上位階層をクリック    
    rank1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'  //*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')))
        j=0
        #準最上位階層がなくなるまでやる。
        while True:
            try:
                #商品名をクリック
                shohinmei = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="treeDiv1"]/ul/li/ul/li[i]/ul/li[j]/span/a')))
                shohinmei.click()
                #編集をクリック
                hensyu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="YstrHeadLine"]/div[3]/button[3]')))
                
                browser.execute_script(".click();", hensyu)
                #商品説明を参照
                textarea_element = browser.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea')
                time.sleep(1)
                textarea_content = textarea_element.get_attribute('value')
                #もしアルナチュリアがあればベーカリスタに変更する。
                if textarea_content and 'アルナチュリア' in textarea_content:
                    print('文字列 "アルナチュリア" が該当の場所に存在します。')
                    new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
                    browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
                    time.sleep(1)
                    hozon=browser.find_element(By.XPATH,  '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span/a')
                    hozon.click()
                    time.sleep(1)
                else:
                    print('文字列 "アルナチュリア" が該当の場所に存在しません。')
                    time.sleep(1)
                j += 1
            #フォルダーがなければ次へ行く。
            except NoSuchElementException:
                # Elementが見つからないときにループを終了
                print("Elementが見つかりません。次に行きます。")
                time.sleep(1)
                break


# In[33]:


yahoo()//*[@id="treeDiv1"]/ul/li/ul/li[2]/ul/li[1]/span/a


# In[ ]:


(/*[@id="treeDiv1"]/ul/li/ul/li[2]/span/a)
  商品番号
(/*[@id="treeDiv1"]/ul/li/ul/li[25]/span/a)
  '''user_name=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
  user_name.send_keys('bakema')  # 実際のユーザー名を設定してください
  pass_word=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
  pass_word.send_keys('Megurarara99')  # 実際のパスワードを設定してください
  log_btn=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[3]/td/input')
  log_btn.click()
  # Excelファイルのパスを指定
  file_path = r"C:\Users\konez\OneDrive\デスクトップ\shohinharikae\I_社名変更作業管理表_商品ページ (1).xlsx"
  # Excelファイルを読み込む
  df = pd.read_excel(file_path)
  # C列のデータを取得する
  column_c_data = df['商品ID']
  for j in range(298,299):
      b_cartid=column_c_data.iloc[j]
      #商品IDの列を変更する
      print(column_c_data.iloc[j])
      url = f'https://bakema.jp/admin/products/{b_cartid}/edit'  # URLを適切に設定してください
      browser.get(url)

      # ステップ 3: 指定されたXPathでテキストエリア要素を取得
      textarea_element = browser.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div/form/div[1]/div[2]/table[1]/tbody/tr[13]/td/textarea')

      # ステップ 4: テキストエリアのテキストを取得して、条件を確認
      textarea_content = textarea_element.get_attribute('value')
      if textarea_content and 'アルナチュリア' in textarea_content:
          print(f'文字列 "アルナチュリア" が該当の場所に存在します。商品番号{b_cartid}')
          # 該当のテキストを "ベーカリスタ" に書き換える
          new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
          browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
      else:
          print('文字列 "アルナチュリア" が該当の場所に存在しません。')

      hozon=browser.find_element(By.XPATH,  '//*[@id="page-content-wrapper"]/div/form/div[3]/div/div[2]/input')
      hozon.click()

      setzyohou=browser.find_element(By.XPATH,  '//*[@id="page-content-wrapper"]/div/div[2]/div[1]/a[2]')
      setzyohou.click()


      from selenium.common.exceptions import NoSuchElementException
      i = 1
      while True:
          try:
              hensyu = browser.find_element(By.XPATH, f'//*[@id="page-content-wrapper"]/div/div[3]/div[2]/div/table/tbody/tr[{i}]/td[9]/a')
              browser.execute_script("arguments[0].click();", hensyu)
              textarea_element = browser.find_element(By.XPATH, '//*[@id="form"]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td/textarea')
              time.sleep(1)
              textarea_content = textarea_element.get_attribute('value')
              if textarea_content and 'アルナチュリア' in textarea_content:
                  print('文字列 "アルナチュリア" が該当の場所に存在します。')
                  new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
                  browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
                  time.sleep(1)
                  hozon=browser.find_element(By.XPATH,  '//*[@id="form"]/div[2]/div/div[2]/input')
                  hozon.click()
                  time.sleep(1)
              else:
                  print('文字列 "アルナチュリア" が該当の場所に存在しません。')
                  time.sleep(1)
              i += 1
          except NoSuchElementException:
              # Elementが見つからないときにループを終了
              print("Elementが見つかりません。次に行きます。")
              time.sleep(1)
              break'''


# In[15]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[35]:


browser = webdriver.Chrome()
url = r'https://pro.store.yahoo.co.jp/pro.alnaturia'  # URLを適切に設定してください
browser.get(url)

# ユーザー名を入力
user_name = browser.find_element(By.XPATH,  '//*[@id="login_handle"]')
user_name.send_keys('alnaturia_murayama')  # 実際のユーザー名を設定してください

# 「次へ」ボタンをクリック
next_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/form/div[1]/div[1]/div[2]/div/button')))
next_button.click()

# パスワードフィールドが利用可能になるまで待つ
password_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))

# パスワードを入力
password_field.send_keys('Megurarara99')  # 実際のパスワードを設定してください

# ログインボタンをクリック
login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/form/div[2]/div/div[1]/div[2]/div[3]/button')))
login_button.click()

#//*[@id="treeDiv1"]/ul/li/ul/li[2]/span/a
#商品・在庫をクリック
hensyu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ycWrHeader"]/div[2]/div/ul[2]/li[5]/a')))
hensyu.click()

#商品名をクリック
try:
    shohinmei = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="treeDiv1"]/ul/li/ul/li[2]/span/a')))
    shohinmei.click()
except StaleElementReferenceException:
    shohinmei = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="treeDiv1"]/ul/li/ul/li[2]/span/a')))
    shohinmei.click()

#編集する商品をクリック
hensyu_shohin = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="treeDiv1"]/ul/li/ul/li[2]/ul/li[1]/span/a')))
hensyu_shohin.click()

#編集する商品名をクリック
hensyu_shohinmei = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="treeDiv1"]/ul/li/ul/li[2]/ul/li[1]/span/a')))
hensyu_shohinmei.click()

hensyusan = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="YstrHeadLine"]/div[3]/button[3]')))
hensyusan.click()

time.sleep(1)
#反映をキャンセル

cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
cancel.click()
#WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea')))

time.sleep(5)
hensyu = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="YstrHeadLine"]/div[3]/button[3]')))
hensyu.click()

time.sleep(5)
# ステップ 3: 指定されたXPathでテキストエリア要素を取得
textarea_element = browser.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea')

textarea_content = textarea_element.get_attribute('value')
if textarea_content and 'アルナチュリア' in textarea_content:
    print('文字列 "アルナチュリア" が該当の場所に存在します。')

'''
browser.execute_script(".click();", hensyu)
#商品説明を参照
textarea_element = browser.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea')
time.sleep(1)
textarea_content = textarea_element.get_attribute('value')
#もしアルナチュリアがあればベーカリスタに変更する。

if textarea_content and 'アルナチュリア' in textarea_content:
    print('文字列 "アルナチュリア" が該当の場所に存在します。')
    new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
    browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
    time.sleep(1)
    hozon=browser.find_element(By.XPATH,  '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span/a')
    hozon.click()
    time.sleep(1)
else:
    print('文字列 "アルナチュリア" が該当の場所に存在しません。')
    time.sleep(1)
j += 1
#フォルダーがなければ次へ行く。
except NoSuchElementException:
# Elementが見つからないときにループを終了
print("Elementが見つかりません。次に行きます。")
time.sleep(1)
break
'''


# In[42]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from selenium.common.exceptions import NoSuchElementException


# 対象をクリックする関数

# In[43]:


def click_element(xpath, timeout=10):
    try:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except StaleElementReferenceException:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()


# 文字列をアルナチュリアからベーカリスタに変更する関数

# In[40]:


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


# In[45]:


def delete(xpath, strings_to_remove, timeout=10):
    textarea_element = browser.find_element(By.XPATH, xpath)
    textarea_content = textarea_element.get_attribute('value')
    for str_to_remove in strings_to_remove:
        if str_to_remove in textarea_content:
            print(f'文字列 "{str_to_remove}" が該当の場所に存在します。')
            textarea_content = textarea_content.replace(str_to_remove, "")
            browser.execute_script("arguments[0].value = arguments[1]", textarea_element, textarea_content)
            time.sleep(3)
    hozon = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
    hozon.click()


# In[34]:


def shohinmei(xpath,time=10):
        textarea_element = browser.find_element(By.XPATH, xpath)
        print(textarea_element)


# In[46]:


#メイン関数
def main():
    i = 2
    j = 1
    while True:
        try:
            # ②商品名をクリックお得なセット商品から
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')

            # ③編集する商品をクリック
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')
            #編集をクリック
            time.sleep(5)
            click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')
            
            time.sleep(2)

            # ⑤反映をキャンセル
            try:
                cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
                cancel.click()
            except TimeoutException:
                print("キャンセルボタンが見つかりませんでした。処理を続行します。")
            
            time.sleep(3)
            # ⑥ステップ 3: 指定されたXPathでテキストエリア要素を取得
            # ⑦〜⑩の処理を関数でまとめる
            replace_and_save('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
            time.sleep(5)
            #ALNを削除
            delete('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea','ALN')
            time.sleep(5)
            
            # ⑧追加表示情報からスマートフォン編集画面へ移行
            click_element('//*[@id="react-tabs-2"]/span')
            time.sleep(3)
            # ⑨〜⑩の処理を関数でまとめる
            replace_and_save('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
            time.sleep(2)
            delete('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea','ALN')
            time.sleep(3)
            delete('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea','ALN')
            # ⑪商品を選ぶ画面に戻る→②
            
            j+=1
            browser.get(url)
            
        except NoSuchElementException:
            print(f"jのXPath ({j}) が存在しないため、i ({i}) をインクリメントします")
            i += 1
            j = 1
            browser.get(url)
        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")
            break
            browser.close()


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





# In[ ]:





# In[ ]:





# In[ ]:




