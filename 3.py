import requests
from bs4 import BeautifulSoup
from collections import Counter

'''Первым делом напишем парсер '''
animals_lst = ['0']
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

'''Т.к. по условию задания необходимо парсить названия животных кирилицей, 
ставлю условия цикла: (пока первая буква последнего элемента не равна латинской А '''

while animals_lst[-1][0] != 'A':
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    animals = soup.find('div', class_="mw-category-columns").find_all("a")

    for animal in animals:
        animals_lst.append(animal.text)

    links = soup.find('div', id='mw-pages').find_all('a')

    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org' + a.get('href')

'''Далее преобразуем список животных в список заглавных букв'''

alphabet_lst = []
idx = 1

while idx <= (len(animals_lst) - 2):
    alphabet_lst.append(animals_lst[idx][0])
    idx += 1

'''Методом counter считаю количество повторения букв, и сортирую по алфавиту для корректности вывода'''
alphabet_counter = Counter(alphabet_lst)
eng_rus_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
res = sorted(alphabet_counter, key=lambda x: eng_rus_upper.index(x[0][0]))

'''Отсеиваю латинские буквы:
По логике мы успеваем запарсить только небольшое количество значений на латинскую: "A" но из-за бага 
википедии отсеиваем еще и "H" (почему-то в алфавитном списке вики на букву Д записанно название латинскими буквами'''
for i in res:
    if i != 'A':
        if i != 'H':
            print(i + ':', alphabet_counter[i])
