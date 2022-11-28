import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_driver_path = "C:\Development\chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)

url = "http://www.hotornot.com"
driver.get(url)

log_on_with_facebook = driver.find_element(By.XPATH,
                                           value='//*[@id="page"]/div[1]/div[3]/div/div[3]/'
                                                 'div/div[1]/div[1]/div[1]/div/div/a')
log_on_with_facebook.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)

allow_cookies = driver.find_elements(By.CSS_SELECTOR, value="button")[5]
allow_cookies.click()
time.sleep(2)

email_input = driver.find_element(By.ID, value="email")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, value="pass")
password_input.send_keys(PASSWORD)
login_button = driver.find_element(By.ID, value="loginbutton")
login_button.click()
driver.switch_to.window(base_window)
time.sleep(15)

like_button = driver.find_element(By.XPATH, value='//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')

while True:
    try:
        like_button.click()
        time.sleep(2)
    except selenium.common.exceptions.ElementClickInterceptedException:
        try:
            pop_up = driver.find_element(By.XPATH, value='/html/body/aside/'
                                                         'section/div[1]/div/div[1]/div/section/div/h1')
        except selenium.common.exceptions.NoSuchElementException:
            skip_button = driver.find_element(By.XPATH,
                                              value='/html/body/aside/section/div[1]/div/'
                                                    'div/section/div/div/div/div[2]/div')
            skip_button.click()
        else:
            dismiss_button = driver.find_element(By.XPATH, value='/html/body/aside/section/div[1]/div/div[2]/i')
            dismiss_button.click()
    else:
        like_button = driver.find_element(By.XPATH,
                                          value='//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
