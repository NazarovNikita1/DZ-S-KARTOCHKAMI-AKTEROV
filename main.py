# задание 1
def main():
    score = float(input('Введите оценку по десятибальной шкале'))
    if score == 10:
        print('Ваша оценка по 5-бальной шкале: 5')
    elif score >= 9:
        print('Ваша оценка по 5-бальной шкале: 4')
    elif score >= 8:
        print('Ваша оценка по 5-бальной шкале: 3')
    else:
        print('Неудовлетворительная оценка')


if __name__ == '__main__':
    main()


# задание 2
def main():
    age = int(input('Введите ваш возраст: '))

    if age < 13:
        print('Ребенок')
    elif age < 18:
        print('Подросток')
    elif 18 <= age <= 25:
        print('Юноша/девушка')
    elif 26 <= age <= 60:
        print('Зрелый человек')
    elif age > 60:
        print('Пожилой человек')
if __name__ == '__main__':
    main()


# задание 3
def greet(time):
    if time < 6 or time >= 21:
        return 'Доброй ночи!'
    elif time <= 11:
        return 'Доброе утро!'
    elif time < 15:
        return 'Добрый день!'
    else:
        return 'Доброго вечера!'

hour = int(input())
print(greet(hour))


#задание 4
import random

number_of_tries = 0
target_number = random.randint(1,100)
print("Я загадал какое-то число от 1 до 100 - угадай его")
while True:
    number_of_tries += 1
    user_input = int(input("Ваша догадка: "))
    if user_input < target_number:
        print("ваше число меньше загаданного")
    elif user_input > target_number:
        print ("Ваше число больше загаданного")
    else:
        break

print("ВЫ УГАДАЛИ!")
print (f"Вы пытались {number_of_tries} раз.")
print(f"Загаданное число: {target_number}")
