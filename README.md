# Instagram-Scraper

Instagram-Scraper jest to prosty skrobak do Instagrama. Podajesz pierwszy hashtag a program sam szuka innych. Jest to wczesna wersja tego programu więc przeszukanie ok 50 hashtagów zajmuję około 20 min

## Włączenie skrobaka

Skrobaka należy włączyć przez Windows Powershell w folderze projektu (powoduje to mniej błędów) oraz wpisania w Powershell komendy:

```bash
python .\scraper.sk
```


## Instrukcja

Po uruchomieniu skrobaka poprzez komendę powyżej, program zapyta o login i hasło do serwisu Instagram
Po odczekaniu kilku sekund skrobak poprosi o podanie pierwszego hashtagu tzw 'Targetu'.
Następuje po tym wyszukanie podobnych hashtagow i wpisaniu go do pliku data.json w folderze DATA. Następnie program poprosi o podanie liczby targetów, które chcemy przeszukać (opcja potrzebna bo jak pisałem wcześniej program jest w fazie rozwoju i potrzebuje torchę czasu na skrobanie). To wszystko skrobak sam wyszuka dane i wpisze je w folder DATA.

## Problemy
Dopiero zaczynam swoją przygodę z takimi programami/skryptami więc jest jeszcze kilka błędów, które muszę naprawić.

Problem 1:
Jeżeli logowanie do serwisu trwa więcej niż 6 sek skrobak zgłosi błąd, że podano błędne hasło. W takim wypadku należy wyłączyć skrobaka i przeglądarkę Firefox. Błąd do naprawienia ale muszę trochę nad nim pomyśleć.

Problem 2:
Podczas gdy wpiszemy pierwszy target, i wyszukiwarka Instagrama nic nie znajdzie w Powershell wyświetli się błąd że nie znaleziono żadnych danych. Program trzeba uruchomić ponownie. Błąd w trakcie naprawiania.

Problem 3:
Podczas gdy ładowanie postu zajmuję więcej niż 20 sek program wyświetli błąd z za długim oczekiwaniem na post, nie zapiszą się również dane do data.json, otherh.txt oraz secdata.json. Błąd w trakcie naprawiania.

## License
[MIT](https://choosealicense.com/licenses/mit/)