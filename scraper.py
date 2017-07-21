import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper(object):
    """Starts up a browser and is able to authenticate to Instagram and get
    followers and people following a specific user"""


    def __init__(self, target):
        self.target = target
        self.driver = webdriver.Chrome('drivers/chromedriver')


    def close(self):
        self.driver.close()


    def authenticate(self, username, password):
        print('\nLogging in…')
        self.driver.get('https://www.instagram.com')

        # Go to log in
        login_link = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Log in'))
        )
        login_link.click()

        # Authenticate
        username_input = self.driver.find_element_by_xpath(
            '//input[@placeholder="Username"]'
        )
        password_input = self.driver.find_element_by_xpath(
            '//input[@placeholder="Password"]'
        )

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(1)


    def get_users(self, group, verbose = False):
        print('\nGetting users…')
        self._open_dialog(group)

        links = []
        last_user_index = 0
        updated_list = self._get_updated_user_list()
        initial_scrolling_speed = 5

        # While there are more users scroll and save the results
        while updated_list[last_user_index] is not updated_list[-1]:
            self._scroll(self.users_list_container, 5)

            for index, user in enumerate(updated_list):
                if index < last_user_index:
                    continue

                try:
                    link_to_user = user.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    last_user_index = index
                    if link_to_user not in links:
                        links.append(link_to_user)
                        if verbose == True:
                            print(link_to_user)
                except:
                    if (initial_scrolling_speed > 1):
                        initial_scrolling_speed -= 1
                    pass

            updated_list = self._get_updated_user_list()
        return links


    def _open_dialog(self, group):
        print('\nNavigating to %s profile…' % self.target)
        self._go_to_user_profile(self.target)
        dialog_link = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, group))
        )
        dialog_link.click()
        self.expected_number = int(
            re.search('(\d+)', dialog_link.text).group(1)
        )
        time.sleep(1)
        self.users_list_container = self.driver.find_element_by_xpath(
            '//div[@role="dialog"]//ul/parent::div'
        )


    def _go_to_user_profile(self, username):
        self.driver.get('https://www.instagram.com/%s/' % username)


    # Get the actual list of `li` elements containing the users info
    def _get_updated_user_list(self):
        return self.users_list_container.find_elements(By.XPATH, 'ul//li')


    # Scroll an element
    def _scroll(self, element, times = 1):
        while times > 0:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight',
                element
            )
            time.sleep(.2)
            times -= 1
