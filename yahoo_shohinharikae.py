#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[8]:


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

#①商品・画像・在庫をクリック
hensyu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ycWrHeader"]/div[2]/div/ul[2]/li[5]/a')))
hensyu.click()

i=2
j=1

while True:
    #②商品名をクリックお得なセット商品から
    try:
        shohinmei = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')))
        shohinmei.click()
    except StaleElementReferenceException:
        shohinmei = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')))
        shohinmei.click()

    #③編集する商品をクリック
    hensyu_shohin = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')))
    hensyu_shohin.click()

    #④商品の編集をクリック
    hensyu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="YstrHeadLine"]/div[3]/button[3]')))
    hensyu.click()

    time.sleep(1)

    #⑤反映をキャンセル
    try:
        cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
        cancel.click()
    except TimeoutException:
        print("キャンセルボタンが見つかりませんでした。処理を続行します。")

    time.sleep(5)
    hensyu = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="YstrHeadLine"]/div[3]/button[3]')))
    hensyu.click()

    time.sleep(5)
    #⑥ステップ 3: 指定されたXPathでテキストエリア要素を取得
    textarea_element = browser.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea')

    #⑦HTML編集ページにアルナチュリアまたはbakerlistaが検出されるとベーカリスタに変更する。
    textarea_content = textarea_element.get_attribute('value')
    if textarea_content and 'アルナチュリア' in textarea_content:
        print('文字列 "アルナチュリア" が該当の場所に存在します。')
        new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
        browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
        hozon = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
        hozon.click()
    if textarea_content and 'bakerlista' in textarea_content:
        print('文字列 "bakerlista" が該当の場所に存在します。')
        new_text = textarea_content.replace('bakerlista', 'ベーカリスタ')
        browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
        hozon = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
        hozon.click()

    #⑧追加表示情報からスマートフォン編集画面へ移行
    sumaho_hensyu = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-tabs-2"]/span')))
    sumaho_hensyu.click()

    #⑨HTML編集ページにアルナチュリアまたはbakerlistaが検出されるとベーカリスタに変更する。
    textarea_element = browser.find_element(By.XPATH, '//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea')

    #⑩HTML編集ページにアルナチュリアまたはbakerlistaが検出されるとベーカリスタに変更する。
    textarea_content = textarea_element.get_attribute('value')
    if textarea_content and 'アルナチュリア' in textarea_content:
        print('文字列 "アルナチュリア" が該当の場所に存在します。')
        new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
        browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
        hozon = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
        hozon.click()
    if textarea_content and 'bakerlista' in textarea_content:
        print('文字列 "bakerlista" が該当の場所に存在します。')
        new_text = textarea_content.replace('bakerlista', 'ベーカリスタ')
        browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
        hozon = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EditItem"]/div[3]/div/div/ul/li[2]/span/span')))
        hozon.click()
    #⑪商品を選ぶ画面に戻る→②
    url = r'https://editor.store.yahoo.co.jp/RT/alnaturia/PageEdit/index?_c=ArZXCGUA7I2te5G6k4O4aErs7HbYReNYW8vun7pomn6xxf8ct-RxyWN-_zFkDd7Osqm3A1APiUKHdXjG8Jo8WicdJ-SWI3wfSS3X8HiROEa3LSoBi2YVVVK-spN6cpNGcMTKIb55'  # URLを適切に設定してください
    browser.get(url)
    j+=1
    
    
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


# In[12]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

# URLを適切に設定してください
url = 'https://editor.store.yahoo.co.jp/RT/alnaturia/PageEdit/index?_c=ArZXCGUA7I2te5G6k4O4aErs7HbYReNYW8vun7pomn6xxf8ct-RxyWN-_zFkDd7Osqm3A1APiUKHdXjG8Jo8WicdJ-SWI3wfSS3X8HiROEa3LSoBi2YVVVK-spN6cpNGcMTKIb55'

def click_element(xpath, timeout=10):
    try:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except StaleElementReferenceException:
        element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

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

