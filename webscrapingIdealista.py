from bs4 import BeautifulSoup
import requests
import simplejson as json

def get_data_safely(list_, index, default):
    try:
        return list_[index]
    except IndexError:
        list_[index] = default

active_url = "https://www.idealista.com/alquiler-viviendas/valencia/poblats-maritims/el-cabanyal-el-canyamelar/"
req = requests.get(active_url)
data = req.text
soup = BeautifulSoup(data, "html.parser")
idealista_houses = list()
houses = soup.find_all("div", class_="item")
# houses = soup.find_all("element", {"class":"item"})

for house in houses:
    item_link = house.find("a", class_="item-link")
    name = item_link.text
    url = item_link['href']
    price = house.find("span", class_="item-price").text
    details = house.find_all("span", class_="item-details")
    rooms = get_data_safely(details, 0, "")
    size = get_data_safely(details, 1, "")
    moreinfo = get_data_safely(details, 2, "")

    try:
        phone = house.find("a", class_"item-clickable-phone").text
    except AttributeError:
        phone = ""

    idealista_houses.append({
        'name': name,
        'url': url,
        'price': price,
        'rooms': rooms,
        'size': size,
        'moreinfo': moreinfo,
        'phone': phone

    })

next_url = soup.find("a", class_="icon-arrow-right-after")
if not next_url:
    break:
active_url = next_url["href"]


print(json.dumps(idealista_houses, indent=4))
