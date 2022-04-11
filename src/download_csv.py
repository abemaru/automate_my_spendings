"""各カードのサイトからカードの明細情報をダウンロードするモジュール"""

import os
import string
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import src.helper as sh

class Rakuten():
    """
    楽天カードのサイトからカードの明細情報をダウンロードするためのクラス
    """
    BRAND = sh.RAKUTEN_CARD_BRAND

    def __init__(self, brand) -> None:
        """
        Parameters
        ----------
        brand : string
            楽天カードのブランド。
        """
        self.brand = brand


    def execute_download(self):
        """
        クラス作成時に指定されたブランドの明細をダウンロードする
        """
        self.driver = self.create_driver()
        self.login_to_mypage()
        self.download_csv()


    @classmethod
    def visacard(cls):
        return Rakuten(brand=Rakuten.BRAND[0])


    @classmethod
    def mastercard(cls):
        return Rakuten(brand=Rakuten.BRAND[1])

    
    @classmethod
    def jcb(cls):
        return Rakuten(brand=Rakuten.BRAND[2])

    
    @classmethod
    def amex(cls):
        return Rakuten(brand=Rakuten.BRAND[3])
        

    @staticmethod
    def create_driver():
        """
        selenium
        """
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs", sh.CHROME_DRIVER_OPTIONS)
        return webdriver.Chrome(service=sh.SERVICE_OBJECT, options=opt)


    def login_to_mypage(self):
        """
        .envで読み込んだ環境変数をもとに楽天カードログインを行う関数
        """
        self.driver.get(sh.RAKUTEN_LOGIN_PAGE)
        time.sleep(1)
        self.driver.find_element(by=By.NAME, value="u").send_keys(sh.RAKUTEN_CREDENTIALS["id"])
        self.driver.find_element(by=By.NAME, value="p").send_keys(sh.RAKUTEN_CREDENTIALS["password"])
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="loginButton").click()
        self.driver.find_element(by=By.LINK_TEXT, value="明細を見る").click()


    def download_csv(self):
        selection_element = Select(self.driver.find_element(by=By.ID, value="j_idt609:card"))
        if self.brand not in selection_element.first_selected_option.text:
            selection_element.select_by_visible_text(f"楽天カード（{self.brand}）")
        
        # scroll実行せずにダウンロードを試みるとダウンロードアイコンが画面外でエラーになるため
        self.driver.execute_script("window.scrollTo(0, 300);")
        tags = self.driver.find_element(by=By.CSS_SELECTOR, value=".stmt-c-btn-dl.stmt-csv-btn")
        csv_url = tags.get_attribute("href")
        cookies = self._get_cookies()
        download_path = os.path.join(sh.DOWNLOAD_DIR, f"{self.brand}_rakuten.csv")
        r = requests.get(csv_url, cookies=cookies)
        with open(download_path, "wb") as f:
            f.write(r.content)
        time.sleep(3)


    def _get_cookies(self):
        c = {}
        for cookie in self.driver.get_cookies():
            name = cookie['name']
            value = cookie['value']
            c[name] = value
        return c
