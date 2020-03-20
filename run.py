#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pickle
import sys
import webbrowser
from time import sleep

from PyQt5 import QtWidgets
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from gui import Ui_Form


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton_4.clicked.connect(self.connect)
        self.ui.pushButton_2.clicked.connect(self.open_q)
        self.ui.pushButton_3.clicked.connect(self.open_y)


    def setHeadless(self):
        self.headless = True


    def open_q(self):
        webbrowser.open_new_tab('https://qiwi.com/n/WENDERCCC')


    def open_y(self):
        webbrowser.open_new_tab('https://money.yandex.ru/to/410016917614556')


    def linuxmode(self):
        self.linux = True


    def connect(self):
        self.enable()
        self.likes()


    def enable(self):
        while True:
            if self.ui.checkBox.isChecked() == True:
                from pyvirtualdisplay import Display
                display = Display(visible=0, size=(400, 300))
                display.start()
            self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Вход в систему...')
            global chrome_options
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            if self.ui.checkBox_2.isChecked() == True:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument('--disable-audio-output')
            chrome_options.add_argument('./webdriver')
            global driver
            driver = webdriver.Chrome(options=chrome_options)
            global actionChains
            actionChains = ActionChains(driver)
            passyt = self.ui.lineEdit_2.text()
            logyt = self.ui.lineEdit.text()
            logyt = logyt.strip()
            passyt = passyt.strip()
            driver.get('https://www.ytmonster.net/login')
            # while True:
            #     try:
            #         driver.find_element_by_css_selector('body > table > tbody > tr > td > div.cf-browser-verification.cf-im-under-attack')
            #         sleep(2)
            #     except:
            #         break
            # sleep(1)
            # while True:
            #     try:
            #         driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()
            #         break
            #     except:
            #         driver.refresh()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="inputUsername"]').send_keys(logyt)
            driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(passyt)
            sleep(1)
            driver.find_element_by_xpath('//*[@id="formLogin"]/button').click()
            sleep(5)
            driver.get('https://www.youtube.com/')
            cookies = pickle.load(open("cookiesgoogle.pkl", "rb"))
            for cookie in cookies:
                if 'expiry' in cookie:
                    del cookie['expiry']
                    driver.add_cookie(cookie)
            driver.refresh()
            driver.get('https://www.ytmonster.net/exchange/likes')
            # try:
            #     driver.find_element_by_css_selector('#news > div > div > div > div.col-lg-2.ml-lg-auto > div > img')
            #     self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Вход в YtMonster не был произведен, начинаем программу заново...')
            #     continue
            # except:
            #     pass
            # self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Вход успешен!')
            break


    def likes(self):
        while True:
            while True:
                try:
                    driver.find_element_by_css_selector('body > div.container-fluid > div > div.col-sm-9.col-md-10.main > div.mainContent > div > div > div > div:nth-child(7) > div > a.likeClick').click()
                    break
                except:
                    sleep(6)
                    try:
                        driver.find_element_by_css_selector('body > div.content.light.padding-top-140 > div.container.padding-top-140 > div > div.col-md-3.copyright > a > img')
                        self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Вход в YtMonster не был произведен')
                        driver.quit()
                        self.enable()
                        self.likes()
                    except:
                        pass
            sleep(1)
            handles = driver.window_handles
            try:
                driver.switch_to.window(handles[1])
            except:
                self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Произошла ошибка! Производим перезапуск...')
                driver.refresh()
                return
            self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Задание началось')
            sleep(3)
            try:
                ltext = driver.find_element_by_css_selector('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/paper-tooltip/div').text()
                if ltext == 'Больше не нравится':
                    self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Вы уже поставили лайк')
            except:
                driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1)').click()
            driver.close()
            driver.switch_to.window(handles[0])
            sleep(1)
            button = driver.find_element_by_css_selector('body > div.container-fluid > div > div.col-sm-9.col-md-10.main > div.mainContent > div > div > div > div:nth-child(7) > div > div > div')
            driver.execute_script("arguments[0].click();", button)
            sleep(23)
            error = False
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div/div/div[3]')
                error = True
            except:
                pass
            if error == True:
                button = driver.find_element_by_css_selector('body > div.container-fluid > div > div.col-sm-9.col-md-10.main > div.mainContent > div > div > div > div:nth-child(7) > div > a.likeSkip > div')
                driver.execute_script("arguments[0].click();", button)
            else:
                pass
            sleep(2)
            self.ui.textBrowser.append('[' + datetime.datetime.today().strftime("%H:%M:%S") + '] Задание выполенено!')



# print('Программа запускается')
# while True:
#     enable()
#     while True:
#         likes()
#         continue

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
