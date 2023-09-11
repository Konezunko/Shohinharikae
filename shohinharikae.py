#!/usr/bin/env python
# coding: utf-8

# In[40]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# ステップ 1: ブラウザインスタンスを起動
browser = webdriver.Chrome()

# ステップ 2: URLを開く
url = 'https://bakema.jp/admin/products/30/edit'  # URLを適切に設定してください
browser.get(url)
user_name=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
user_name.send_keys('bakema')
pass_word=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
pass_word.send_keys('Megurarara99')
log_btn=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[3]/td/input')
log_btn.click()
# ステップ 3: 指定されたXPathでテキストを取得
textarea_content = browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div/form/div[1]/div[2]/table[1]/tbody/tr[13]/td/textarea')

# ステップ 4: テキストが含まれているかどうかを確認
if textarea_content and 'アルナチュリア' in textarea_content.text:
    print('文字列 "アルナチュリア" が該当の場所に存在します。')
else:
    print('文字列 "アルナチュリア" が該当の場所に存在しません。')

# ステップ 5: ブラウザを閉じる
browser.quit()


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def bcart():
    
    browser = webdriver.Chrome()
    url = 'https://bakema.jp/admin/login'  # URLを適切に設定してください
    browser.get(url)
    user_name=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[1]/td[2]/input')
    user_name.send_keys('bakema')  # 実際のユーザー名を設定してください
    pass_word=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[2]/td[2]/input')
    pass_word.send_keys('Megurarara99')  # 実際のパスワードを設定してください
    log_btn=browser.find_element(By.XPATH,  '//*[@id="loginForm"]/table/tbody/tr[3]/td/input')
    log_btn.click()
    # Excelファイルのパスを指定
    file_path = r"C:\Users\konez\Downloads\shameihencou\I_社名変更作業管理表_商品ページ.xlsx"
    # Excelファイルを読み込む
    df = pd.read_excel(file_path)
    # C列のデータを取得する
    column_c_data = df['商品ID']
    for j in range(147,298):
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
                time.sleep(2)
                textarea_content = textarea_element.get_attribute('value')
                if textarea_content and 'アルナチュリア' in textarea_content:
                    print('文字列 "アルナチュリア" が該当の場所に存在します。')
                    new_text = textarea_content.replace('アルナチュリア', 'ベーカリスタ')
                    browser.execute_script("arguments[0].value = arguments[1]", textarea_element, new_text)
                    time.sleep(2)
                    hozon=browser.find_element(By.XPATH,  '//*[@id="form"]/div[2]/div/div[2]/input')
                    hozon.click()
                    time.sleep(2)
                else:
                    print('文字列 "アルナチュリア" が該当の場所に存在しません。')
                    time.sleep(3)
                i += 1
            except NoSuchElementException:
                # Elementが見つからないときにループを終了
                print("Elementが見つかりません。次に行きます。")
                time.sleep(2)
                break


# In[2]:


bcart()

