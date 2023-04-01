def jordanElimination(matrix: List[List[float]], vector: List[float]):
    number = len(matrix)
    zeroes = [0] * number
    for i in range(number):
        copy = []
        cvector = round(vector[i], 8)
        for c in range(number):  # robimy kopię macierzy
            copy.append(round(matrix[i][c], 8))
        if copy == zeroes:  # Sprawdzamy czy układ jest sprzeczy lub nieoznaczony
            if cvector == 0:
                print("Układ nieoznaczony")
            else:
                print("Układ sprzeczny")
            return
        # Zabezpieczenie gdyby mnożnik przy zmiennej którą chcemy obliczyć wynosił zero
        if matrix[i][i] == 0:
            maks = 0
            index = i
            bufor: float
            for x in range(number - i):  # Sprawdzamy gdzie na pozostałych wierszach jest największa liczba
                if abs(matrix[i + x][i]) > maks:
                    maks = matrix[i + x][i]
                    index = i + x
            for y in range(number):  # Zamiana miejscamy wierszy
                bufor = matrix[i][y]
                matrix[i][y] = matrix[index][y]
                matrix[index][y] = bufor
            bufor = vector[i]
            vector[i] = vector[index]
            vector[index] = bufor
        mult = matrix[i][i]
        for j in range(number):  # dzielimy cały wiersz przez badana
            matrix[i][j] /= mult
        vector[i] /= mult
        index = i
        for x in range(number):  # Odejmujemy od reszty wierszy badany wiersz w celu wyzerowania badanej komórki
            if index != x:
                mult = matrix[x][i]
                vector[x] -= vector[i] * mult
                for j in range(number):
                    matrix[x][j] -= matrix[i][j] * mult
    return vector
