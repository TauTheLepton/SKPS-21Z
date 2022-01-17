## SKPS21Z_mpalczuk_tkobylecki

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