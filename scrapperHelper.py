import requests
from bs4 import BeautifulSoup


class ScrapHelper:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'PostmanRuntime/7.28.4',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
        }

    
    def getTextFromHttpLink(self,url: str) -> str:
        response = requests.request("GET", url, headers=self.headers)
        if response.status_code == 200:
            print(response.content)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text().strip().split()
            return ' '.join(text)
        else:
            raise ValueError(f"Invalid URL: {url}")
        
        