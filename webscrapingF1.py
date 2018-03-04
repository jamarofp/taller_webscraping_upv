from bs4 import BeautifulSoup
import requests
import simplejson as json
from slugify import slugify

req = requests.get("http://www.caranddriver.es/formula-1")
data = req.text
soup = BeautifulSoup(data, "html.parser")

article_list = []
articles = soup.find_all("div", class_="landing-feed--story")
