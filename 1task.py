import csv


with open('cars.txt', encoding='utf8') as file:
    reader = csv.reader(file, delimiter='$')
    answer = list(reader)[1:]
    # Считывание файла
    for price, year, manufacturer, model, odometer, paint_color in answer:
        if int(odometer[:-2]) < 10000 and paint_color == 'серебро':
            print(f'{manufacturer}{model} есть машина серебряного цвета. Ее стоимость {price} и пробег {odometer}')
            # Нахожение машины серебряного цвета с пробегом меньше 10000

