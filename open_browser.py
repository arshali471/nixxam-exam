import requests.exceptions
from selenium import webdriver
import chromedriver_autoinstaller
import os
from tkinter import messagebox


def open_browser(url):
    chromedriver_path = chromedriver_autoinstaller.install(os.getcwd())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--kiosk")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # driver = webdriver.Chrome("./chromedriver", 0, chrome_options)
    driver = webdriver.Chrome(chromedriver_path, 0, chrome_options)
    driver.get(url)
