

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os.path

browser = webdriver.Chrome("C:\chromedriver_win32\chromedriver")

csv_path = "results.csv"

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["backendPerformance_calc", "frontendPerformance_calc"])
# try:
#     file = open(csv_path, 'w', newline='')
#     writer = csv.writer(file)
#     writer.writerow(["backendPerformance_calc", "frontendPerformance_calc"])
# except:
#     print("error opening or writing to the CSV file!")
# finally:
#     file.close()


hyperlink = "http://automationpractice.com/index.php"


iterations = 10

for i in range(iterations):
    browser.get(hyperlink)

    navigationStart = browser.execute_script(
        "return window.performance.timing.navigationStart")
    responseStart = browser.execute_script(
        "return window.performance.timing.responseStart")
    domComplete = browser.execute_script(
        "return window.performance.timing.domComplete")

    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("Back End: %sms" % backendPerformance_calc)
    print("Front End: %sms" % frontendPerformance_calc)

    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
#
        writer.writerow([backendPerformance_calc, frontendPerformance_calc])
    # browser.close()
    print("start next iteration")
