"""

MIT License

Copyright (c) 2020 Jakub aka ColderVoid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

========= KONIEC NUDNYCH LICENCJI ==========

Telegram: https://t.me/ColderVoid
Discord: ColderVoid#6176

Wersja: W sumie nie śledze tego.. Jakaś jedna z pierwszych

"""

# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import urllib.request
import getpass_ak
import numpy
import time
import json
import math


# Sprawdz czy strona dziala
def isworking(idriver):
    print('Sprawdzanie lacza...')
    isup = urllib.request.urlopen("https://www.instagram.com/").getcode()

    if isup == 200:
        print('')
        print('* #### *')
        print("Strona Instagram jest aktywna!")
        print('* #### *')
        print('')
        getpassw(idriver)

    else:
        exitprogram(idriver, reason='Brak stalego polaczenia z serwerem Instagram')


def gettosite(input1, input2, gdriver):
    user = input1
    passw = input2
    print('Trwa logowanie, prosze czekac...')
    gdriver.get('https://www.instagram.com/')

    conandlog(user, passw, gdriver)


def getpassw(idriver):
    input1 = input("Wprowadz login: ")
    input2 = None

    while input2 is None:
        input2 = (getpass_ak.getpass('Wprowadz haslo: '))

        if len(input2) < 6:
            print('')
            print("Wprowadzone haslo jest za krotkie!")
            input2 = None
        else:
            break

    gettosite(input1, input2, idriver)


def wrongpass(input1, idriver):
    user = input1
    input2 = None

    print('')
    print('Twoj login (Jesli wprowadzono zly: uruchom ponownie program): ', input1)
    while input2 is None:
        input2 = (getpass_ak.getpass('Wprowadz haslo ponownie: '))

        if len(input2) < 6:
            print('')
            print("Wprowadzone haslo jest za krotkie!")
            input2 = None

        else:
            break

    conandlog(user, input2, idriver)


def conandlog(user, passw, idriver):
    cdriver = idriver

    # Poczekaj az strona sie zaladuje
    WebDriverWait(cdriver, 10).until(

        EC.presence_of_element_located((By.NAME, 'username'))

    )

    # znajdz div
    usernamediv = cdriver.find_element_by_name("username")
    passworddiv = cdriver.find_element_by_name("password")
    loginbutton = cdriver.find_element_by_xpath("//button[@type='submit']")

    # wyczysc divy
    usernamediv.clear()
    passworddiv.clear()

    # wprowadz dane
    usernamediv.send_keys(user)
    passworddiv.send_keys(passw)
    loginbutton.click()

    try:
        time.sleep(5)
        WebDriverWait(cdriver, 1).until(

            EC.presence_of_element_located((By.XPATH, "//article[@class = '_4_yKc']"))

        )

    except TimeoutException:

        print('')
        print('Zalogowany pomyslnie!')

    else:
        print('')
        print('Podane zle haslo!')
        wrongpass(user, idriver)

    print('Oczekiwanie na komunikaty... (okolo 10 sek)')

    # Szukanie okienka z zapisaniem logowania 1

    try:
        WebDriverWait(driver, 5).until(

            EC.presence_of_element_located((By.XPATH, "//div[@class='pV7Qt        DPiy6            Igw0E     IwRSH    "
                                                      "  eGOV_         _4EzTm                                         "
                                                      "                                                               "
                                                      "       qhGB0 ZUqME']"))

        )

    except NoSuchElementException:

        connector(driver)

    except TimeoutException:

        connector(driver)

    notnow = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")

    notnow.click()

    # Szukanie okienka z powiadomieniem o powiadomieniach xd (po co to wgl komu nwm po co im to ale ok)

    try:
        WebDriverWait(driver, 5).until(

            EC.presence_of_element_located((By.XPATH, "//button[@class='aOOlW   HoLwm ']"))

        )

    except NoSuchElementException:

        connector(driver)

    except TimeoutException:

        connector(driver)

    notnow = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")

    notnow.click()
    connector(driver)


def connector(idriver):
    print('')
    print("Program gotowy do dzialania!")
    searcher(idriver)


def exitprogram(idriver, reason):
    idriver.quit()
    print('')
    print('')
    print(reason)
    exit()


#
# ======================================================================================================================
#
# ======================================================================================================================
#
#                                                  START PROGRAMU
#

