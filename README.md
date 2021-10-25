# SKPS21Z_mpalczuk_tkobylecki

## Dokumentacja laboratorium 1
19.10.2021

Zadaniami na laboratorium były:
1. Złożenie stanowiska laboratoryjnego: zestaw z Raspberry Pi 4B (RPI),
2. Pierwsze uruchomienie RPI, sprawdzenie połączenia sieciowego, wykonanie próbnych transferów plików,
3. Zbudowanie za pomocą Buildroot obrazu Linuxa dla RPI, z init RAM fs,
4. Zbudowanie za pomocą Buildroot obrazu Linuxa dla RPI, z systemem plików na trwałym nośniku,
5. Zbudowanie za pomocą Buildroot obrazu Linuxa dla maszyny wirtualnej i uruchomienie na qemu.

# Przygotowanie stanowiska
Stanowisko zostało przygotowane bez większych problemów, z efektem końcowym wyglądającym jak na zdjęciu przedstawionym w instrukcji:
[](https://media.discordapp.net/attachments/784434620665954364/902290466609959012/unknown.png?width=1056&height=676)
Podłączenie stanowiska zostało zweryfikowane przez prowadzącego.

# Uruchomienie RPI
Za pomocą komendy
`tio /dev/ttyUSB0`
został uruchomiony terminal UART (tio). Następnie zostało zweryfikowane poprawne podłączenie Raspberry Pi do sieci poprzez komendy
`ifconfig`
oraz
`ping 10.42.0.188`

# Kopiowanie plików na RPI
Za pomocą komendy
`cp nazwa_przykladowego_pliku.txt /tftp`
został skopiowany utworzony przez nas plik .txt, po czym został zapisany na naszym RPI poprzez komendę
`curl tftp://10.42.0.1/nazwa_przykladowego_pliku.txt -output nazwa_przykladowego_pliku.txt`

# Kompilacja obrazu Linuxa w Buildroot
Po pobraniu buildroota archiwum zostało rozpakowane w katalogu tmp, zgodnie z zaleceniami. Kompilacja, wykonana poprzez instrukcje
`make raspberrypi4_64_defconfig`
`make menuconfig`
trwała znacząco dłużej niż przewidywała instrukcja, jednak zakończyła się sukcesem.
Zaznaczone zostały opcje _Toolchain type: External toolchain_, _initramfs_ oraz wyłączone zostało _ext2/3/4_. To ostatnie posunięcie spowodowało liczne błędy, które zostały naprawione dopiero po ponownym włączeniu wyżej wymienionej opcji. Obraz został zbudowany bez dalszych komplikacji poleceniem
`make clean all`


fdt addr $fdt_addr
fdt get value bootargs_org /chosen
setenv bootargs $bootargs_org

printenv bootargs

bootargs

BR/.config


setenv bootargs "root=/dev/mmcblk0p4 $bootargs_org root=/dev/mmcblk0p4"


sudo dd if=rootfs.ext4 of=/dev/mmcblk0p4

wget https://10.42.0.1/rootfs/.......

root=/dev/mmcblk0p4
