from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


serv_obj = Service("C:\windows\chromedriver.exe") 
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://openmynetwork.com/register/")

# Fill in registration form
driver.find_element(By.NAME, "signup_email").send_keys("pxetr98@gmail.com")
driver.find_element(By.NAME, "signup_password").send_keys("Test@1234")
driver.find_element(By.NAME, "field_3").send_keys("Test19")
driver.find_element(By.NAME, "field_1").send_keys("pxetri")
driver.find_element(By.NAME, "field_2").send_keys("xetri")
driver.find_element(By.NAME, "field_2").send_keys("xetri")
dropdown_element = driver.find_element(By.ID, "field_8")
dropdown = Select(dropdown_element)
optional_value = "Academy for scholarship"
dropdown.select_by_visible_text(optional_value)
dropdown_element = driver.find_element(By.ID, "field_11")
dropdown = Select(dropdown_element)
optional_value = "Grade 9"
dropdown.select_by_visible_text(optional_value)

driver.find_element(By.ID, "signup_submit").click()

driver.implicitly_wait(5)

success_message = driver.find_element(By.CLASS_NAME, "We’re almost there!").text


if "successfully registered" in success_message.lower():
    print("Registration Test Passed")
else:
    print("Registration Test Failed")


driver.quit()