def searcher(sdriver):
    # Wprowadzenie pierwszego hashtagu przez uzytkownika

    target = input('Wprowadz pierwszy hashtag (! BEZ ZNAKU "#" !): ')

    # Wprowadzenie hasztagu do pola wyszukiwania
    search = sdriver.find_element_by_xpath("//input[@type = 'text']")

    search.clear()

    hashtag = '#' + target
    hashtag = hashtag.lower()
    print('Pierwszy target: ', hashtag)

    search.send_keys(hashtag)

    time.sleep(2)

    # Wpisanie do tabeli 'searchlist' wszystkich znalezionych hasztagow
    searchlist = sdriver.find_elements(By.PARTIAL_LINK_TEXT, hashtag)

    print('Znaleziono: ', len(searchlist) - 1, 'podobnych hashtagow!')
    print('')
    print('Lista:')
    print('')

    # Ladne wypisanie hashtagow w konsoli
    JSONstarter = '{"TARGET": "' + hashtag + '","SCRAPER":['
    JSONplus = ''
    JSONnext = ','
    JSONend = ']}'

    i = 1
    while i < len(searchlist):
        # inne poprzednie rzeczy
        arr = searchlist[i]
        hlist = arr.text
        hsliced = hlist.split()
        hm = len(hsliced)
        postsnum = ''.join(hsliced[2:hm])
        tpos = i + 0
        pos = str(tpos)

        # Dodanie zera przed liczbami mniejszymi od 10
        if tpos < 10:
            posc = '0' + pos

        else:
            posc = pos

        # Wypisanie listy
        print('[', posc, '] ', hsliced[0], '(', hsliced[1], postsnum, ')')

        i = i + 1

        # Wypisywanie ',' przed przedmiotami w JSON
        JSONprimary = '{"HASH": "' + hsliced[0] + '", "POSTS": "' + postsnum + '"}'
        if i < len(searchlist) and i != len(searchlist):
            JSONprimary = JSONprimary + JSONnext

        JSONplus = JSONplus + JSONprimary

    # Złożenie całego pliku JSON
    JSON = JSONstarter + JSONplus + JSONend

    # Wpisanie JSON do pliku data.json
    JSONwriter = open('DATA/data.json', 'w', encoding='utf-8')
    JSONwriter.write(JSON)
    JSONwriter.close()

    # Wgrywanie danych do pliku JSON
    JSONcreator(driver)


