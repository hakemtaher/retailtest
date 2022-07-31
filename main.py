import os
import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import login


os.environ['PATH'] += "D:\Program Files\Python37\Lib\site-packages\selenium\webdriver\chrome"
driver = webdriver.Chrome()
driver.get("https://svretailmodule.smartqr.app/login")
driver.implicitly_wait(120)

login.logigitnfo(driver, 'hakem', '123456')
# WebDriverWait(driver, 120).until(
#     EC.presence_of_element_located(
#         (By.ID, 'step-0')
#     )
# )
# end_tour_btn = driver.find_element(By.ID, 'ebd_btn')
# end_tour_btn.click()
f = open('bus.json', "r")
data = json.loads(f.read())
f.close()
for i in data:
    driver.get("https://svretailmodule.smartqr.app/superadmin/business/create")
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located(
            (By.ID, 'name')
        )
    )
    
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="business_register_form"]/input[3]')
        )
    )
    Business_name_box = driver.find_element(By.ID, 'name')
    Select_currency_box = Select(driver.find_element(By.ID, 'currency_id'))
    Country_box = driver.find_element(By.ID, 'country')
    State_box = driver.find_element(By.ID, 'state')
    City_box = driver.find_element(By.ID, 'city')
    Zipcode_box = driver.find_element(By.ID, 'zip_code')
    Landmark_box = driver.find_element(By.ID, 'landmark')
    timezone_box = Select(driver.find_element(By.ID, 'time_zone'))
    Firstname_box = driver.find_element(By.ID, 'first_name')
    Username_box = driver.find_element(By.ID, 'username')
    Password_box = driver.find_element(By.ID, 'password')
    Confirm_box = driver.find_element(By.ID, 'confirm_password')
    Package_box = driver.find_element(By.ID, 'package_id')
    Paid_box = driver.find_element(By.ID, 'paid_via')
    ct = datetime.datetime.now()
    ts = ct.timestamp()
    ts = int(ts)
    ts = str(ts)
    ts = i["username"] + ts
    # i = data['business_details']
    Business_name_box.send_keys(ts)
    Select_currency_box.select_by_value(i["currency_id"])
    Country_box.send_keys(i["country"])
    State_box.send_keys(i["state"])
    City_box.send_keys(i["city"])
    Zipcode_box.send_keys(i["zip_code"])
    Landmark_box.send_keys(i["landmark"])
    timezone_box.select_by_value(i["time_zone"])
    Firstname_box.send_keys(i["first_name"])
    Username_box.send_keys(ts)
    Password_box.send_keys(i["password"])
    Confirm_box.send_keys(i["confirm_password"])
    Package_box.send_keys(i["package_id"])
    Paid_box.send_keys(i["paid_via"])
    submit_btn = driver.find_element(By.XPATH, '//*[@id="business_register_form"]/input[3]')
    submit_btn.submit()

    WebDriverWait(driver, 120).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="toast-container"]/div/div')
        )
    )

driver.find_element(By.XPATH, '//*[@id="superadmin_business_table"]/tbody/tr[1]/td[11]/button').click()
WebDriverWait(driver, 120).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="package_id"]')
        )
    )
Select(driver.find_element(By.ID, 'package_id')).select_by_value('1')
Select(driver.find_element(By.ID, 'paid_via')).select_by_value('offline')
driver.find_element(By.XPATH, '//*[@id="superadmin_add_subscription"]/div[3]/button[1]').click()



WebDriverWait(driver, 120).until(
    EC.presence_of_element_located(
        (By.ID, 'hakem')
    )
)
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


WebDriverWait(driver, 120).until(
    EC.presence_of_element_located(
        (By.ID, 'hakem')
    )
)