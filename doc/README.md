## SKPS21Z_mpalczuk_tkobylecki

# Dokumentacja projektowa
Mateusz Palczuk, Tymon Kobylecki

## Struktura katalogów
W pliku `dioda.py` znajduje się rozwiązanie zadania laboratoryjnego nr 2.
Polegało ono na implementacji sterowania diodą.
W naszym przypadku program ten wykonywał płynną zmianę jasności diody LED.
Pełna dokumentacja tego zadania najduje się w pliku [lab2.md](lab2.md).

W katalogu `buzzer_owrt_pkg` znajduje się pakiet **OpenWRT** zawierający program służący obsłudze buzzera w ramach zadania laboratoryjnego numer 3.
To zadanie polegało na generacji dźwięku, w naszym przypadku źródłem sygnału sterującego był nasz własny program ("pozytywka").
Ten sam kod znajduje się również w pliku `buzzer.c`.
Pełna dokumentacja tego zadania najduje się w pliku [lab3.md](lab3.md).

Ostatnim zadaniem ukończonym w ramach zajęć laboratoryjnych było wykonanie projektu.
Rozwiązanie tego zadania znajduje się w pliku `projekt.py`.
Pełna dokumentacja tego zadania znajduje się poniżej.

## Opis projektu
Projekt miał na celu połączenie działania czujnika pulsu oraz efektorów w postaci trzech diod LED o różnych kolorach oraz buzzera pasywnego.
Po odczytaniu "zdrowej" wartości pulsu (tj. między 50 bpm a 130 bpm) zapalała się dioda czerwona.
Gdy wartość była bliska zeru (<= 10 bpm), zapalała się zielona dioda, zaś w pozostałych przypadkach świeciła się dioda niebieska.
Po każdym pomyślnym odczytaniu wartości przez czujnik uruchamiany był buzzer pasywny, który wydawał dźwięk o częstotliwości zależnej od wartości odczytu.
Ostatni z tych elemetów miał za zadanie dać możliwość monitorowania wielu stanowisk pomiarowych na raz, na przykład w szpitalu, żeby pielęgniarka mogła nasłuchiwać sygnałów od wielu pacjentów i gdy usłyszy odpowiednio inny dźwięk mogła zareagować.

## Opis zastosowanych rozwiązań
W programie w języku Python wykorzystane zostały biblioteki `gpiod`, `multiprocessing`, `time` oraz `max30105`.
Ta pierwsza wykorzystana została w celu komunikacji z wyprowadzeniami GPIO.
Biblioteki `time` oraz `multiprocessing` posłużyły do obsługi buzzera pasywnego.

Pierwsza z nich została wykorzystana przy generacji programowego sygnału PWM przekazywanego do brzęczyka, zaś użycie drugiej pozwoliło na wykorzystanie wielu procesów w realizacji programu, dzięki czemu działanie buzzera nie zatrzymywało działania LEDów czy czujnika MAX30105.
Zostało w tym celu wybrane rozwiązanie wieloprocesowe, a nie np. wielowątkowe, ponieważ zapewniało ono ciągłość działania programu.
Było to kluczowe, gdyż programowa implementacja generacji sygnału PWM wiązała się z bardzo dużym zużyciem czasu procesora, co powodowało nieciągłą pracę systemu, gdyż przy rozwiązaniu wielowątkowym wszystkie wątki działały na jednym procesorze, co sprawiało, że bywał on przeciążony.
Komunikacja z procesem działającym w tle i generującym odpowiedni dźwięk przy pomocy programowej generacji fali PWM o odpowiednim wypełnieniu została przeprowadzona przy pomocy kolejki, w której każda wiadomość zawierała dwa pola.
Pierwsze było typu `bool` i zawierało wiadomość, czy ostatnio została odczytana nowa wartość tętna.
Kolejne pole natomiast zawierało wartość podaną w uderzeniach na minutę (jeżeli przy ostatniej próbie nie został zarejestrowany nowy odczyt, to powielana była wartość z ostatniego pomyślnego odczytu).

Biblioteka `max30105` pozwoliła nam na uproszczoną obsługę czujnika MAX30105.
Zdecydowaliśmy sie na wykorzystanie tego czujnika, ponieważ komunikował się on z urządzeniem *Raspberry Pi* poprzez protokół **I2C**.
Podjęliśmy próby samodzielnego ustanowienia komunikacji z czujnikiem przy użyciu tego protokołu, ale okazało się to wykraczać poza nasze możliwości.
Z tego też powodu nasza implementacja zakończyła się na etapie stworzenia programu w języku *Python*.

