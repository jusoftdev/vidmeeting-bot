import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Tylko ty jesteś odpowiedzialny za swoje czyny. Projekt dotyczy tylko ilustracji Python i Selenium")
link = input("Link do konferencji (tylko bigbluebutton)")
name = input("Jak masz na imię?")
dur = int(input("Czas trwania konferencji (w sekundach)"))

driver = selenium.webdriver.Firefox()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
