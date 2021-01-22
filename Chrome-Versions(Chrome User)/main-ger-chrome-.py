import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Du allein bist für deine Handlungen verantwortlich. Das Projekt dient nur zur Veranschaulichung von Python und Selenium")
link = input("Link zur Konferenz(nur bbb)")
name = input("Wie ist dein Name?")
dauer = int(input("Dauer der Konferenz (in sek)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dauer)
driver.quit()
