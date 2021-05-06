from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path = PATH) #selecting browser


#login credentials
phone = "+46761177777"
password = "testerQA123"


try:
    driver.set_page_load_timeout(10)
    driver.get("http://stage-www.keyflow.com/en/profile/login")   
except Exception:
    print ('page not found')

#filling the login details
driver.find_element_by_name("phone").send_keys(phone)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_class_name("full-width.primary").click()

time.sleep(3)

#new url
driver.get("https://stage-www.keyflow.com/en/profile/me")
child = driver.find_element_by_xpath("//h1/span")

print(child.text)
time.sleep(5)
driver.quit()

