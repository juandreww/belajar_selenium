from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://gooogle.com")

# Wait for user input before closing the browser window
input("Press Enter to quit")

# Quit the browser
driver.quit()