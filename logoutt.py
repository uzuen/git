from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

def login_with_valid_credentials(username, password):
    serv_obj = Service("C:\windows\chromedriver.exe")  
    driver = webdriver.Chrome(service=serv_obj)

    driver.get("https://site.openmynetwork.com/dev3141567/wp-login.php")

   
    username_field = driver.find_element(By.NAME, "log")  
    password_field = driver.find_element(By.ID, "user_pass")  
    submit_button = driver.find_element(By.ID, "wp-submit")  

    
    username_field.send_keys(username)
    password_field.send_keys(password)

    submit_button.click()

    driver.implicitly_wait(5)

    if "https://site.openmynetwork.com/dev3141567/" in driver.current_url:  
        print('Login Test Passed')
    else:
        print('Login Test Failed')

    return driver  
def profile(driver):
    
    profile = driver.find_element(By.XPATH, "//a[contains(@href, 'https://site.openmynetwork.com/dev3141567/members/student_one')]")
    profile.click()

def logout(driver):
    logout_link = driver.find_element(By.XPATH, "//a[contains(@href, 'https://site.openmynetwork.com/dev3141567/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsite.openmynetwork.com%2Fdev3141567%2F&_wpnonce=4b4f8bb7df')]")
    #logout_link = driver.find_element(By.XPATH, "//li[@class='https://site.openmynetwork.com/dev3141567/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fsite.openmynetwork.com%2Fdev3141567%2F&_wpnonce=8ec9266056']/a[text()='Log Out']") 
    logout_link.click()

   
    driver.implicitly_wait(5)

   
    if "https://site.openmynetwork.com/dev3141567/" in driver.current_url:  # Update with the expected URL after logout
        print('Logout Test Passed')
    else:
        print('Logout Test Failed')

   
    driver.quit()

driver = login_with_valid_credentials("Student_one", "student_one")
profile(driver)
logout(driver)
