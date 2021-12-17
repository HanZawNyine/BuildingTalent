import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://ouo.io/6b35nY')

print('title : ',driver.title)

human = driver.find_element_by_id("btn-main")
print(human.text)
time.sleep(5)
human.click()

time.sleep(5)
human = driver.find_element_by_id("btn-main")
print(human.text)
time.sleep(5)
human.click()

driver.close()
driver.quit()