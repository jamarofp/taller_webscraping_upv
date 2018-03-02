import requests

req = requests.get("http://enreda.coop")
from bs4 import BeautifulSoup
soup = BeautifulSoup(req.text, "html.parser")
contacts = soup.find_all("a", class_="contact")
