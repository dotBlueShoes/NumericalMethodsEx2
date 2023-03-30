from typing import List

# TEXTS
text_size_of_equation: str = "Podaj wielkość równania"

# Values
Equation_size: int


def jordanElimination(matrix: List[List[float]], vector: List[float]):
    number = len(matrix)
    for i in range(number):
        #Zabezpieczenie gdyby mnożnik przy zmiennej którą chcemy obliczyć wynosił zero
        if matrix[i][i] == 0:
            maks = 0
            index=i
            bufor: float
            for x in range(number-i):
                if matrix[i+x][i] > maks:
                    maks=matrix[i+x][i]
                    index=i+x
            for y in range(number):
                bufor=matrix[i][y]
                matrix[i][y]=matrix[index][y]
                matrix[index][y]=bufor
            bufor=vector[i]
            vector[i]=vector[index]
            vector[index]=bufor
        mult = matrix[i][i]
        for j in range(number):
            matrix[i][j] /= mult
        vector[i] /= mult
        index = i
        for x in range(number):
            if index != x:
                mult = matrix[x][i]
                vector[x] -= vector[i]*mult
                for j in range(number):
                    matrix[x][j]-= matrix[i][j]*mult

def main():
    # Equation_size = int(input(text_size_of_equation))
    matrix = [[3, -1, 2, -1], [3, -1, 1, 1], [1, 2, -1, 2], [-1, 1, -2, -3]]
    vector = [-13, 1, 21, -5]
    jordanElimination(matrix, vector)
    print("Już")

if __name__ == '__main__':
    main()
"""
TO DO:
1.Sprawdzanie czy uklad jest sprzeczny lub nieoznaczony
2.Czytanie z pliku
3.Napisanie raportu
4.Jeszcze raz wszystko przetestować
"""