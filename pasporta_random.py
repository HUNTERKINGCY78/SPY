import random
from colorama import Fore


def randm():
    passports = ["Алесич Александр Николаевич,Дата рождения: 28.07.1975,Место рождения: Дивногорск,Серия и номер: 0400 718369,Дата выдачи: 28.08.2001,Место выдачи: 1 ГОМ УВД г. Норильска,Код подразделения: 243007,СНИЛС: 142-877-020 69,ИНН: 245723675816,", "Костюченко Елена Сергеевна,Дата рождения: 22.10.1981,Место рождения: гор. Джамбул Казахской ССР,Серия и номер: 7515 715942,Дата выдачи: 25.11.2015,Место выдачи: Отделом УФМС России по Челябинской области в Ленинском районе гор. Челябинска,Код подразделения: 740054,СНИЛС: 072-899-737 31,ИНН: 742401518302,", "Апарин Геннадий Константинович,Дата рождения: 05.11.1970,Место рождения: г. Воронеж,Серия и номер: 2015 908101,Дата выдачи: 04.12.2015,Место выдачи: Отделом УФМС России по Воронежской области в Советском районе г. Воронежа,Код подразделения: 360007,СНИЛС: 031-192-875 32,ИНН: 366501397932,", "Кошелева Альбина Васильевна,Дата рождения: 16.07.1956,Место рождения: Новосибирская обл г Чулым,Серия и номер: 5003 442250,Дата выдачи: 26.08.2002,Место выдачи: ОВД Железнодорожного района города Новосибирска,Код подразделения: 542002,СНИЛС: 079-089-238 13,ИНН: 540787718581,", "Тупицын Александр Вячеславович,Дата рождения: 13.10.1976,Место рождения: г. Очёр Очёрский район Пермская область РСФСР,Серия и номер: 0719 549993,Дата выдачи: 31.07.2019,Место выдачи: ГУ МВД России по Ставропольскому краю,Код подразделения: 260023,СНИЛС: 028-713-107 40,ИНН: 261500587015,", "Куликов Александр Викторович,Дата рождения: 14.06.1973,Место рождения: с. Калининское Калининского района респ. Кыргызстан,Серия и номер: 4618 972279,Дата выдачи: 23.06.2018,Место выдачи: ГУ МВД России по Московской области,Код подразделения: 500141,СНИЛС: 110-893-694 61,ИНН: 621701233477,", "Павлова Анна Викторовна,Дата рождения: 24.09.1984,Место рождения: Гор.Свердловск,Серия и номер: 6505 468374,Дата выдачи: 06.04.2005,Место выдачи: ом кировского рувд,Код подразделения: 663002,СНИЛС: 148-824-352 91,ИНН: 667005774020,", "Щербаков Анатолий Александрович,Дата рождения: 25.09.1968,Место рождения: ПГТ Тюльган Оренбургской  области,Серия и номер: 5313 356000,Дата выдачи: 07.10.2013,Место выдачи: Отделением Паспортной  работы отдела УФМС России по Оренбургской области в Ленинском  районе г. Оренбурга,Код подразделения: 560048,СНИЛС: 047-103-072 14,ИНН: 563700036803,", "Фролова Ирина Витальевна,Дата рождения: 05.11.1989,Место рождения: Г. ФЕРГАНА УЗ. ССР,Серия и номер: 5214 367263,Дата выдачи: 17.09.2014,Место выдачи: ОТДЕЛОМ УФМС РОССИИ ПО ОМСКОЙ ОБЛАСТИ В ОМСКОМ РАЙОНЕ,Код подразделения: 550027,СНИЛС: 173-718-631 89,ИНН: 552809621434,"]
    random_passports = random.choice(passports)
    print(Fore.RED + "Рандомный пасспорт:", random_passports)