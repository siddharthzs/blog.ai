import requests
from bs4 import BeautifulSoup
# blog
url = "https://stayhostfolio.com/blog/the-magnificence-of-ryman-auditorium-a-journey-through-music-history/"

#about us
# url = "https://paluxuryrentals.com/about/"

payload = {}
headers = {
    'User-Agent': 'PostmanRuntime/7.28.4',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the parsed HTML
    text = soup.get_text().strip()
    text = ' '.join(text.split())

    # Print the extracted text
    print(text)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
