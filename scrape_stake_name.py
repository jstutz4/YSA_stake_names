from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_page_title(url):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")  # Run in headless mode

    # Specify the path to the pre-installed Geckodriver
    service = FirefoxService('/usr/bin/geckodriver')
    driver = webdriver.Firefox(service=service, options=firefox_options)

    driver.get(url)
    title = driver.title
    driver.quit()
    return title
