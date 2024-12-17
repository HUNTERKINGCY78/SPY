import urllib.request
import json
import os
from colorama import Fore

getIP = input(Fore.RED + 'ENTER IP: ')
url = "https://ipinfo.io/" + getIP + "/json"
try:
    getInfo = urllib.request.urlopen(url)
except:
    print(Fore.RED + 'IP NOT FOUND')
infoList = json.load(getInfo)


def whoisIPinfo(ip):
    try:
        myComand = "whois " + getIP
        whoisInfo = os.popen(myComand).read()
        return whoisInfo
    except:
        return "Error 404"


print("IP: ", infoList["ip"])
print("Город: ", infoList["city"])
print("Регион: ", infoList["region"])
print("Страна: ", infoList["country"])
print("Временная зона: ", infoList["timezone"])
print("Координаты: ", infoList["loc"])
print("Название хоста: ", infoList["hostname"])
print("Индекс: ", infoList["postal"])
