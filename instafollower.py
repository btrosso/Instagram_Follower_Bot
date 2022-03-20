import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
load_dotenv()


class InstaFollower:

    def __init__(self):
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(os.environ['INSTA_USER'])

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(os.environ['INSTA_PASSWORD'])

        time.sleep(1)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        time.sleep(10)
        not_now_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()
        time.sleep(5)

        self.driver.get(f"https://www.instagram.com/{os.environ['SIMILAR_ACCOUNT']}/")
        time.sleep(3)


    def find_followers(self):
        followers_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/'
                                                              'ul/li[2]/a/div')
        followers_button.click()
        time.sleep(5)
        scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        # In this case we're executing some Javascript, that's what the execute_script() method does.
        # The method can accept the script as well as a HTML element.
        # The element_inside_popup in this case, becomes the arguments[0] in the script.
        # Then we're using Javascript to say: "scroll the top of the element_inside_popup (popup)
        # element by the height of the element_inside_popup (popup)"
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(3)

    def follow(self):
        people_to_follow = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for person in people_to_follow:
            try:
                person.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
                time.sleep(2)
            else:
                continue

