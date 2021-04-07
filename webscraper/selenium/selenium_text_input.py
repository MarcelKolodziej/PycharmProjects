from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://login.metafilter.com')

password = "your_real_password_here"

#find and fill Username
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')
#find and fill Password
passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys(password)
passwordElem.submit()

