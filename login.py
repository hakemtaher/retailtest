from selenium import webdriver
from selenium.webdriver.common.by import By


def loginfo(driver, username, password):
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
