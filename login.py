
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj=Service("C:\windows\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://site.openmynetwork.com/dev3141567/wp-login.php")
driver.find_element(By.NAME, "log").send_keys("Student_one")
driver.find_element(By.ID, "user_pass").send_keys("student_one")
driver.find_element(By.ID, "wp-submit").click()

act_title=driver.title
exp_title="Open My Networkss"
if act_title==exp_title:
 print("Login Test Passed")
else:
 print("Login Test Failed")
driver.close()