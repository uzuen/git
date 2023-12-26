from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def validlog(teacher_one, teacher_onee):
    # path to driver
    driver_path = 'C:\Windows'

    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Navigate to the login page
        driver.get('https://openmynetwork.com/wp-login.php')

        # location of username and password
        username_field = driver.find_element('Email address', 'teacher_one')  
        password_field = driver.find_element('password', 'teacher_one')  

        username_field.send_keys(teacher_one)
        password_field.send_keys(teacher_onee)

        # submit log form
        password_field.send_keys(Keys.RETURN)

        time.sleep(3)

        # if login is sucessfull
        if 'https://openmynetwork.com' in driver.current_url:  
            print('Login successful!')
        else:
            print('Login failed. Check your credentials.')

    except Exception as e:
        print(f'An error occurred: {e}')

    finally:
        # Close the browser window
        driver.quit()

# Example usage:
validlog('teacher_one', 'teacher_one')