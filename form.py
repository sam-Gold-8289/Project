name = input()
print(name.title())

import datetime

Birthday = input("Введите дату рождения: ")
first_date = datetime.datetime.strptime(Birthday, '%d.%m.%Y')
second_date = datetime.datetime.now()

age = second_date.year - first_date.year

if age in range (1, 13):
    print(name.title(), ", малолетка ты еще по таким сайтам шарить.")
elif age in range (14, 17):
    print(name.title(), ", можешь конечно попробывать, но думaю не надо.")
elif age in range (18, 100):
    print(name.title(), "- Добро пожаловать!")
    x=open('user_1.txt', 'a+')
    x.write(name.title() + "- Больше 18 лет"+'\n')
    x.close()



