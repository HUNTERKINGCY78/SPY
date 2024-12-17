import hashlib
import netifaces
import uuid
import requests
def get_mac_address():
    all_interfaces = netifaces.interfaces()

    interfaces_with_mac = [interface for interface in all_interfaces if netifaces.AF_LINK in netifaces.ifaddresses(interface)]

    mac_addresses = []
    for interface in interfaces_with_mac:
        mac_address_info = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'].upper()
        mac_addresses.append(mac_address_info)

    formatted_mac_address = ':'.join(mac_addresses)

    return formatted_mac_address

def generate_license_key():
    node_uuid = uuid.UUID(int=uuid.getnode()).hex
    encoded_part1 = 'NjM0NWVhcXdhZTEyM3pvbG1hbm5pY2VjaGVsa2trdHF6ZXdxZWRzYWVkeWhod3JzdGV3ZXJxd2Vkc2Z6c2RmZ2ZoZ2VkcnRnZXJzdGV3YXFzZWRxd2UyMTMyMzUyMzRha2Rx'
    encoded_part2 = 'Y2hlbG5pY2V6b2xtYW5ra2t0cXpld3FlZHNhZWR5aGh3cnN0ZXdlcnF3ZWRzZnpzZGZnZmhnZWRydGdlcnN0ZXdhcXNlZHF3ZTIxMzIzNTIzNGFr'

    license_key = f"{node_uuid}{hashlib.sha256(encoded_part1.encode()).hexdigest()}{get_mac_address()}{hashlib.sha256(encoded_part2.encode()).hexdigest()}"
    return hashlib.sha256(license_key.encode()).hexdigest()

def send_telegram_message(message):
    bot_api_key = '7020542876:AAGz4uZX-PSqIPYrQC3w6d0kocoRss5s17Q'
    telegram_api_url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage?chat_id={6933837772}&text={message}'
    requests.get(telegram_api_url)

def main():
    generated_license_key = generate_license_key()
    message_to_send = f"DWIH - {uuid.UUID(int=uuid.getnode()).hex}\nKey - {generated_license_key}"
    send_telegram_message(message_to_send)

    user_input = input("Введите ваш лицензионный ключ: ")
    if user_input == generated_license_key:
        print("Вы прошли проверку на клоуна, поздравляем.")
    else:
        print("Неверный ключ. Попробуйте еще раз.")

if __name__ == "__main__":
    main()


