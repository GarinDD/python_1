print("Personal info")
name = input("Введите имя ")
age = input("Введите возраст ")
height = input("Введите рост (в см) ")
address = input("Введите адрес ")
preferences = input("Введите предпочтения ")
print(name,age,height,preferences)

if name == "Daniel":
  print(name)

var_1 = 5
var_2 = 2

print(var_1 + var_2)
print(var_1 - var_2)
print(var_1 * var_2)
print(var_1 / var_2)
print(var_1 ** var_2) #возведение в степень
print(var_1 // var_2) #деление нацело
print(var_1 % var_2) #остаток от деления

print(var_1 > var_2)
print(var_1 < var_2)
print(var_1 >= var_2)
print(var_1 <= var_2)
print(var_1 != var_2) #не равно
print(var_1 == var_2) #равно

q_1 = "Когда начинается урок?"
q_2 = "Сколько длится урок?"
q_3 = "Кто проводит урок?"

a_1 = "В 18:30"
a_2 = "3 часа"
a_3 = "Кирилл"

result = 0

print(q_1)
user_A = input("Введите ответ ")
if user_A == a_1:
  result += 1
  print("Правильно")
else:
  print("Неверно")

print(q_2)
user_A = input("Введите ответ ")
if user_A == a_2:
 result +=1
 print("Правильно")
else:
 print("Неверно")


print(q_3)
user_A = input("Введите ответ ")
if user_A == a_3:
  result += 1
  print("Правильно")
else:
  print("Неверно")

if result == 1:
 print("Поздравляю, у вас 1 правильный ответ")
elif result == 2 or result == 3:
 print("Поздравляю, у вас", result , "правильных ответа")


var_1 = 0
while var_1 < 5:
  var_1 += 1
  print(var_1)

  import random

print("------------Угадай загаданное число------------")
print("Вам нужно угадать заданное число!")
print("Число находится в промежутке от 1 до 10")

number = random.randint(1,10)
count = 0
user_number = 0

while user_number != number:
  user_number = int(input("Ваше число: "))
  count+=1

if number > user_number:
  print("Загаданное число больше, чем ваше!")
elif number < user_number:
  print("Загадаггле число меньше, чем ваше!")

print("Ты выйграл! У тебя получилось с", count, "попытки")