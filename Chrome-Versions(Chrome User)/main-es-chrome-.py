import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Solo usted es responsable de sus acciones. El proyecto es solo para ilustraciones de Python y Selenium")
link = input("Conexión de conferencia (solo bigbluebutton)")
name = input("¿Cuál es tu nombre?")
dur = int(input("Duración (en segundos)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
