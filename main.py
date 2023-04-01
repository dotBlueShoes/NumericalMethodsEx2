from typing import List
from jordanEliminationMethod import jordanElimination

# TEXTS
text_choice: str = "Wybierz źródło układu(1.Plik data.txt, 2.Konsola)"
text_size_of_equation: str = "Podaj ilość równań:"


def main():
    matrix = []
    vector = []

    print(text_choice)
    choice = int(input())
    match choice:
        case 1:
            with open("data.txt", "r") as file:
                for line in file:
                    row = []
                    l = line.strip().split("|")
                    for i, value in enumerate(l):
                        if i != len(l) - 1:
                            row.append(float(value))
                        else:
                            vector.append(float(value))
                    matrix.append(row)
        case 2:
            length = int(input(text_size_of_equation))
            for i in range(length):
                value = []
                for j in range(length):
                    value.append(float(input("Podaj %d wartość dla wiersza %d:" % (j + 1, i + 1))))
                matrix.append(value)
                vector.append(float(input("Podaj wartość dla równania w %d wierszu:" % (i + 1))))
        case other:
            print("Błędna ""Wprowadzono błędny znak nie odpowiadający poleceniu!")
    result = jordanElimination(matrix, vector)
    if result is not None:
        print("Wynik to:")
        for i in range(len(result)):
            print("x%d: %f" % (i, result[i]))


if __name__ == '__main__':
    main()
"""
TO DO:

3.Napisanie raportu
4.Jeszcze raz wszystko przetestować
"""
