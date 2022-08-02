from selenium import webdriver
from selenium.webdriver.common.by import By


def loginfo(driver, username, password):
    
    driver.get("https://svretailmodule.smartqr.app/login")
    driver.execute_script("window.localStorage.setItem('tour_end', 'yes');")
    driver.execute_script(
        "window.localStorage.setItem('upos_app_tour_shown', 'true');")
    driver.execute_script(
        "window.localStorage.setItem('tour_current_step', '0');")
    driver.execute_script(
        "window.localStorage.setItem('skin', 'skin-blue-light');")

    username_box = driver.find_element(By.ID, 'username')
    username_box.send_keys(username)
    password_box = driver.find_element(By.ID, 'password')
    password_box.send_keys(password)
    login_button = driver.find_element(By.CLASS_NAME, 'btn-login')
    login_button.click()

def logout(driver):
    driver.get("https://svretailmodule.smartqr.app/home")
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/header/nav/div/ul/li[2]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/header/nav/div/ul/li[2]/ul/li[2]/div[2]/a').click()
