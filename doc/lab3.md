## SKPS21Z_mpalczuk_tkobylecki

# Dokumantacja laboratorium 3
26.11.2021

## Treść
Celem laboratorium 3 było uruchomienie buzzera pasywnego. Jednak tym razem trudność polegała na tym, że skrypt nie miał być napisany w języku `Python`, a w `C`, co oznaczało dodatkową kompilację programu - należało stworzyć paczkę w systemie SDK zawierającą ten program.

## Paczki SDK - wyjaśnienie
Takie podejście, podczas rozwijania swojego programu w `C`, jest wygodne, ponieważ, aby przetestować rozwiązanie na rzeczywistym sprzęcie, nie ma potrzeby budowania obrazu systemu od zera razem z tym programem. Zamiast tego można dodać do obrazu samą paczkę, bez ponownej kompilacji systemu. Ma to szczególne znaczenie, kiedy wystąpi jakiś problem wywołujący potrzebę ponownego wgrania plików na sprzęt (w naszym wypadku Raspberry Pi 4) raz za razem. Bez SDK za każdym razem trzeba by było czekać, aż skompiluje się cały system, co mogłoby zdecydowanie wydłużyć czas pracy i spowodować dużą irytację developera.

## Praca na laboratorium
Nasze prace zaczęliśmy od napisania prostego programu w `C`, któy by emitował określony dźwięk przy pomocy wspomnianego buzzera pasywnego. Następnie, po paru nieudanych próbach, udało nam się zbudować paczkę SDK zawierającą nasz program. Wybrany został wariant "pozytywka". W międzyczasie na komputerze z sali laboratoryjnej wystąpił błąd, który spowodował zamrożenie systemu. Z uwagi na ten oraz inne problemy laboratoria zostały przedłużone i praca nad zadaniami z laboratorium nr 3 była kontynuowana na zajęciach nr 4. Wówczas program w C został już poprawnie zaimplementowany tak, by sterować buzzerem w sposób analogiczny do diody z poprzedniego zadania. Paczka z programem znajduje się w folderze `buzzer_owrt_pkg`, zaś skrypt w C odpowiadający za pracę buzzera to `demo1.c`. Dla wygody sprawdzającego został on skopiowany do pliku `buzzer.c`, znajdującego się w folderze głównym repozytorium.
