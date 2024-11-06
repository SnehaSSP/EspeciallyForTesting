from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/Users/somud/Downloads/chromedriver-mac-x64 2/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")