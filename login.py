#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

print('Войдите вручную в ваш гугл аккаунт (Сейчас появится браузер)')
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
input('Войдите как обычно, а потом нажмите Enter. Если вам пишут, что вход небезопасен, то создайте новый аккаунт.')
pickle.dump(driver.get_cookies(), open("cookiesgoogle.pkl", "wb"))
print('Вход удался!')
driver.quit()