def JSONcreator(cdriver):
    permacom = []
    counter = 0
    endhash = 0
    hashcounter = 0
    fulllikes = 0
    videocounter = 0
    scan = ''
    err = 0
    err2 = 0

    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")

    JSONstarter = '{"TIMESTAMP": "' + timestamp + '","HASHTAGS_INFO":['
    JSONplus = ''
    JSONnext = ','
    JSONend = ']}'

    JSONopen = open('DATA/data.json', 'r', encoding='utf-8')
    JSONj = json.load(JSONopen)
    JSONscrapper = JSONj['SCRAPER']

    # Zapytanie do uzytkownika ile hashtagow chce przeskanowac
    print('')

    while err2 == 0:
        scan = input('Podaj liczbe hashtagow to przeskanowania (Maksymalna liczba: ' + str(len(JSONscrapper)) + '): ')

        try:
            scan = int(scan)

        except ValueError:
            err2 = 0

        else:
            err2 = 1

    if len(JSONscrapper) >= scan > 0:
        err = 1

    while err == 0:
        scan = input('Wprowadz liczbe wieksza od 0 oraz nie przekraczajaca liczby ' + str(len(JSONscrapper)) + ': ')
        scan = int(scan)

        if len(JSONscrapper) >= scan > 0:
            break

    j = 0
    while j < scan:
        time.sleep(2)
        Nsearch = cdriver.find_element_by_xpath("//input[@type = 'text']")

        stat = JSONscrapper[j]
        hashtag = stat['HASH']

        print('')
        print('')

        pos = j + 1
        poss = str(pos)

        if pos < 10:
            posc = '0' + poss

        else:
            posc = poss

        print('===================')
        print('[ ' + posc + ' ] -> ' + 'TARGET: ', hashtag)
        Nsearch.clear()
        time.sleep(1)
        Nsearch.send_keys(hashtag)
        time.sleep(2)
        Nsearch.send_keys(Keys.RETURN)
        Nsearch.send_keys(Keys.RETURN)
        print('')
        print('Zaznaczam najlepsze posty...')
        print('')

        try:
            WebDriverWait(cdriver, 20).until(

                EC.presence_of_element_located((By.XPATH, "//div[@class = 'v1Nh3 kIKUG  _bz0w']"))

            )

        except TimeoutException:

            exitprogram(cdriver, reason='Za dluga odpowiedz serwera. Zamykanie...')

        TOPPost = cdriver.find_elements_by_xpath("//div[@class = 'v1Nh3 kIKUG  _bz0w']")

        # TOP posty hashtagi/statystyki
        r = 0
        sumlikes = 0
        videoloop = 0
        j = j + 1

        while r < 9:
            TOP = TOPPost[r]
            TOP.click()

            try:
                WebDriverWait(cdriver, 20).until(

                    EC.presence_of_element_located((By.XPATH, "//div[@class = 'P9YgZ']"))

                )

            except TimeoutException:

                exitprogram(cdriver, reason='Za dluga odpowiedz serwera. Zamykanie...')

            comment = cdriver.find_elements_by_xpath("//a[@class = ' xil3i']")

            try:
                WebDriverWait(cdriver, 3).until(

                    EC.presence_of_element_located((By.XPATH, "//button[@class='sqdOP yWX7d     _8A5w5    ']/span[1]"))

                )

            except TimeoutException:
                likes = 0
                videocounter = videocounter + 1
                videoloop = videoloop + 1

            else:
                likes = cdriver.find_element_by_xpath("//button[@class='sqdOP yWX7d     _8A5w5    ']/span[1]").text
                likes = likes.replace(' ', '')
                likes = int(likes)

            sumlikes = sumlikes + likes

            hcomment = numpy.array(comment)

            for hc in hcomment:
                hc = hc.text
                if hc.startswith("#"):
                    counter = counter + 1
                    permacom.append(hc)

            time.sleep(1)

            ESCdiv = cdriver.find_element_by_xpath("//div[@class='                    Igw0E     IwRSH      eGOV_      "
                                                   "   _4EzTm                                                         "
                                                   "                         BI4qX            qJPeX            fm1AK  "
                                                   " TxciK yiMZG']/button[@class='wpO6b ' and 1]")
            ESCdiv.click()
            r = r + 1

            permacom = list(dict.fromkeys(permacom))
            hashcounter = hashcounter + counter
            endhash = endhash + counter
            print('Dodatkowych hashtagow: ', counter)
            counter = 0

        # Druga petla

        print('')
        print('RAZEM: ' + str(endhash))

        JSONprimary = '{"HASH": "' + hashtag + '", "ADDITIONAL_HASHTAGS": "' + str(endhash) + '", "HEARTS": "' + str(sumlikes) + '"}'
        if j < int(scan) and j != int(scan):
            JSONprimary = JSONprimary + JSONnext

        JSONplus = JSONplus + JSONprimary
        endhash = 0

        fulllikes = fulllikes + sumlikes
        sumlikes = sumlikes / (9 - videoloop)
        sumlikes = math.ceil(sumlikes)

        print('')
        print('Srednia liczba serduszek pod postami: ', sumlikes)
        print('')

        time.sleep(1)
        home = cdriver.find_element_by_xpath("//div[@class = 'Fifk5']")
        home.click()

        permacom = list(dict.fromkeys(permacom))

    print('')
    print('========')
    print('')
    print('Liczba wszystkich serduszek: ', fulllikes)
    print('')
    print('Ilosc filmikow w wyszukiwaniach: ', videocounter)
    print('')
    print('Ostateczna liczba dodatkowych hashtagow: ', hashcounter)
    print('Lista w pliku otherhashes.txt oraz secdata.json')
    print('')
    print('========')
    print('')

    JSON = JSONstarter + JSONplus + JSONend

    HASHopen = open("DATA/secdata.json", "w", encoding="utf-8")
    HASHopen.write(JSON)

    HASHopen.close()

    txtopen = open("DATA/otherhashes.txt", "w", encoding="utf-8")
    for element in permacom:
        txtopen.write(element + ' ')

    txtopen.close()

    exitprogram(cdriver, reason='Koniec programu. Zamykanie...')


#
#                                                  KONIEC PROGRAMU
#
# ======================================================================================================================
#
# ======================================================================================================================
#


if __name__ == "__main__":
    # options = FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    isworking(driver)
