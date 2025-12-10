import requests
from bs4 import BeautifulSoup
import time 
url = "https://github.com/etano/productner/blob/master/Product%20Dataset.csv"
headers = {"User-Agent":(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
)}
response = requests.get(url, headers=headers)
print("Status code ", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("tr"):
    print(link.text)

print(response.text[:500])