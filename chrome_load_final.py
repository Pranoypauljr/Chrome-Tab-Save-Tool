from selenium import webdriver
import time
driver = webdriver.Chrome(
    executable_path="C:\chromedriver.exe")
time.sleep(1)
count = 0
num_of_lines = sum(1 for line in open('tab.txt'))
with open("tab.txt", "r") as file:
    while True:
        tab = file.readline()
        if not tab:
            break
        print(tab)
        link = tab
        try:
            driver.get(link)
        except:
            link_correction = "https://"
            driver.get(link_correction+link)
        if count < num_of_lines-1:
            driver.execute_script(f"window.open('about:blank','{count}tab');")
            driver.switch_to.window(f"{count}tab")
            count = count+1
    file.close()
# The code in this file is used to load all the links to a new chrome driver window
# file execution number:3
