from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='elements']/button").click()

input("Press Enter to quit")
driver.quit()
