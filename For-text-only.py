import requests
from bs4 import BeautifulSoup

# Define the URL of the web server you want to send requests to
url = 'http://example.com'

# Send a GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Remove HTML tags and print text content
    print("Text Content of the Page:")
    print(soup.get_text())
else:
    print("Failed to retrieve content from the URL:", url)
