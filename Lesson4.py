#Программа, которая запрашвиает у пользователя Имя и дату рождения и отвечает сколько ему лет
name = input('Введите ваше имя: ')
current_year = 2024
date_of_birth = int(input('В каком году вы родились? ')) # Обязательно нужно переводить в тип (int)!
age = current_year -date_of_birth # создаем переменную, которая будет вычислять по формуле (текущий год минус год рождения)
print("Здравствуйте, ", name)
print("В этом году вам ",age, 'лет')

#Работа со строками
#print("привет, я александр". upper(). lower()) #upper - верхний регистр, а lower - нижний регистр
#print("привет, я александр". replace("привет", "Пока")) #измена элементов