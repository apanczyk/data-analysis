# User-agent: *
# CSS, JS, Images
# Allow: /core/*.css$
# Allow: /core/*.css?
# Allow: /core/*.js$
# Allow: /core/*.js?
# Allow: /core/*.gif
# Allow: /core/*.jpg
# Allow: /core/*.jpeg
# Allow: /core/*.png
# Allow: /core/*.svg
# Allow: /profiles/*.css$
# Allow: /profiles/*.css?
# Allow: /profiles/*.js$
# Allow: /profiles/*.js?
# Allow: /profiles/*.gif
# Allow: /profiles/*.jpg
# Allow: /profiles/*.jpeg
# Allow: /profiles/*.png
# Allow: /profiles/*.svg
# Allow: /sites/default/files/styles/
# # Directories
# Disallow: /core/
# Disallow: /profiles/
# Disallow: /sites/default/files/
# # Files
# Disallow: /README.txt
# Disallow: /web.config
# # Paths (clean URLs)
# Disallow: /admin/
# Disallow: /comment/reply/
# Disallow: /filter/tips
# Disallow: /node/add/
# Disallow: /search/
# Disallow: /user/register/
# Disallow: /user/password/
# Disallow: /user/login/
# Disallow: /user/logout/
# # Paths (no clean URLs)
# Disallow: /index.php/admin/
# Disallow: /index.php/comment/reply/
# Disallow: /index.php/filter/tips
# Disallow: /index.php/node/add/
# Disallow: /index.php/search/
# Disallow: /index.php/user/password/
# Disallow: /index.php/user/register/
# Disallow: /index.php/user/login/
# Disallow: /index.php/user/logout/

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request


class Driver:

    driver = webdriver.Chrome()
    titles = []

    def __init__(self):
        self.driver.get('https://www.pap.pl/')
        time.sleep(1)
        self.accept_cookies()
        self.maximize_window()
        self.use_english()
        self.switch_to_business()
        self.save_titles()
        self.save_images()
        self.scroll_down()
        self.last_page()

    def accept_cookies(self):
        cookies = self.driver.find_element(
            by=By.XPATH, value='//*[@id="cookie"]/div/div/div/div/div/div[1]')
        cookies.click()

    def maximize_window(self):
        self.driver.maximize_window()

    def use_english(self):
        english_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="navbar"]/ul[2]/li[3]/a')
        english_button.click()

    def switch_to_business(self):
        business_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="block-mainnavigationen"]/ul/li[3]/a')
        business_button.click()

    def save_titles(self):
        titles = self.driver.find_elements(by=By.CLASS_NAME, value='title')
        for title in titles:
            self.titles.append(
                title.find_element(by=By.TAG_NAME, value='a').text)
        print(self.titles)

    def save_images(self):
        images = self.driver.find_elements(by=By.TAG_NAME, value='img')
        for img in images:
            source = img.get_attribute("src")
            file_name = source.split('/')[-1].split('?')[0]
            print(file_name)
            urllib.request.urlretrieve(source, f'images/{file_name}')

    def scroll_down(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def last_page(self):
        last_page = self.driver.find_element(
            by=By.XPATH,
            value=
            '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a'
        )
        last_page.click()
        last_page = self.driver.find_element(
            by=By.XPATH,
            value=
            '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a'
        )
        print(last_page.text)


driver = Driver()
