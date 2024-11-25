# Import the function from selenium_utils.py
from selenium_utils import get_page_title

def main(event):
  # Use the function
  url = "https://maps.churchofjesuschrist.org/"
  title = get_page_title(url)
  print(f"The title of the page is: {title}")
  return "hello world"
