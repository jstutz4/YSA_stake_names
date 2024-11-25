# Import the function from scrape_stake_name.py
from scrape_stake_name import get_page_title

def main(event):
    try:
        print("we are at the start")
        url = "https://maps.churchofjesuschrist.org/"
        title = get_page_title(url)
        print(f"The title of the page is: {title}")
        return "hello world"
    except Exception as e:
        print(f"An error occurred: {e}")

main()