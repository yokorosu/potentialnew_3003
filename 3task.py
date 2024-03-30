import csv

import csv
cnt = 1
t = 0
budgetmin = input('Введите нижнюю границу своего бюджета ')
budgetmax = input('Введите верхнюю границу своего бюджета ')
with open('cars.txt', encoding='utf8') as file:
    reader = csv.reader(file, delimiter='$')
    answer = list(reader)[1:]
    # Считывание файла
    for price, year, manufacturer, model, odometer, paint_color in answer:
        budgetmin = int(budgetmin)
        budgetmax = int(budgetmax)
        if budgetmin <= int(price) <= budgetmax:
            print(f'{cnt}. {manufacturer} {model} цена {price}, пробег данной машины составляет {odometer}')
            cnt += 1
            t += 1

if t == 0:
    print('Ничего не найдено')





