from dotenv import load_dotenv
import os
import json
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import login
import business
import unique



os.environ['PATH'] += "D:\Program Files\Python37\Lib\site-packages\selenium\webdriver\chrome"
driver = webdriver.Chrome()
driver.implicitly_wait(120)
load_dotenv()

login.loginfo(driver, 'hakem', '123456')

business.addBusiness(driver, 'bus.json')

login.logout(driver)

f = open("data.json", "r")
file_data = json.loads(f.read())
f.close()
last_element = file_data["users_detail"].pop()
login.loginfo(driver, last_element['username'], '123456')

driver.get(os.environ["APP_URL"] + "tax_rates/create")
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys('VAT')
driver.find_element(By.XPATH, '//*[@id="amount"]').send_keys('10')
driver.find_element(By.XPATH, '//*[@id="tax_rate_add_form"]/div[3]/button[1]').click()

driver.get(os.environ["APP_URL"] + "business/settings")
Select(driver.find_element(By.XPATH, '//*[@id="bussiness_edit_form"]/div[1]/div/div/div[2]/div[1]/div[4]/div/div/div/select')).select_by_value('3')
driver.find_element(By.XPATH, '')
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys('VAT')
driver.find_element(By.XPATH, '//*[@id="amount"]').send_keys('10')
driver.find_element(By.XPATH, '//*[@id="bussiness_edit_form"]/div[2]/div/button').click()


driver.get("https://svretailmodule.smartqr.app/products/create")
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(unique.unique('product '))
driver.find_element(By.XPATH, '//*[@id="single_dpp"]').send_keys('10')
# driver.find_element(By.XPATH, '').send_keys()
# driver.find_element(By.XPATH, '').send_keys()
# driver.find_element(By.XPATH, '').send_keys()
# driver.find_element(By.XPATH, '').send_keys()
# driver.find_element(By.XPATH, '').send_keys()
# driver.find_element(By.XPATH, '').send_keys()

WebDriverWait(driver, 120).until(
    EC.presence_of_element_located(
        (By.ID, 'hakem')
    )
)