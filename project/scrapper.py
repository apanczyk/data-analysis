# -*- coding: utf-8 -*-
import sys
from math import prod
import os
from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException, StaleElementReferenceException
import csv   

class Scrapper:
    url = 'https://www.lego.com'
    endpoints = [
        '/en-pl/categories/age-1-plus-years', 
        '/en-pl/categories/age-4-plus-years',
        '/en-pl/categories/age-6-plus-years', 
        '/en-pl/categories/age-9-plus-years', 
        '/en-pl/categories/age-13-plus-years', 
        '/en-pl/categories/age-18-plus-years'
        ]
    category_endpoint = '?filters.i0.key=categories.id&filters.i0.values.i0=12ba8640-7fb5-4281-991d-ac55c65d8001'
    page_endpoint = '&page='
    driver = webdriver.Chrome()
    delay = 3
    titles = []

    def __init__(self):
        self.create_csv()
        self.driver.get(self.url)
        time.sleep(1.5 + random())
        self.accept_cookies()
        # self.get_all_products()
        products = self.read_products()
        self.gather_all_informations(products)

    def accept_cookies(self):
        try:
            cookies = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="root"]/div[5]/div/div/div[1]/div[1]/div/button')
            cookies.click()
            cookies = self.driver.find_element(
                by=By.XPATH,
                value='/html/body/div[5]/div/aside/div/div/div[3]/div[1]/button[2]'
            )
            cookies.click()
        except:
            print("No cookies")

    def get_all_products(self):
        for endpoint in self.endpoints:
            self.driver.get(f'{self.url}{endpoint}{self.category_endpoint}')
            time.sleep(0.5 + random())

            element = self.driver.find_element(
                by=By.XPATH,
                value='//div[starts-with(@class, "Paginationstyles__PageLinks-")]'
            ).text
            pages = max(map(int, [e for e in re.split("[^0-9]", element) if e != '']))

            for i in range(pages):
                new_url = f'{self.url}{endpoint}{self.category_endpoint}{self.page_endpoint}{i+1}'
                print(new_url)
                self.driver.get(new_url)
                time.sleep(0.5 + random())
                self.get_from_site()            

    def get_from_site(self):
        filtered = set()
        elems = self.driver.find_elements_by_xpath("//a[@href]")
        time.sleep(0.5 + random())
        try:
            for elem in elems:
                element = elem.get_attribute("href")
                if '/product/' in element:
                    filtered.add(element)
        except StaleElementReferenceException:
            print("Message: stale element reference: element is not attached to the page document")
        print(filtered)
        self.create_products(filtered)

    def gather_all_informations(self, products):
        for product in products:
            self.driver.get(product)
            time.sleep(0.5 + random())
            self.fetch_product_info()

    def fetch_product_info(self):
        category, title, price, age, pieces, item = None, None, None, None, None, None
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="main-content"]/div/ol/li[2]/a/span/span')))
        except TimeoutException:
            print("Loading took too much time!")
        try:
            category = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="main-content"]/div/ol/li[2]/a/span/span').text
        except Exception as err:
            print(f'Exception on category {err}')
        try:
            title = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="main-content"]/div/div[1]/div/div[2]/div[2]/h1/span'
            ).text
        except Exception as err:
            print(f'Exception on title {err}')
        try:    
            price = self.driver.find_element(
                by=By.XPATH,
                value='//*[@id="main-content"]/div/div[1]/div/div[2]/div[3]/div'
            ).text
            price = re.findall(r'\d+,\d+', price)
        except Exception as err:
            print(f'Exception on price {err}')
        try:
            age = self.driver.find_element(
                by=By.XPATH,
                value=
                '//*[@id="main-content"]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/span/span'
            ).text
        except Exception as err:
            print(f'Exception on age {err}')
        try:
            pieces = self.driver.find_element(
                by=By.XPATH,
                value=
                '//*[@id="main-content"]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/span/span'
            ).text
        except Exception as err:
            print(f'Exception on pieces {err}')
        try:
            item = self.driver.find_element(
                by=By.XPATH,
                value=
                '//*[@id="main-content"]/div/div[1]/div/div[1]/div[2]/div/div/div[4]/div[1]/span/span'
            ).text
        except Exception as err:
            print(f'Exception on item {err}')
        self.append_csv(f'{category};{title};{price};{age};{pieces};{item}\n')

    def append_csv(self, line):
        print(line)
        with open('scrapped_set_lego.csv', 'a', encoding='utf-8') as f:
            f.write(line)

    def create_csv(self):
        with open('scrapped_set_lego.csv', 'a', encoding='utf-8') as f:
            f.write('category;title;price;age;pieces;item\n')

    def create_products(self, set):
        with open('products.txt', 'a', encoding='utf-8') as f:
            for i in set:
                f.write(f'{i}\n')

    def read_products(self):
        with open('products.txt', 'r', encoding='utf-8') as f:
            return f.read().splitlines()


scrapper = Scrapper()
