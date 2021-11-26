## SKPS21Z_mpalczuk_tkobylecki

# Dokumentacja laboratorium 1
19.10.2021

Zadaniami na laboratorium były:
1. Złożenie stanowiska laboratoryjnego: zestaw z Raspberry Pi 4B (RPI),
2. Pierwsze uruchomienie RPI, sprawdzenie połączenia sieciowego, wykonanie próbnych transferów plików,
3. Zbudowanie za pomocą Buildroot obrazu Linuxa dla RPI, z init RAM fs,
4. Zbudowanie za pomocą Buildroot obrazu Linuxa dla RPI, z systemem plików na trwałym nośniku,
5. Zbudowanie za pomocą Buildroot obrazu Linuxa dla maszyny wirtualnej i uruchomienie na qemu.

## Przygotowanie stanowiska
Stanowisko zostało przygotowane bez większych problemów, z efektem końcowym wyglądającym jak na zdjęciu przedstawionym w instrukcji:

![](https://media.discordapp.net/attachments/784434620665954364/902290466609959012/unknown.png)

Podłączenie stanowiska zostało zweryfikowane przez prowadzącego.

## Uruchomienie RPI
Za pomocą komendy

`tio /dev/ttyUSB0`

został uruchomiony terminal UART (tio). Następnie zostało zweryfikowane poprawne podłączenie Raspberry Pi do sieci poprzez komendy

`ifconfig`

oraz

`ping 10.42.0.188`

## Kopiowanie plików na RPI
Za pomocą komendy

`cp nazwa_przykladowego_pliku.txt /tftp`

został skopiowany utworzony przez nas plik .txt, po czym został zapisany na naszym RPI poprzez komendę

`curl tftp://10.42.0.1/nazwa_przykladowego_pliku.txt -output nazwa_przykladowego_pliku.txt`

## Kompilacja obrazu Linuxa w Buildroot
### Stworzenie obrazu dla RPI z initramfs
Po pobraniu buildroota archiwum zostało rozpakowane w katalogu tmp, zgodnie z zaleceniami. Kompilacja, wykonana poprzez instrukcje

`make raspberrypi4_64_defconfig`

`make menuconfig`

trwała znacząco dłużej niż przewidywała instrukcja, jednak zakończyła się sukcesem.
Zaznaczone zostały opcje _Toolchain type: External toolchain_, _initramfs_ oraz wyłączone zostało _ext2/3/4_. To ostatnie posunięcie spowodowało liczne błędy, które zostały naprawione dopiero po ponownym włączeniu wyżej wymienionej opcji. Dodatkowo zabrakło pamięci na obrazie karty SD, w związku z czym rozmiar partycji boot w budowanym obrazie został zwiększony poprzez modyfikację pliku genimage-raspberrypi4-64.cfg. Obraz został zbudowany bez dalszych komplikacji poleceniem

`make clean all`

### Uruchomienie zbudowanego obrazu
RPI zostało zrebootowane poleceniem

`reboot`

a następnie RPI zostało zbootowane i wprowadzone w tryb interaktywny. Za pomocą komendy

`dhcp 10.42.0.1:Image`

obraz Linuxa został załadowany na RPI. Zostały zmienione jego zmienne środowiskowe poleceniem

`setenv bootargs "root=/dev/mmcblk0p4 $bootargs_org root=/dev/mmcblk0p4"`

### Uruchomienie z karty SD, z użyciem systemu ratunkowego

Plik Image został skopiowany na RPI, po czym ów komputer został zrebootowany. U-boot został wprowadzony w tryb interaktywny.

# Dokumentacja laboratorium 2
4.11.2021

Zadaniami na laboratorium były:
1. Uruchomienie OpenWRT na RPI 4B
2. Podłączenie podstawowych akcesoriów i ich obsługa przez sysfs oraz za pomocą
Pythona
    - GPIO - wyjście dla LED (10-krotne włączenie i wyłączenie diody LED)
    - GPIO - wyjście dla LED z płynną zmianą jasności (np. funkcją sin)
3. Przywrócenie początkowego obrazu karty SD

## OpenWRT
Najnowsza wersja OpenWRT została zainstalowana na urządzeniu Raspberry Pi 4 z adresu podanego w instrukcji do laboratorium. Został w tym celu wykorzystany system ratunkowy Raspbian. Potrzebna do tego była modyfikacja tablicy partycji, ponieważ w swoim stanie podstawowym zostałby jedynie uruchomiony system ratunkowy. Dzieje się tak, ponieważ program ładujący Raspberry Pi dostosowuje DT do Raspbiana i Buildroota, podczas gdy OpenWRT nie jest kompatybilny z tymi ustawieniami. Po zamianie linijek w pliku konfiguracyjnym należało zrestartować system. Wówczas objawił się nam system OpenWRT. Aby uzyskać dostęp do sieci, a zarazem instalacji programów (np. edytorów, z których wiadomo jak wyjść), należało dokonać edycji pliku konfiguracyjnego. Sekcja `device` została usunięta, zaś konfiguracja interfejsu `lan` została dostosowana do naszych potrzeb poprzez usunięcie wybranych linijek oraz alterację pozostałych. Sieć następnie została zrestartowana, po czym system OpenWRT był już gotów na kolejne wyzwania.

## Obsługa akcesoriów przez GPIO
W języku `Python` został napisany skrypt `dioda.py` służący do sterowania diodą LED. Na początku został on skonfigurowany tak, by dioda migała z określonym interwałem, następnie zaś skrypt został zmodyfikowany tak, by dioda płynnie zmieniała swoją jasność. Zostało to przeprowadzone poprzez stopniową zmianę częstotliwości migania diody. W obu przypadkach należało jednak najpierw przygotować środowisko OpenWRT do przyjęcia programu w `Pythonie`. Pierwszym krokiem potrzebnym do tego celu było zainstalowanie `Pythona` oraz pakietu `pip` za pomocą menedżera pakietów `opkg`. Z pomocą zainstalowanego już pakietu `pip` możliwa była instalacja kolejnego pakietu `Pythona` o nazwie gpio4. Wówczas zostało zaobserwowane poprawne działanie obu programów.

# Dokumantacja laboratorium 3
26.11.2021

## Treść
Celem laboratorium 3 było uruchomienie buzzera pasywnego. Jednak tym razem trudność polegała na tym, że skrypt nie miał być napisany w języku `Python`, a w `C`, co oznaczało dodatkową kompilację programu stworzyć paczkę w systemie SDK zawierającą ten program.

## Paczki SDK - wyjaśnienie
Takie podejście, podczas rozwijania swojego programu w `C`, jest wygodne, ponieważ, aby przetestować rozwiązanie na rzeczywistym sprzęcie, nie ma potrzeby budowania obrazu systemu od zera razem z tym programem. Zamiast tego można dodać do obrazu samą paczkę, bez ponownej kompilacji systemu. Ma to szczególne znaczenie, kiedy wystąpi jakiś problem wywołujący potrzebę ponownego wgrania plików na sprzęt (w naszym wypadku Raspberry Pi 4) raz za razem. Bez SDK za każdym razem trzeba by było czekać, aż skompiluje się cały system, co może zdecydowanie wydłużyć czas pracy i spowodować dużą irytację developera.

## Praca na laboratorium
Nasze prace zaczęliśmy od napisania prostego programu w `C`, któy by emitował jakiś dźwięk przy pomocy wspomnianego buzzera pasywnego. Następnie, po paru nieudanych próbach, udało nam się zbudować paczkę SDK zawierającą nasz program. Wybrany został wariant > pozytywka
