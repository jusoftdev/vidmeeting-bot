import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Tu singur ești responsabil pentru acțiunile tale. Proiectul este doar pentru ilustrația Python și Selenium")
link = input("Link către conferință (numai bigbluebutton)")
name = input("Care e numele tău?")
dur = int(input("Durata (în secunde)"))

driver = selenium.webdriver.Firefox()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
