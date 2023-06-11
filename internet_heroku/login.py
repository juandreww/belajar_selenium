from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element("id", "username").send_keys("belajar_selenium@yahoo.com")

# Wait for user input before closing the browser window
input("Press Enter to quit")

# Quit the browser
driver.quit()