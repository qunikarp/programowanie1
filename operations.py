from math import sqrt as qq
import numpy as np
import json

def calc():
    while True:
        print('Kalkulator obsługuje tylko podstawowe operacje:\n'
          'Dodawanie: "+", odejmowanie: "-", mnożenie: "*", dzielenie: "/", potęgowanie: "**" i pierwiastkowanie kwadratowe: "qq(liczba pierwiastkowana)"')
        dzialanie = (input('Wpisz swoje działanie: '))
        print(f"Wynik to: {eval(dzialanie)}")
        x = int(input("Jeśli chcesz kontynuować wpisz 1, jeśli powrócić inną wartość: "))
        if x == 1:
            continue
        else:
            break


def percent():
    print('Obliczanie procentów:')
    while True:

        def procent1():
            x = float(input('Wpisz liczbę której procent chcesz otrzymać: '))
            y = float(input('Wpisz procent: '))
            proc1 = x / 100 * y
            print(f'Procent z liczby: {proc1}')
        def procent2():
            x = float(input('Jakim procentem liczby: '))
            y = float(input('jest liczba: '))
            proc2 = y * 100 / x
            print(f'{proc2}%')
        def procent3():
            x = float(input('O jaki procent liczba wzrosła/zmalała z: '))
            y = float(input('do: '))
            proc3 = (y-x)/x * 100
            print(f'{proc3}%')
        def procent4():
            x = float(input('Liczba: '))
            y = float(input('Dodawany procent: '))
            proc4 = x + (y/100 * x)
            print(f'Po dodaniu {y}% liczba wynosi: {proc4}')
        def procent5():
            x = float(input('Liczba: '))
            y = float(input('Odejmowany procent: '))
            proc5 = x - (y/100 * x)
            print(f'Po odjęciu {y}% liczba wynosi: {proc5}')

        print('"1" Obliczanie procentu z liczby')
        print('"2" Obliczanie liczby z procentu')
        print('"3" Obliczanie o ile procent wzrosła/zmalała liczba')
        print('"4" Dodaj procenty do liczby')
        print('"5" Odejmij procenty od liczby')
        print('Jakakolwiek inna wartość - powrót do interfejsu')
        procenty = {
            "1": procent1,
            "2": procent2,
            "3": procent3,
            "4": procent4,
            "5": procent5,
        }
        x = (input("Wybierz operację: "))
        try:
            procenty[x]()
        except KeyError as k:
            break

def avg():
    while True:
        print(f"Żeby wyświetlić średnią wciśnij ENTER!")
        c = []
        d = []
        while True:
            try:
                c.append(float(input("Podaj liczbę: ")))
                d.append(float(input("Podaj wagę: ")))

            except ValueError:
                if c != d:
                    c.pop()
                break
            except TypeError:
                if c != d:
                    d.pop()
                continue
            else:
                continue

        print(f'Podane liczby: {c}')
        print(f'Podane wagi:   {d}')
        if len(c) > 0 and len(d) > 0:
            x = np.average(c, weights=d)
            print(f"Średnia to: {x}")
        else:
            print("Nie wpisałeś liczb!")
        x = int(input("Jeśli chcesz kontynuować wpisz 1, jeśli powrócić inną wartość: "))
        if x == 1:
            continue
        else:
            break


def show10():
    while a == True:
        plik = open("pliczek.txt", "w+")
        rh.write("coś do zapisania")

        x = int(input("Jeśli chcesz kontynuować wpisz 1, jeśli powrócić inną wartość: "))
        if x == 1:
            continue
        else:
            break


def saveandprint():
    while True:



        x = int(input("Jeśli chcesz kontynuować wpisz 1, jeśli powrócić inną wartość: "))
        if x == 1:
            continue
        else:
            break


