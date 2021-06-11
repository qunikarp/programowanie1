import operations
import sys


while True:
    print('Witaj w ezCalc v1.0')
    print('Wybierz działanie które chcesz wykonać')
    print('Wybierz "1" jeśli chcesz skorzystać z podstawowego kalkulatora')
    print('Wybierz "2" do liczenia procentów')
    print('Wybierz "3" do liczenia średniej ważonej')
    print('Wybierz "4" żeby pokazać 10 ostatnich operacji')
    print('Wybierz "5" żeby pokazać historię wszystkich operacji')
    print('Wybierz "6" aby wyjsć z programu')

    UI = {
        1: operations.calc,
        2: operations.percent,
        3: operations.avg,
        4: operations.show10,
        5: operations.saveandprint,

    }
    x = int(input("Wybierz funckję: "))
    if x == 6:
        print('Dziękujemy za skorzystanie z usług ezCalc v1.0\n'
              'Dalsze aktualizacje NIE przewidziane :)')
        break
    try:
        UI[x]()
    except KeyError:
        print("Podano nieprawidłową operację!")




