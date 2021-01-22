import time

import selenium
from selenium.webdriver.common.keys import Keys

print("©2021 JuSoft All Rights Reserved")
print("You alone are responsible for your actions. The project is for Python and Selenium illustration only")
link = input("Link to the conference (bigbluebutton only)")
name = input("Whats your name?")
dur = int(input("Duration (in seconds)"))

driver = selenium.webdriver.Chrome()
driver.get(link)

inputElement = driver.find_element_by_id("_b_511-w2v-mle-5pi_join_name")
inputElement.send_keys(name)
inputElement.submit()

time.sleep(dur)
driver.quit()
