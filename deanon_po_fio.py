import time
from colorama import Fore


def get_id(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 0:
            fio = data[0]
            if search_value in fio:
                fio = data[0]
                date_birth = data[1]
                sity = data[2]
                passport = data[3]
                gaved = data[4]
                mesto = data[5]
                cod = data[6]
                snils = data[7]
                inn = data[8]
                print(Fore.RED + f'''
[RESULT]
BaseData: QIVI (2020)
Full Name: {fio}
SITY: {sity}
PASSPORT: {passport}
BITHDAY: {date_birth}
CREATED AT:  {gaved}
MESTO: {mesto}
COD: {cod}
SNILS: {snils}
INN: {inn}
[ADI]
                ''')

                time.sleep(4)
                found = True

    if not found:
        print("Ничего не найдено в базе")
        time.sleep(2)
