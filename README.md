# NumericalMethodsEx2
Metoda eliminacji Jordana to jedna z metod rozwiązywania układów równań liniowych. Polega na wykorzystaniu operacji elementarnych na macierzy współczynników, aby sprowadzić ją do postaci diagonalnej.

Kroki metody eliminacji Jordana są następujące:

Zapisz układ równań liniowych w postaci macierzowej Ax = b, gdzie A to macierz współczynników, x to wektor zmiennych i b to wektor wyrazów wolnych.
Dołącz do macierzy A wektor b, aby uzyskać macierz rozszerzoną [A|b].
Przeprowadź operacje elementarne na macierzy rozszerzonej, aby uzyskać macierz górną trójkątną. Można to zrobić poprzez wykonywanie następujących kroków:

a. Wybierz element główny w pierwszym wierszu i pierwszej kolumnie.
b. Wykonaj operacje elementarne na wierszach macierzy, aby wyzerować wszystkie elementy pod elementem głównym w pierwszej kolumnie.
c. Powtarzaj krok a i b dla kolejnych kolumn, aż uzyskasz macierz górną trójkątną.

Wykonaj kolejne operacje elementarne na macierzy górnym trójkątną, aby uzyskać macierz diagonalną. Można to zrobić poprzez wykonywanie następujących kroków:

a. Dla każdego elementu diagonalnego, wykonaj operacje elementarną, aby wyzerować wszystkie elementy nad nim.
b. Powtarzaj krok a dla kolejnych elementów diagonalnych, aż uzyskasz macierz diagonalną.

Odczytaj rozwiązanie układu równań z macierzy diagonalnej.
Metoda eliminacji Jordana jest skutecznym sposobem na rozwiązanie układów równań liniowych, ale może być czasochłonna, zwłaszcza dla dużych macierzy.

Rozważmy następujący układ równań:

  2x - y + z = 5
  4x + 4y - 3z = 3
  2x + 5y - 4z = 6

Możemy zapisać ten układ równań w postaci macierzowej:

  [2 -1 1 | 5]
  [4 4 -3 | 3]
  [2 5 -4 | 6]

Aby rozwiązać ten układ równań metodą eliminacji Jordana, wykonujemy następujące kroki:

Dołączamy wektor wyrazów wolnych do macierzy A, aby uzyskać macierz rozszerzoną:

  [2 -1 1 | 5]
  [4 4 -3 | 3]
  [2 5 -4 | 6]

Wykonujemy operacje elementarne na macierzy rozszerzonej, aby uzyskać macierz górną trójkątną:

  [2 -1 1 | 5]
  [0 6 -7 | -7]
  [0 0 -5 | -2]

Wykonujemy kolejne operacje elementarne na macierzy górnej trójkątnej, aby uzyskać macierz diagonalną:

  [2 0 0 | 1]
  [0 6 0 | 1]
  [0 0 1 | 0.4]

Odczytujemy rozwiązanie układu równań z macierzy diagonalnej: x=1, y=1/6, z=0.4.

Zatem rozwiązanie naszego układu równań to x=1, y=1/6, z=0.4.
