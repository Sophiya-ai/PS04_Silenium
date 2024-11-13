from selenium import webdriver
import time
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver import Keys
#Библиотека с поиском элементов на сайте
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

#АВТОСКРИНШОТЫ
# browser.get('https://ru.wikipedia.org/wiki/Selenium')
# browser.save_screenshot('sel.png')
# time.sleep(10)
# #browser.quit() #закрыть браузер
# browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
# browser.save_screenshot('dom.png')
# time.sleep(10)
# browser.refresh() #перезагрузка страницы

browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
#проверяем на правильной ли странице находимся
assert "Википедия" in browser.title
time.sleep(10)
#Находим окно поиска по ID, просмотрев код поля поиска
search_box = browser.find_element(By.ID, 'searchInput')
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys('Солнечная система')
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)
#находим ссылку элемента
a = browser.find_element(By.LINK_TEXT, 'Солнечная система')
#кликаем по найденной ссылке
a.click()




