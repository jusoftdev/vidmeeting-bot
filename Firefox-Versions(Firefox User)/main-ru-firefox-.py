import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("Ты единственный, кто отвечает за твои действия. Этот проект только для иллюстрации Python  и Selenium.")
link = input("Ссылка конференции")
name = input("Как тебя зовут?")
dur = int(input("Сколько длится конференция в секундах"))

driver = selenium.webdriver.Firefox()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
