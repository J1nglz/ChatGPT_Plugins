import requests
from bs4 import BeautifulSoup

def fetch_content_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Here, we're just grabbing all the text content. Adjustments may be needed based on site structure.
    return soup.get_text()

if __name__ == "__main__":
    url = input("Enter the URL: ")
    content = fetch_content_from_url(url)
    print(content)
