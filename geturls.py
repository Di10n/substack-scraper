import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# this script doesn't actually need to log in but I'll remove it later

URL = "https://example.substack.com/"
EMAIL = ""
PASSWORD = ""

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
browser.get(URL)

time.sleep(5)

articles = get("//*[@id='main']/div[2]/div/div/div/div[2]/div[1]/div")

old_num = 0
new_num = (len(articles.find_elements(By.XPATH, "./*")) + 1)/2
while old_num != new_num:
    old_num = new_num
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_num = (len(articles.find_elements(By.XPATH, "./*")) + 1)/2
    print(new_num)

time.sleep(5)

for i in range(1, int(new_num)+1):
    article = get(f"//*[@id='main']/div[2]/div/div/div/div[2]/div[1]/div/div[{2*i - 1}]/div/div[1]/div[1]/a")
    print(article.get_attribute("href"))