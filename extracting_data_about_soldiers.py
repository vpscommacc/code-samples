# -*- coding: utf-8 -*-

import xlrd
import xlwt
import xlutils
import os
import csv

# записываем путь к текущему файлу в переменную
file = os.path.abspath(__file__)
l_fio = ["Альмир", "Михаил", "Зинур", "Иван", "Николай"]


# создаём функцию для получения пути к нужному файлу программно
def dr(di, fi):
    # превращаем строку(путь к файлу) в список
    lst = file.split(os.sep)
    # создаём новый список в который записываем срез содержащий путь к папке с файлом
    ks = lst[0:-1]
    # в конец списка добавляем новую папку
    ks.append(di)
    # в конец списка добавляем новый файл
    ks.append(fi)
    # превращаем список обратно в строку используя разделитель файлов
    nt = os.sep.join(ks)
    return nt


p = dr('files', 'rvsn.xls')
cs = dr('files', 'dmbs.csv')

# получаем все ярлыки
# получаем индекс ярлыка "дембеля"
# используем индекс в коде ниже

with xlrd.open_workbook(p, 'r', formatting_info=True) as xl:
    # получаем названия листов
    names = xl.sheet_names()
    dmb = names.index('дембеля')
    lst = names.index('список')
    read = xl.sheet_by_index(dmb)
    colread = xl.sheet_by_index(lst)
    print(type(names), '\n')
    for row in range(read.nrows):
        # запись данных листа в переменную
        wor = read.row_values(row)
        lewor = len(str(wor[0] + wor[1] + wor[2]).strip())
        if lewor == 0:
            continue
        dmbs = ' '.join(wor)
        with open(cs, 'a', encoding="utf-8", newline='') as dmbs:
            writer = csv.writer(dmbs, delimiter=',')
            # запись данных в файл
            writer.writerow(wor)
    # получаем заголовки столбцов в таблице
    loc = ' '.join(colread.row_values(3))
    print(loc, '\n')
    # - перебираем лист "список"
    for col in range(colread.nrows):
        # - записываем значения ячеек в список
        olc = colread.row_values(col)
        # - запись определённых столбцов в переменные
        fio = olc[1]
        days = olc[9]
        # - перебор столбца фамилий
        for io in l_fio:
            # - если в столбце есть не фамилии, пропускаем их
            if not io in fio:
                continue
            print(fio)
        # - если не float, пропускаем этот тип данных
        if not isinstance(days, float):
            continue

        print(round(days))