def main():
    i=1
    j=1
    # ②商品名をクリックお得なセット商品から
    click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')

    # ③編集する商品をクリック
    click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')

    # ④商品の編集をクリック
    click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')
    
    time.sleep(1)
    
    # ⑤反映をキャンセル
    try:
        cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
        cancel.click()
    except TimeoutException:
        print("キャンセルボタンが見つかりませんでした。処理を続行します。")

    time.sleep(5)
    click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')

    time.sleep(5)
    
    # ⑥ステップ 3: 指定されたXPathでテキストエリア要素を取得
    # ⑦〜⑩の処理を関数でまとめる
    replace_and_save('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
    
    # ⑧追加表示情報からスマートフォン編集画面へ移行
    click_element('//*[@id="react-tabs-2"]/span')
    
    # ⑨〜⑩の処理を関数でまとめる
    replace_and_save('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
    
    # ⑪商品を選ぶ画面に戻る→②
    browser.get(url)

# main関数を呼び出し
if __name__ == "__main__":
    main()


# In[14]:


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

def main():
    i=2
    j=1
    
    # ②商品名をクリックお得なセット商品から
    click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')

    # ③編集する商品をクリック
    click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')

    # ④商品の編集をクリック
    click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')
    
    time.sleep(1)
    
    # ⑤反映をキャンセル
    try:
        cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
        cancel.click()
    except TimeoutException:
        print("キャンセルボタンが見つかりませんでした。処理を続行します。")

    time.sleep(5)
    click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')

    time.sleep(5)
    
    # ⑥ステップ 3: 指定されたXPathでテキストエリア要素を取得
    # ⑦〜⑩の処理を関数でまとめる
    replace_and_save('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
    
    # ⑧追加表示情報からスマートフォン編集画面へ移行
    click_element('//*[@id="react-tabs-2"]/span')
    
    # ⑨〜⑩の処理を関数でまとめる
    replace_and_save('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')
    
    # ⑪商品を選ぶ画面に戻る→②
    browser.get(url)
    j+=1



# In[ ]:


from selenium.common.exceptions import NoSuchElementException
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

def main():
    i = 2
    j = 1
    
    while True:
        try:
            # ②商品名をクリックお得なセット商品から
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/span/a')

            # ③編集する商品をクリック
            click_element(f'//*[@id="treeDiv1"]/ul/li/ul/li[{i}]/ul/li[{j}]/span/a')

            # 以下のコードは変更なし
            # ④商品の編集をクリック
            click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')

            time.sleep(1)

            # ⑤反映をキャンセル
            try:
                cancel = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmPubCancel"]')))
                cancel.click()
            except TimeoutException:
                print("キャンセルボタンが見つかりませんでした。処理を続行します。")

            time.sleep(5)
            click_element('//*[@id="YstrHeadLine"]/div[3]/button[3]')

            time.sleep(5)

            # ⑥ステップ 3: 指定されたXPathでテキストエリア要素を取得
            # ⑦〜⑩の処理を関数でまとめる
            replace_and_save('//*[@id="react-tabs-1"]/div/div[8]/div[5]/div[2]/div/div/div/ul/li[1]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')

            # ⑧追加表示情報からスマートフォン編集画面へ移行
            click_element('//*[@id="react-tabs-2"]/span')

            # ⑨〜⑩の処理を関数でまとめる
            replace_and_save('//*[@id="react-tabs-3"]/div/div[1]/div[5]/div[2]/div/div/div/ul/li[2]/span/span/textarea', ['アルナチュリア', 'bakerlista'], 'ベーカリスタ')

            # ⑪商品を選ぶ画面に戻る→②
            browser.get(url)
            j+=1
            # ⑪商品を選ぶ画面に戻る→②
            browser.get(url)
            j += 1

        except NoSuchElementException:
            print(f"jのXPath ({j}) が存在しないため、i ({i}) をインクリメントします")
            i += 1
            j = 1

        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")
            break

