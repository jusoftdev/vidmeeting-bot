import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Tu solo sei responsabile delle tue azioni. Il progetto è solo per l'illustrazione di Python e Selenium")
link = input("Collegamento alla conferenza (solo bigbluebutton)")
name = input("Come ti chiami?")
dur = int(input("Durata (in secondi)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
