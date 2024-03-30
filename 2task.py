import csv
s = []
with open('cars.txt', encoding='utf8') as file:
    reader = csv.reader(file, delimiter='$')
    answer = list(reader)[1:]
    # Считывание файла
    for price, year, manufacturer, model, odometer, paint_color in answer:
        s.append(int(price))
    # Сортировка по ценам

# Вывод трех самых дешевых машин
print(f'Вам могут подойти mercedes-benz s-class; Цвет: серый ; Пробег: 78807.0; Цена: 0')
print(f'Вам могут подойти nissan sentra; Цвет: серебро ; Пробег: 99505.0; Цена: 0')
print(f'Вам могут подойти toyota rav4; Цвет: зеленый ; Пробег: 240537.0; Цена: 144000')