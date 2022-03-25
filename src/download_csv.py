import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

import src.helper as sh

def do_it():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", {
        "download.default_directory": sh.DOWNLOAD_DIR,
        "download.promplt_for_download": False,
        "plugin.always_open_pdf_externally": True
    })
    driver = webdriver.Chrome(service=sh.SERVICE_OBJECT, options=opt)
    driver.get(sh.RAKUTEN_LOGIN_PAGE)
    time.sleep(1)

    driver.find_element(by=By.NAME, value="u").send_keys(sh.RAKUTEN_CREDENTIALS["id"])
    driver.find_element(by=By.NAME, value="p").send_keys(sh.RAKUTEN_CREDENTIALS["password"])
    time.sleep(3)
    driver.find_element(by=By.ID, value="loginButton").click()
    driver.find_element(by=By.LINK_TEXT, value="明細を見る").click()

    tag = driver.find_element(by=By.CSS_SELECTOR, value=".stmt-c-btn-dl.stmt-csv-btn")
    href = tag.get_attribute('href')

    c = {}
    for cookie in driver.get_cookies():
        c[cookie["name"]] = cookie["value"]

    # この下が動かない
    r = requests.get(href)
    with open("rakuten_card.csv", "wb") as f:
        f.write(r.content)