## Realizacja (sprzęt)
Wykorzystanym czujnikiem pulsu był wielofunkcyjny czujnik cząsteczek MAX30105.
Działa on na zasadzie świecenia na daną powierzchnię światłem z różnych diod i obserwacji światła odbitego.
Po analizie wyników można odczytać tętno, sprawdzić stężenie dymu w powietrzu, jak i dokonywać innych ciekawych pomiarów.
Nasze użycie tego czujnika ograniczało się jedynie do odczytu tętna badanego obiektu.

Całość projektu wyglądała następująco:

![Zdjęcie poglądowe](images/zielona.jpg)

z widocznymi trzema diodami LED z lewej strony, buzzerem pasywnym po prawej oraz czujnikiem MAX30105 pośrodku.

Dokładny schemat połączeń został pokazany poniżej:

![Schemat](images/circuit.png)

Pełna lista komponentów wykorzystanych w projekcie to:
- *Raspberry Pi* 4 (wraz ze wszystkimi kablami potrzebnymi do zasilenia oraz poprawnego podłączenia do komputera będącego hostem)
- wielofunkcyjny czujnik cząsteczek MAX30105
- 3 diody LED
    - zielona
    - niebieska
    - czerwona
- 3 oporniki 1 kOhm
- 1 opornik 330 Ohm
- 9 kabli "żeńsko-męskich"

### Uwaga do realizacji sprzętowej
Jesteśmy świadomi, że podpięliśmy zasilanie czujnika opisanego jako 5V do wyprowadzenia 3.3V na komputerze jednopłytkowym *Raspberry Pi*.
Przed użyciem czujnika dużo czytaliśmy o nim na forach internetowych i dowiedzieliśmy się, że podpięcie go do zasilania 5V na płytce *Raspberry Pi* może się źle skończyć tak dla samego czujnika jak i (co gorsza) dla *Raspberry Pi*.
Dowiedzieliśmy się również, że przez to nie będzie działać dioda zielona czujnika `MAX30105`, ale, ponieważ nas do odczytu tętna interesowały jedynie dioda czerwona i świata podczerwonego, postanowiliśmy zastosować się do tej rekomendacji w obawie przed uszkodzeniem czujnika.

## Testy
Testy przebiegały poprzez uruchomienie programu i przyłożenie palca żywego człowieka do czujnika MAX30105. Aby wywołać odczyty wykraczające poza "zdrowy" zakres, palec lekko odrywano, dzięki czemu czujnik nie potrafił zebrać poprawnego odczytu.

Pierwszym zaprezentowanym odczytem jest odczyt "zdrowy" - w zakresie między 50 bpm a 130 bpm.
Zgodnie z przewidywaniami zapaliła się czerwona dioda (efekt widoczny na zdjęciu poniżej), zaś buzzer wybrzmiał dźwiękiem o wysokiej częstotliwości (1.2 kHz).
![Czerwona dioda](images/czerwona.jpg)

W drugiej kolejności przetestowany został odczyt bliski zerowemu ( <= 10 bpm).
Wówczas, zgodnie z założeniami, zapaliła się dioda zielona, a brzęczyk wydał dźwięk o niskiej częstotliwości (600 Hz).
![Zielona dioda](images/zielona.jpg)

Na koniec przetestowana została reakcja na odczyt o "niezdrowej" wartości, nieznajdującej się we wcześniej wymienionych zakresach.
Rezultatem było widoczne światło bijące od niebieskiej diody oraz dźwięk buzzera o umiarkowanej częstotliwości (900 Hz).
![Niebieska dioda](images/niebieska.jpg)

## Instrukcja uruchomienia
Aby uruchomić program i przetestować go na własną rękę należy, po poprawnym podłączeniu całego układu, uruchomić serwer na komputerze będącym hostem, za pomocą komendy `python3 -m http.server`.
Następnie, już na *Raspberry Pi*, należy pobrać plik `projekt.py` za pomocą komendy `wget http://<adres_ip_hosta>/projekt.py`.
Ostatnią komendą potrzebną do uruchomienia programu jest komenda włączająca sam program w języku Python: `python3 projekt.py`.
