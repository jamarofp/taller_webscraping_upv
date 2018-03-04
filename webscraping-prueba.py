from bs4 import BeautifulSoup
import requests

req = requests.get("http://enreda.coop")
soup = BeautifulSoup(req.text, "html.parser")
contacts = soup.find_all("a", class_="contact")
