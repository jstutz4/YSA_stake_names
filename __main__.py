# Import the function from selenium_utils.py
from scrape_stake_name import get_page_title

def main(event):
  # Use the function
  print("we are at the starts")
  url = "https://maps.churchofjesuschrist.org/"
  title = get_page_title(url)
  print(f"The title of the page is: {title}")
  return "hello world"
