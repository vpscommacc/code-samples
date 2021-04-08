import lxml
from bs4 import BeautifulSoup
import os

# записываем путь к текущему файлу в переменную
file = os.path.abspath(__file__)


# создаём функцию для подачи пути к нужному файлу
def dr(fi):
    # превращаем строку(путь к файлу) в список
    lst = file.split(os.sep)
    # создаём новый список в который записываем срез содержащий путь к папке с файлом
    ks = lst[0:-1]
    # в конец списка добавляем новый файл
    ks.append(fi)
    # превращаем список обратно в строку используя разделитель файлов
    nt = os.sep.join(ks)
    return nt


# записываем результат функции в переменную и создаём пустой список
s = dr("hhvacancies.html")
vi = []
# начинаем работу с файлом
with open(s, 'r', encoding='utf-8') as new:
    # создаём объект BeautifulSoup
    soup = BeautifulSoup(new, 'lxml')
    # ищем класс vacancy-serp-item
    vac = soup.select(".vacancy-serp-item")
    serpi = BeautifulSoup(str(vac), 'lxml')
    # ищем класс vacancy-serp-item__info внутри vacancy-serp-item
    inf = serpi.select(".vacancy-serp-item__info")
    blo = BeautifulSoup(str(inf), 'lxml')
    # ищем все теги а внутри класса vacancy-serp-item__info
    ak = blo.find_all("a")
    # извлекаем все href из ссылок и записываем их в список
    for i in ak:
        vi.append(i.get("href"))

# запись результата в переменную
answers = "Всё что нашёл, сорри что так мало" + '\n'.join(vi)
