from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "http://www.saucedemo.com/"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(1)
# type a user_id by using find element.
webelement_of_email_input = driver.find_element(By.XPATH, "//input[@id='user-name']" )
webelement_of_email_input.send_keys("standard_user")

# type a password by using find element.
webelement_of_password_input = driver.find_element(By.XPATH, "//input[@type='password']")
webelement_of_password_input.send_keys("secret_sauce")

sleep(1)

# to click a login button for move to the next page.
webelement_of_login_button = driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]')
# print(webelement_of_login_button)
webelement_of_login_button.click()

sleep(1)

#write an text file to print a output

OUTPUT_FILE = "webpage_task_11.txt"

output = open("webpage_task_11.txt","a")

# write data to file 
output.write(f"{driver.title}\t'\n'{driver.current_url}\t'\n'+{driver.page_source}\t"+'\n')
#f.write("\n")
output.write("This data will be written to the file.")

# close file
output.close()

