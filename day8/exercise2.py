# We have to print a dictionary in below format by taking user input:

# users = {
#     'name' : 'Amitesh',
#     'age' : 24,
#     'fav_movies' : ['coco', 'avengers'],
#     'fav_songs' : ['song1', 'song2'],
# }

users = {}
name = input('Enter the name: ')
age = input('Enter the age: ')
fav_movies = input('Enter your fav movies separated by comma: ').split(',')
fav_songs = input('Enter your fav songs separated by comma: ').split(',')
print('\n')

users['name'] = name
users['age'] = age
users['fav_movies'] = fav_movies
users['fav_songs'] = fav_songs

for key, value in users.items():
    print(f'{key} : {value}')