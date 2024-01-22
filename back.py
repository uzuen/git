from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj=Service("C:\windows\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://site.openmynetwork.com/dev3141567/wp-login.php")

paragraph_element = driver.find_element("css selector", 'p.lostmenot').click()
anchor_element = driver.find_element(By.CLASS_NAME,'wp-login-log-in bs-sign-in').click()

if "https://site.openmynetwork.com/dev3141567/wp-login.php" in driver.current_url: 
        print('Logout Test Passed')
else:
        print('Logout Test Failed')

driver.close()