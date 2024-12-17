from colorama import Fore
def dfd(mts, numberss):
    Found = False
    with open(mts, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 3:
            system_number = data[0]
            if numberss in system_number:
                phone_Numbers = data[1]
                organisation = data[2]
                print(Fore.RED + f'''
[RESULT]
BaseData: MTS (2020)
PHONE NUMBER: {phone_Numbers}
System Number: {system_number}
Organisation: {organisation}
STATUS: ACTIVATED 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')
                Found = True

def wildberries(wb_bd, numberss):
    Found = False
    with open(wb_bd, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            kod = data[0]
            if numberss in kod:
                name = data[1]
                comment = data[2]
                phone = data[3]
                sot_phone = data[4]
                work_phone = data[5]
                email = data[6]
                adress = data[7]

                print(Fore.RED + f'''
[RESULT]
BaseData: Wildberries (2024)
ID: {kod}
PHONE NUMBER: {phone}
System Number: {sot_phone}
Organisation: {work_phone}
Name: {name}
Mail: {email}
Adress: {adress}
Комментарий: {comment}
STATUS: ACTIVATED 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')
                Found = True