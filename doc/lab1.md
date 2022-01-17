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
