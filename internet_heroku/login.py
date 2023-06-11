
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element("id", "username").send_keys("belajar_selenium@yahoo.com")
driver.find_element("id", "password").send_keys("belajar_itu_menyenangkan")
# can also use By.LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()
# elements (multiple)
h2 = driver.find_elements(By.TAG_NAME, "h2")
print(h2)


# Wait for user input before closing the browser window
input("Press Enter to quit")

# Quit the browser
driver.quit()