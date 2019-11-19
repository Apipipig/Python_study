
from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
elem = browser.find_element_by_id('kw').send_keys('习近平')
# elem.send_keys('')
time.sleep(1)

browser.find_element_by_id('su').click()
time.sleep(1)
elem2 = browser.find_element_by_xpath('//*[@id="2"]/h3/a').click()
browser.refresh()
# linkElem = browser.find_element_by_value('百度一下')
# print(elem)
# browser.quit()

