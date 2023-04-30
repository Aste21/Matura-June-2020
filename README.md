# Matura-June-2020
Matura June 2020

Task:

    Zadanie 4. Pary
W pliku pary.txt znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą
się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągu znaków) złożonego z małych
liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem
spacji.
Napisz program(-my), dający(-e) odpowiedzi do poniższych zadań. Uzyskane odpowiedzi
zapisz w pliku wyniki4.txt, poprzedzając każdą z nich numerem odpowiedniego zadania.
Uwaga: plik przyklad.txt zawiera przykładowe dane spełniające warunki zadania.
Odpowiedzi dla danych z pliku przyklad.txt są podane pod treściami zadań oraz w pliku
odp_przyklad.txt.


    Zadanie 4.1. (0–3)
Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą
dwóch nieparzystych liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie
7 + 13.
Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb pierwszych.
Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej
rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy.
Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku
pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20 należy
wypisać 20 3 17.
Dla danych z pliku przyklad.txt prawidłową odpowiedzią jest:
24 5 19
6 3 3
6 3 3


    Zadanie 4.2. (0–4)
Dla każdego słowa z pliku pary.txt znajdź długość najdłuższego spójnego fragmentu tego
słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości
oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej
samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej
z kolejnością danych w pliku pary.txt.
Przykład:
dla słowa zxyzzzz wynikiem jest:
zzzz 4
natomiast dla słowa kkkabbb wynikiem jest:
kkk 3
Dla danych z pliku przyklad.txt odpowiedzi podano w pliku odp_przyklad.txt. 


    Zadanie 4.3. (0–4)
Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:
– liczba1 < liczba2,
albo
– liczba1 = liczba2 oraz słowo1 jest leksykograficznie (w porządku alfabetycznym)
mniejsze od słowo2.
Przykład:
para (1, bbbb) jest mniejsza od pary (2, aaa), natomiast para (3, aaa) jest mniejsza od pary
(3, ab).
Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których
liczba jest równa długości słowa, i wypisz spośród nich taką parę, która jest mniejsza od
wszystkich pozostałych. W pliku pary.txt jest jedna taka para.
Dla danych z pliku przyklad.txt odpowiedzią jest:
6 abbbbc 
