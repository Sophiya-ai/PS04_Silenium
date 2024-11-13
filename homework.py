from selenium import webdriver
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.keys import Keys
#Библиотека с поиском элементов на сайте
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# service = Service('D:\\chromedriver.exe')
options = Options()  # Можно настроить опции, если требуется
options.add_argument("--no-sandbox") #для устранения возможных проблем доступа к системе
options.add_argument("--disable-dev-shm-usage") #для использования разделяемой памяти, что может предотвратить сбои при недостатке ресурсов
# browser = webdriver.Chrome(service=service, options=options)

def func_menu():
    menu = int(input('Выберите одно из действий:\n'
                     '1 : Листать параграфы текущей статьи\n'
                     '2 : Перейти на одну из связанных страниц\n'
                     '3 : Выйти из программы\n'))
    return menu

def func_menu_1():
    menu_1 = int(input('Выберите одно из действий:\n'
                     '1 : Листать параграфы текущей статьи\n'
                     '2 : Перейти на одну из связанных страниц\n'))
    return menu_1


def paragraph(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')  # поиск по имени тега
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

def hatnote(browser):
    try:
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, 'div'):
            # Чтобы искать атрибут класса
            cl = element.get_attribute('class')
            if cl == 'hatnote navigation-not-searchable':
                hatnotes.append(element)
        if not hatnotes:
            print("Нет связанных статей на странице")
            return None
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, 'a').get_attribute('href')
        return link
    except Exception as e:
        print(f"Ошибка при поиске связанных статей: {e}")
        return None

browser = webdriver.Chrome()
try:
    request = input("Ведите запрос для Википедии, учитывая Ё при вводе: ")
    #заходим на главную страницу википедии
    browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
    #проверяем на правильной ли странице находимся
    WebDriverWait(browser, 3)
    assert "Википедия" in browser.title

    #Находим окно поиска по ID, просмотрев код поля поиска
    #search_box = browser.find_element(By.ID, 'searchInput')
    search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'searchInput')))
    #Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
    search_box.send_keys(request)
    WebDriverWait(browser, 5)
    #Добавляем не только введение текста, но и его отправку
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(browser, 3)


    # находим ссылку элемента
    #a = browser.find_element(By.LINK_TEXT, request)
    a = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, request)))

    # кликаем по найденной ссылке
    a.click()
    WebDriverWait(browser, 10)

    while True:
        menu = func_menu()
        if menu == 3:
            break
        elif menu == 1:
            # вывод параграфов по нажатию клавиши enter
            paragraph(browser)
        elif menu == 2:
            # переход на связанную произвольную страницу
            link = hatnote(browser)
            if link != None:
                browser.get(link)
                WebDriverWait(browser, 5)
                menu_1 = func_menu_1()
                if menu_1 == 1:
                    # вывод параграфов по нажатию клавиши enter
                    paragraph(browser)
                elif menu_1 == 2:
                    # переход на связанную произвольную страницу
                    link = hatnote(browser)
                    if link != None:
                        browser.get(link)
                        WebDriverWait(browser, 5)


except Exception as e:
    print(f"Ошибка при навигации по странице: {e}")

finally:
    browser.quit()









