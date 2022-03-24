import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

DOWNLOAD_DIR = "tmp/"
RAKUTEN_CREDENTIALS = {
    "id": os.environ.get("RAKUTEN_ID"),
    "password": os.environ.get("RAKUTEN_PASSWORD")
}

opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,
    "download.promplt_for_download": False,
    "plugin.always_open_pdf_externally": True
})
driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"), options=opt)
driver.get('https://www.rakuten-card.co.jp/e-navi/index.xhtml')
time.sleep(1)

driver.find_element_by_name("u").send_keys(RAKUTEN_CREDENTIALS["id"])
driver.find_element_by_name("p").send_keys(RAKUTEN_CREDENTIALS["password"])
time.sleep(3)
driver.find_element_by_id("loginButton").click()
driver.find_element_by_link_text("明細を見る").click()
