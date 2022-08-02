
from selenium.webdriver.common.by import By
import json
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import update_data

def addBusiness(driver,jsonFile):
    f = open(jsonFile, "r")
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
        i["name"] += ts        
        i["username"] += ts
        # i = data['business_details']
        Business_name_box.send_keys(i["name"])
        Select_currency_box.select_by_value(i["currency_id"])
        Country_box.send_keys(i["country"])
        State_box.send_keys(i["state"])
        City_box.send_keys(i["city"])
        Zipcode_box.send_keys(i["zip_code"])
        Landmark_box.send_keys(i["landmark"])
        timezone_box.select_by_value(i["time_zone"])
        Firstname_box.send_keys(i["first_name"])
        Username_box.send_keys(i["username"])
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
        update_data.write_json(i)
    #driver.get("https://svretailmodule.smartqr.app/superadmin/business")
    # driver.find_element(By.XPATH, '//*[@id="superadmin_business_table"]/tbody/tr[1]/td[11]/button').click()
    link = driver.find_element(By.XPATH, '//*[@id="superadmin_business_table"]/tbody/tr[1]/td[11]/button').get_attribute('data-href')
    print(link)
    driver.get(link)
    WebDriverWait(driver, 120).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//*[@id="package_id"]')
            )
        )
    Select(driver.find_element(By.ID, 'package_id')).select_by_value('1')
    Select(driver.find_element(By.ID, 'paid_via')).select_by_value('offline')
    driver.find_element(By.XPATH, '//*[@id="superadmin_add_subscription"]/div[3]/button[1]').click()

    #return ts