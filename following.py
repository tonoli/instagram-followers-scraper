from datetime import datetime
import getpass
import os
import pickle
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

target = input('Enter the target username: ')
chromedriver_path = 'drivers/chromedriver'
driver = webdriver.Chrome(chromedriver_path)

driver.get('https://www.instagram.com')

# Go to log in
login_link = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Log in'))
)
login_link.click()

# Authenticate
username = driver.find_element_by_xpath('//input[@placeholder="Username"]')
password = driver.find_element_by_xpath('//input[@placeholder="Password"]')

print('\nEnter your Instagram credentials')

username.send_keys(input('Username: '))
password.send_keys(getpass.getpass())
password.send_keys(Keys.RETURN)
time.sleep(1)

# Go to user profile and click following
driver.get('https://www.instagram.com/%s/' % target)
following_link = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'following'))
)
following_link.click()
time.sleep(1)

# Select scrollable users div
users_list_container = driver.find_element_by_xpath(
    '//div[@role="dialog"]//ul/parent::div'
)

# Get the actual list of `li` elements
def get_updated_user_list(index = None):
    users = users_list_container.find_elements(By.XPATH, 'ul//li')
    if index == None:
        return users
    return users[index:]

# Scroll an element
def scroll(element, times = 1):
    while times > 0:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight',
            element
        )
        time.sleep(.2)
        times -= 1

# While there are more users scroll and save the results
links = []
last_user_index = 0
updated_list = get_updated_user_list()

while updated_list[last_user_index] is not updated_list[-1]:
    scroll(users_list_container, 2)

    for index, user in enumerate(updated_list):
        if index < last_user_index:
            continue

        try:
            link_to_user = user.find_element(By.TAG_NAME, 'a').get_attribute('href')
            last_user_index = index
            if link_to_user not in links:
                links.append(link_to_user)
                print(link_to_user)
        except:
            pass


    updated_list = get_updated_user_list()

# Store the scraped following users link
date = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')
db_path = 'exports/%s/following%s.pkl' % (target, date)
os.makedirs(os.path.dirname(db_path), exist_ok = True)
pickle.dump(links, open(db_path, 'wb'))
print('Number of followers: %i' % len(links))

driver.close()
