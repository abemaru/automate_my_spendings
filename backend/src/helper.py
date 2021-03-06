"""環境変数の読み込みや、設定情報をまとめたファイル"""
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service

load_dotenv()

RUN_TIME=os.environ.get("RUN_TIME")

# for chrome driver
SERVICE_OBJECT = Service(os.environ.get("CHROME_DRIVER_PATH"))
DOWNLOAD_DIR = "tmp/"
CHROME_DRIVER_OPTIONS = {
    "download.default_directory": DOWNLOAD_DIR,
    "download.promplt_for_download": False,
    "plugin.always_open_pdf_externally": True
}

# for rakuten login
RAKUTEN_LOGIN_PAGE = "https://www.rakuten-card.co.jp/e-navi/index.xhtml"
RAKUTEN_CREDENTIALS = {
    "id": os.environ.get("RAKUTEN_ID"),
    "password": os.environ.get("RAKUTEN_PASSWORD")
}
RAKUTEN_CARD_BRAND = ["Visa", "MasterCard", "JCB", "AMEX"]
