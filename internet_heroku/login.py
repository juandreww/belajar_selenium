from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username  = driver.find_element("id", "username")
username.send_keys("belajar_selenium@yahoo.com")

password = driver.find_element("id", "password")
password.send_keys("belajar_itu_menyenangkan")

# elements (multiple)
h2 = driver.find_elements(By.TAG_NAME, "h2")
print(h2)

driver.find_element(By.CLASS_NAME, "radius").click()

# can also use By.LINK_TEXT
# driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()

# Wait for user input before closing the browser window
input("Press Enter to quit")

# Quit the browser
driver.quit()