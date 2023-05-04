import time
from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

path = '/Users/wlax1/Downloads'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://google.com')

# #Maximize window
# driver.maximize_window()
# driver.switch_to.window(driver.current_window_handle)
# driver.implicitly_wait(10)

# #Enter the site
# driver.get('https://www.linkedin.com/login')
# time.sleep(2)

# #Login
# username = '//*[@id="username"]'
# password = '//*[@id="password"]'

# with open('user_creds.txt', 'r', encoding='utf-8') as file:
#   user_credentials = file.readlines()
#   user_credentials = [line.rstrip() for line in user_credentials]
  
# user_username = user_credentials[0]
# user_password = user_credentials[1]

# driver.find_element_by_xpath(username).send_keys(user_username)
# driver.find_element_by_xpath(password).send_keys(user_password)
# time.sleep(1)

# #Click login button
# driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
# driver.implicitly_wait(30)


