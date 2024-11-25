from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

def get_page_title(url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode

    # Specify the path to the pre-installed ChromeDriver
    # service = ChromeService('/Users/jonsoccer/documents/chromedriver-mac-arm64/chromedriver')
    service = ChromeService('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    title = driver.title
    driver.quit()
    return title