import requests
from bs4 import BeautifulSoup

def crawl(url):
    # Send a GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove HTML tags and print text content
        print("Text Content of the Page:")
        print(soup.get_text())
        
        # Find all links on the page
        links = soup.find_all('a', href=True)
        # Print out the links
        print("\nFound Links on the Page:")
        for link in links:
            print("Found link:", link['href'])
            # You can recursively call crawl() on each link if you want to crawl further
            # crawl(link['href'])
    else:
        print("Failed to retrieve content from the URL:", url)

# URL of the website you want to crawl
start_url = 'http://example.com'

# Start crawling
crawl(start_url)import requests
from bs4 import BeautifulSoup

def crawl(url):
    # Send a GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove HTML tags and print text content
        print("Text Content of the Page:")
        print(soup.get_text())
        
        # Find all links on the page
        links = soup.find_all('a', href=True)
        # Print out the links
        print("\nFound Links on the Page:")
        for link in links:
            print("Found link:", link['href'])
            # You can recursively call crawl() on each link if you want to crawl further
            # crawl(link['href'])
    else:
        print("Failed to retrieve content from the URL:", url)

# URL of the website you want to crawl
start_url = 'http://example.com'

# Start crawling
crawl(start_url)
