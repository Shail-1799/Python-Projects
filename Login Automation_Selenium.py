from selenium import webdriver

driver=webdriver.Chrome()      # initialising browser

driver.get(" add url here ")
driver.maximize_window()


id_field=driver.find_element_by_xpath('//*[@id="email--1"]')
id_field.send_keys("Your Login ID")
pass_field=driver.find_element_by_xpath('//*[@id="id_password"]')
pass_field.send_keys("Your Password")
login=driver.find_element_by_xpath('//*[@id="submit-id-submit"]')
login.click()


