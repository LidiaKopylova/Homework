# Задача 1
# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

string_length = len(my_favorite_songs)

print(my_favorite_songs[0:13])
print(my_favorite_songs[-13:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-26:-15])
