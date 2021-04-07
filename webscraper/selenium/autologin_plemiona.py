#automate log in Browser game 'Plemiona'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://plemiona.pl')

# login to account
loginElem = browser.find_element_by_id('user')
loginElem.send_keys("Koniusz")

# password
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('marmilka11')

#click login button
try:
    loginButton = browser.find_element_by_class_name('btn-login')
except:
    print("Cannot find a element  by class name ")
loginButton.submit()

#login to choosen server:
try:
    serverLoginButton = browser.find_element_by_class_name('world_button_active')
except:
    print("Cannot login to choosen world ")

try:
    worldLoginButton = browser.find_element_by_class_name('world-select')
except:
    print("Cannot login to world")

