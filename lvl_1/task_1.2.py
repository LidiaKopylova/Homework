# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random

my_favorite_songs = [
    ['Waste a Moment', 3.05],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_index1 = random.randint(0, len(my_favorite_songs) - 1)
print(my_favorite_songs[random_index1][0])
random_index2 = random.randint(0, len(my_favorite_songs) - 1)
print(my_favorite_songs[random_index2][0])
random_index3 = random.randint(0, len(my_favorite_songs) - 1)
print(my_favorite_songs[random_index3][0])
print(
    'Три песни звучат',
    round(my_favorite_songs[random_index1][1] +
          my_favorite_songs[random_index2][1] +
          my_favorite_songs[random_index3][1]), 'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.05,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
song_1 = random.choice(list(my_favorite_songs_dict))
time_1 = my_favorite_songs_dict[song_1]
song_2 = random.choice(list(my_favorite_songs_dict))
time_2 = my_favorite_songs_dict[song_2]
song_3 = random.choice(list(my_favorite_songs_dict))
time_3 = my_favorite_songs_dict[song_3]
print('Три песни звучат', round(time_1 + time_2 + time_3), 'минут')
