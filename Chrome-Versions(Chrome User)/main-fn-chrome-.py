import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Sinä olet yksin vastuussa teoistasi. Projekti on tarkoitettu vain Python- ja Selenium-kuvituksiin")
link = input("Linkki konferenssiin (vain bigbluebutton)")
name = input("Mikä sinun nimesi on?")
dur = int(input("Kesto (sekunteina)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
