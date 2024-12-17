
from colorama import Fore

def number_check(bd, phone12):
    Found = False
    with open(bd, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 2:
            phone = data[1]
            if phone12 in phone:
                id = data[0]
                username = data[2]
                last_name = data[3]
                first_name = data[4]
                print(Fore.RED + f'''
[RESULT]
BaseData: EYE_OF_GOD
PHONE NUMBER: {phone}
ID: {id}
USERNAME: {username}
LASTNAME: {last_name}
FIRSTNAME:  {first_name} 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')
                Found = True


def sdek(bd12, phone12):
    with open(bd12, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[3]
            if phone12 in phone:
                first_name = data[0]
                email = data[1]
                bithday = data[2]
                created_at = data[4]
                status = data[5]
                print(Fore.RED + f'''
[RESULT]
BaseData: SDEK (2022)
PHONE NUMBER: {phone}
FIRSTNAME: {first_name}
EMAIL: {email}
BITHDAY: {bithday}
CREATED AT:  {created_at}
STATUS: {status} 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')

def yandexfood(yandexeda, phone12):
    with open(yandexeda, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone_number = data[0]
            if phone12 in phone_number:
                first_name = data[1]
                full_name = data[2]
                email = data[3]
                adress_sity = data[4]
                adress_street = data[5]
                adress_house = data[6]
                adress_entrance = data[7]
                print(Fore.RED + f'''
[RESULT]
BaseData: YANDEXEDA (2024)
PHONE NUMBER: {phone_number}
FIRSTNAME: {first_name}
EMAIL: {email}
FULL NAME: {full_name}
SITY:  {adress_sity}
STREET: {adress_street}
HOUSE: {adress_house}
ENTRANCE: {adress_entrance} 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')



def peremena(peremoga, phone12):
    found = False

    with open(peremoga, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')


def part1(part_1, phone12):
    found = False

    with open(part_1, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')


def part2(part_2, phone12):
    found = False

    with open(part_2, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')


def part4(part_4, phone12):
    found = False

    with open(part_4, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')


def part3(part_3, phone12):
    found = False

    with open(part_3, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')


def part6(part_6, phone12):
    found = False

    with open(part_6, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if phone12 in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]
                print(Fore.RED + f''')
[RESULT]
BaseData: PEREMENA (2024)
PHONE NUMBER: {phone}
USER ID: {user_id}
REGISTRATION AT: {registration_date}
FIRSTNAME: {first_name}
LAST NAME: {last_name}
MIDDLE NAME: {middle_name}
EMAIL: {email}
BIRTHDAY: {birthday}
GENDER: {gender}
ROLE: {role}
CLASS LETTER: {class_name}
ADRESS: {address}
COUNTRY: {country}
CITIZENSHIP: {citizenship}
REGION: {region}
SCHOOL: {municipal_education}
INSTITUTION NAME: {institution_name}
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')

def newsdek(bd13, phone12):
    with open(bd13, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[3]
            if phone12 in phone:
                first_name = data[0]
                email = data[1]
                bithday = data[2]
                created_at = data[4]
                status = data[5]
                print(Fore.RED + f'''
[RESULT]
BaseData: SDEK (2022)
PHONE NUMBER: {phone}
FIRSTNAME: {first_name}
EMAIL: {email}
BITHDAY: {bithday}
CREATED AT:  {created_at}
STATUS: {status} 
[ADI]

YOU WILL BE RETURN TO MAIN MENU IN 5 SEC
                      ''')