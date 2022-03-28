import os
import string
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import src.helper as sh


def download_from_rakuten():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", sh.CHROME_DRIVER_OPTIONS)
    driver = webdriver.Chrome(service=sh.SERVICE_OBJECT, options=opt)

    _login_to_mypage(driver)
    selection = Select(driver.find_element(by=By.ID, value="j_idt609:card"))
    card_list = [s.text for s in selection.options]

    for card in card_list:
        brand = _get_card_brand(card)
        print(f"{brand}カードを読み込んでいます。")

        selection.select_by_visible_text(card)
        driver.execute_script("window.scrollTo(0, 300);")
        _download_csv(driver=driver, service="rakuten",card_name=brand)
    
    driver.close()


def _download_csv(driver: object, service: string,card_name: string):
    tags = driver.find_element(by=By.CSS_SELECTOR, value=".stmt-c-btn-dl.stmt-csv-btn")
    csv_url = tags.get_attribute("href")
    cookies = _get_cookies(driver=driver)
    download_path = os.path.join(sh.DOWNLOAD_DIR, f'{card_name}_{service}.csv')

    print(f'Downloading... {download_path}')
    # requestsを利用してデータのダウンロード
    r = requests.get(csv_url, cookies=cookies)
    with open(download_path, 'wb') as f:
        f.write(r.content)
        
    print(f"{card_name}カードの情報を読み込みました。")
    time.sleep(3)


def _get_cookies(driver: object):
    c = {}
    for cookie in driver.get_cookies():
        name = cookie['name']
        value = cookie['value']
        c[name] = value
    return c
    

def _login_to_mypage(driver: object):
    driver.get(sh.RAKUTEN_LOGIN_PAGE)
    time.sleep(1)
    driver.find_element(by=By.NAME, value="u").send_keys(sh.RAKUTEN_CREDENTIALS["id"])
    driver.find_element(by=By.NAME, value="p").send_keys(sh.RAKUTEN_CREDENTIALS["password"])
    time.sleep(3)
    driver.find_element(by=By.ID, value="loginButton").click()
    driver.find_element(by=By.LINK_TEXT, value="明細を見る").click()


def _get_card_brand(name: string) -> string:
    if "Visa" in name:
        return "Visa"
    if "Master" in name:
        return "MasterCard"
    if "JCB" in name:
        return "JCB"
    if "American" in name:
        return "AMEX"
