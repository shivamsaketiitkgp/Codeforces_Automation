import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

username = input("Username: ")
password = getpass("Password: ")
problem_link = input("Question Link: ")
filename = "sol.cpp"

browser = webdriver.Chrome('./chromedriver')
browser.get("https://codeforces.com")

browser.find_element_by_link_text("Enter").click()

time.sleep(1)

username_element = browser.find_element_by_id("handleOrEmail")
username_element.send_keys(username)

password_element = browser.find_element_by_name("password")
password_element.send_keys(password)

browser.find_element_by_class_name("submit").click()

time.sleep(5)

browser.get(problem_link)

time.sleep(5)

browser.find_elements_by_tag_name('a')[24].click()

time.sleep(5)

browser.find_element_by_class_name('toggleEditorCheckboxLabel').click()

time.sleep(5)

with open(filename, 'r') as f:
    code = f.read()

code_element = browser.find_element_by_id('sourceCodeTextarea')
code_element.send_keys(code)

time.sleep(1)

browser.find_element_by_class_name('toggleEditorCheckboxLabel').click()

time.sleep(1)

browser.find_element_by_class_name("submit").click()





