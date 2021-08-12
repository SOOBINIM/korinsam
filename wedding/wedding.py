import time
from selenium import webdriver

driver = webdriver.Ie(
    'C:\\Users\\임수빈\\Desktop\\IEDriverServer_x64_3.9.0\\IEDriverServer.exe')
time.sleep(2)
driver.get("http://www.google.com")
