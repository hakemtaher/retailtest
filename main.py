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

login.loginfo(driver, 'hakem', '123456')
# WebDriverWait(driver, 120).until(
#     EC.presence_of_element_located(
#         (By.ID, 'step-0')
#     )
# )
# end_tour_btn = driver.find_element(By.ID, 'ebd_btn')
# end_tour_btn.click()
ts = business.addBusiness(driver, 'bus.json')




driver.get("https://svretailmodule.smartqr.app/home")
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/header/nav/div/ul/li[2]/a').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/header/nav/div/ul/li[2]/ul/li[2]/div[2]/a').click()


username_box = driver.find_element(By.ID, 'username')
username_box.send_keys(ts)
password_box = driver.find_element(By.ID, 'password')
password_box.send_keys('123456')
login_button = driver.find_element(By.CLASS_NAME, 'btn-login')
login_button.click()


driver.get("https://svretailmodule.smartqr.app/products/create")
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(unique.unique('product '))
driver.find_element(By.XPATH, '//*[@id="single_dpp"]').send_keys(uniform(2.5, 10.0))
driver.find_element(By.XPATH, '').send_keys()
driver.find_element(By.XPATH, '').send_keys()
driver.find_element(By.XPATH, '').send_keys()
driver.find_element(By.XPATH, '').send_keys()
driver.find_element(By.XPATH, '').send_keys()
driver.find_element(By.XPATH, '').send_keys()

WebDriverWait(driver, 120).until(
    EC.presence_of_element_located(
        (By.ID, 'hakem')
    )
)