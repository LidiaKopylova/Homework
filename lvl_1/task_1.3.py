user_input = input("Введите номер месяца: ")
month = int(user_input)


if 0 < month < 13:
    if month == 1:
        print('Вы ввели Январь. ', 31, 'день')
    elif month == 2:
        print('Вы ввели Февраль. ', 28, 'дней')
    elif month == 3:
        print('Вы ввели Март. ', 31, 'дней')
    elif month == 4:
        print('Вы ввели Апрель. ', 30, 'дней')
    elif month == 5:
        print('Вы ввели Май. ', 30, 'дней')
    elif month == 6:
        print('Вы ввели Июнь. ', 31, 'дней')
    elif month == 7:
        print('Вы ввели Июль. ', 30, 'дней')
    elif month == 8:
        print('Вы ввели Август. ', 31, 'дней')
    elif month == 9:
        print('Вы ввели Сентябрь. ', 30, 'дней')
    elif month == 10:
        print('Вы ввели Октябрь. ', 31, 'дней')
    elif month == 11:
        print('Вы ввели Ноябрь. ', 30, 'дней')
    elif month == 12:
        print('Вы ввели Декабрь. ', 31, 'дней')
        
else:
    print('Такого месяца нет!')
