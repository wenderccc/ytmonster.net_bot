#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


print('Введите сначала ваш логин от YTMonster, а потом пароль')
passyt = input('Логин: ')
logyt = input('Пароль: ')
with open('pass_yt.txt', 'w') as file:
    file.write(passyt)
with open('log_yt.txt', 'w') as file:
file.write(logyt)
print('Отлично! Теперь, войдите вручную в ваш гугл аккаунт (Сейчас появится браузер)')
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
input('Войдите как обычно, а потом нажмите Enter. Если вам пишут, что вход небезопасен, то создайте новый аккаунт.')
pickle.dump(driver.get_cookies(), open("cookiesgoogle.pkl", "wb"))
print('Вход удался!')
driver.quit()
