import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Vous êtes seul responsable de vos actes. Le projet est pour l'illustration Python et Selenium uniquement")
link = input("Lien vers la conférence (uniquement bigbluebutton)")
name = input("Quel est votre nom?")
dur = int(input("Durée de la conférence (en secondes)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
