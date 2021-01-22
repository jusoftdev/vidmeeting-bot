import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Você é o único responsável por suas ações. O projeto é apenas para ilustração em Python e Selenium")
link = input("Link para a conferência (apenas bigbluebutton)")
name = input("Qual o seu nome?")
dur = int(input("Duração (em segundos)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
