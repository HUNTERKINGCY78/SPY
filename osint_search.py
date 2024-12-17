import requests
import pystyle
from colorama import Fore
request_count = 0
last_request_time = 0

API = "6933837772:bikNmZjO" ## Тут твой API
def Search(Term):
    def make_request(Term):
        data =  {"token":API, "request":Term, "limit": 100, "lang":"ru"}
        url = 'https://server.leakosint.com/'
        response = requests.post(url, json=data)
        return response.json()
    data = make_request(Term)
    for source in data["List"]:
        if source == "No results found":
            print(Fore.RED + "[ADI] Ничего не найдено")
        pystyle.Write.Print(f"\n[ADI] База данных -> ", pystyle.Colors.purple_to_red, interval = .001)
        pystyle.Write.Print(f"{source}\n", pystyle.Colors.purple_to_red, interval = .001)
        for item in data["List"][source]["Data"]:
            if str(item) in set():
                continue
            for key, value in item.items():
                pystyle.Write.Print(f"[ADI] {key} -> ", pystyle.Colors.purple_to_red, interval = .001)
                pystyle.Write.Print(f"{value}\n", pystyle.Colors.purple_to_red, interval = .001)
    if "No results found" not in data["List"]:
        print()
        pystyle.Write.Print("=============================================", pystyle.Colors.purple_to_red, interval = 0.005)
        pystyle.Write.Print("ADI", pystyle.Colors.purple_to_red, interval = 0.005)
        pystyle.Write.Print("=============================================", pystyle.Colors.purple_to_red, interval = 0.005)
print(Fore.RED + "Введите номер телефона, почту, инн и тп..")
Term = input("")
Search(Term)