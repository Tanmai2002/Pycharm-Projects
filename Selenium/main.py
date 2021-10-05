# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

calss="LC20lb DKV0Md"
Path=r"C:\Users\tanma\Desktop\myprograms\Operadriver\operadriver.exe"
driver=webdriver.Opera(executable_path=Path)
driver.get("https://www.google.com/")
try:
    print(driver.title)
    search=driver.find_element_by_name("q")
    search.send_keys("How do you do?")
    search.send_keys(Keys.RETURN)
    time.sleep(10)
    ele=driver.find_element_by_class_name("main")
    print(ele.text)
finally:
    driver.quit()

