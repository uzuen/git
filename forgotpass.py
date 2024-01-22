from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj=Service("C:\windows\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://site.openmynetwork.com/dev3141567/wp-login.php")

paragraph_element = driver.find_element("css selector", 'p.lostmenot').click()
driver.find_element(By.NAME, "user_login").send_keys("student_one")
driver.find_element(By.ID, "wp-submit").click()

#act_title=driver.title
#exp_title="Check your email for the confirmation link, then visit the"
        
if "https://site.openmynetwork.com/dev3141567/wp-login.php?checkemail=confirm" in driver.current_url:  
#if act_title==exp_title:
        
        print('passed')
else:
        print('Failed') 

driver.quit()
