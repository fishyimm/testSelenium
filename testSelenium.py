from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# test on 05/01/2016
# send_keys work with fire fox version 44 but more than this might be not work
# send_keys doesnt work on chrome latest version
driver = webdriver.Firefox() # add driver in the same path of your .py you can call this function without add location parameter such as "C:\\Users\\User\\Downloads\\geckodriver.exe"
driver.set_page_load_timeout(10)

driver.get("https://www.facebook.com/")
driver.find_element_by_id('email').send_keys("your email") # enter your email
driver.find_element_by_id('pass').send_keys("your password") # enter your password
button = driver.find_element_by_id('u_0_l') #login button
button.click() #click on login button
time.sleep(3) # need to delay because browser run slower than this program, if not, you cant find element on browser
driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys("Hi this is browser automation testing ^0^") # add text in postbox

time.sleep(3) # need to delay because browser run slower than this program, if not, you cant find element on browser
summitButton = driver.find_element_by_xpath("//button[@data-testid='react-composer-post-button'] ") # post button
summitButton.click() #click on post button
driver.quit() # close browser
