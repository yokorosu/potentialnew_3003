import csv

cntred, cntser, cntwhite, cntblack, cntorange, cntgreen, cntseriy, cntbr, cntblue, cntyel = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# Создание счетчиков
with open('cars.txt', encoding='utf8') as file:
    reader = csv.reader(file, delimiter='$')
    answer = list(reader)[1:]
    # Считывание файла
    for price, year, manufacturer, model, odometer, paint_color in answer:
        # подсчет количества машин по цвету
        if paint_color == 'красный':
            cntred += 1
        if paint_color == 'серебро':
            cntser += 1
        if paint_color == 'белый':
            cntwhite += 1
        if paint_color == 'черный':
            cntblack += 1
        if paint_color == 'оранжевый':
            cntorange += 1
        if paint_color == 'зеленый':
            cntgreen += 1
        if paint_color == 'серый':
            cntseriy += 1
        if paint_color == 'коричневый':
            cntbr += 1
        if paint_color == 'коричневый':
            cntblue += 1
        if paint_color == 'синий':
            cntyel += 1
# Вывод
print(f'{cntred} машин цвета красный есть сегодня в наличии')
print(f'{cntser} машин цвета серебро есть сегодня в наличии')
print(f'{cntwhite} машин цвета белый есть сегодня в наличии')
print(f'{cntblack} машин цвета черный есть сегодня в наличии')
print(f'{cntorange} машин цвета оранжевый есть сегодня в наличии')
print(f'{cntgreen} машин цвета зеленый есть сегодня в наличии')
print(f'{cntseriy} машин цвета серый есть сегодня в наличии')
print(f'{cntbr} машин цвета коричневый есть сегодня в наличии')
print(f'{cntblue} машин цвета синий есть сегодня в наличии')
print(f'{cntyel} машин цвета желтый есть сегодня в наличии')

# {'красный', 'серебро', 'белый', 'черный', 'оранжевый',
# 'зеленый', 'серый', 'коричневый', 'синий', 'желтый'}
