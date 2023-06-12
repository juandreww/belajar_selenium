from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def find_elements(driver):
  username = driver.find_element("id", "username")
  password = driver.find_element("id", "password")
  radius = driver.find_element(By.CSS_SELECTOR, "button.radius")

  return username, password, radius

def perform_first_task(username, password, radius):
  username.send_keys("belajar_selenium@yahoo.com")
  password.send_keys("belajar_itu_menyenangkan")
  radius.click()

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username, password, radius = find_elements(driver)
perform_first_task(username, password, radius)

h2 = driver.find_elements(By.TAG_NAME, "h2")
print(h2)

input("Press Enter to quit")
driver.quit()
