import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Before running: put the urls from the other script in a file named urls.txt

URL = "https://example.substack.com/"
EMAIL = ""
PASSWORD = ""
FILE_PATH = ""
FOLDER_NAME = ""

browser = webdriver.Safari()
browser.get(URL)

time.sleep(5)

def get(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return browser.find_element(By.XPATH, xpath)

get("//*[@id='main']/div[1]/div[1]/div/div[1]/div[2]/div/button[2]").click()
get("//*[@id='substack-login']/div[2]/div[2]/form/div[2]/div/a").click()
get("//*[@id='substack-login']/div[2]/div[2]/form/div[1]/input").send_keys(EMAIL)
get("//*[@id='substack-login']/div[2]/div[2]/form/input[3]").send_keys(PASSWORD)
get("//*[@id='substack-login']/div[2]/div[2]/form/button").click()

time.sleep(5)

urls = open(f"{FILE_PATH}/urls.txt", "r").readlines()
for i in range(1, len(urls)+1):
    url = urls[i-1]
    browser.get(url)
    time.sleep(2)
    page_source = browser.page_source
    with open(f"{FILE_PATH}/{FOLDER_NAME}/{i}_{url.strip().replace(f"{URL}/p/", "")}.html", "w") as file:
        file.write(page_source)