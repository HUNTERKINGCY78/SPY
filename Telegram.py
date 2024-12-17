from colorama import Fore

def tg(tgbase, username):
    with open(tgbase, 'r', ) as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 6:
            tg = data[5]
            if username in tg:
                system_number = data[0]
                name = data[1]
                last_name = data[2]
                phone_number = data[3]
                ID = data[4]
                was_online = data[6]
                print(Fore.RED + f'''
[RESULT]
BaseData: Telegram (2024)
USERNAME: {tg}
NAME: {name}
LAST NAME: {last_name}
Phone Number: {phone_number}
ID: {ID}
Was Online: {was_online}
System Number: {system_number}
[IDO]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')