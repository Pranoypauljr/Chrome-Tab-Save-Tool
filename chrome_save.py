from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
tab_dict = {}
b = []
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    a = driver.current_url
    b.append(a)
c = []
c = b
# file execution number:1
# No further changes in code is required here in this file.
