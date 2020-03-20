Временное описание


Описание
=====================


Бот для авто-выполнения заданий на YTmonster.net. Прост в использовании и можно загрузить на дедик.

Цели
=====================


Известные баги
=====================

- Графическая версия зависает при запуске заданий

Установка на линукс
=====================
1. Скопируйте все эти команды и вставьте в терминал
```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install selenium
sudo pip3 install pyvirtualdisplay
sudo apt-get install unzip
wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin
sudo export PATH=$PATH:/usr/local/bin/chromedriver
wget https://github.com/wenderccc/ytmonster_bot/releases/download/releaseV1.0/ytbot.zip
sudo ytbot.zip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
cd ytbot
```
2. Теперь, если у вас нету граф. оболочки на линуксе, то вам нужно с другого ПК (на виндовсе, или линуксе с граф. оболочкой) перекинуть файлы cookiesgoogle.pkl, log_yt.txt и pass_yt.txt в директорию с программой.
Если оболочка есть, то можете продолжать: 
```bash
python3 login.py
```
Следуйте инструкциям и все! Вводите эту команду:
```bash
python3 frun_subs.py
```
Или
```bash
python3 frun_like.py
```

Установка на виндовс
=====================

1. Установите python
2. Введите в терминале это:
```
pip install selenium
```
3. Установите Chromedriver и добавьте его в переменную среды PATH (Пожалуйста, загуглите)
4. Теперь запустите login.py и следуйте инструкциям
5. Все! Теперь можете запускать frun_subs или frun_likes (subs - подписки, likes - лайки)
