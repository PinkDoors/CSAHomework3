import input_encryption
from sys import getsizeof

# ------------------------------------------------------------------------------
# container.py - содержит тип данных,
# представляющий простейший контейнер
# ------------------------------------------------------------------------------

class Container:

    def __init__(self):
        # Массив строк.
        self.cont = []

    # Ввод содержимого контейнера из указанного потока
    def in_file(self, ifst):
        number_of_elements = int(ifst.readline())
        if number_of_elements > 10000 or number_of_elements < 0:
            print("Incorrect number of strings", end='')
            print("\n", end='')
            return
        i = 0
        while i < number_of_elements:
            self.cont.append(input_encryption.in_file(ifst))
            i += 1

    # Случайный ввод содержимого контейнера
    def in_rnd(self, size):
        i = 0
        while i < size:
            self.cont.append(input_encryption.in_rnd())
            i += 1

    # Вывод содержимого контейнера в указанный поток
    def out(self, ofst):
        ofst.write("Container contains ")
        ofst.write(str(len(self.cont)))
        ofst.write(" elements.\n")
        i = 0
        while i < len(self.cont):
            ofst.write("----------------------------------------------------\n")
            ofst.write(str(i))
            ofst.write(": ")
            self.cont[i].out(ofst)
            i += 1

    def heapify(self, arr, n, i):
        # Инициализируем наименьший элемент как корень.
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left].quotient_of_division() < arr[smallest].quotient_of_division():
            smallest = left
        if right < n and arr[right].quotient_of_division() < arr[smallest].quotient_of_division():
            smallest = right

        # Если самый маленький элемент не является корнем, то меняем местами.
        if smallest != i:
            smallest_element = arr[smallest]
            arr[smallest] = arr[i]
            arr[i] = smallest_element
            # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
            self.heapify(arr, n, smallest)

    # Сортировка элементов контейнера по убыванию с помощью "дерева"
    def heap_sort(self):
        # Построение кучи (перегруппируем массив)
        for i in range(int(len(self.cont) / 2) - 1, -1, -1):
            self.heapify(self.cont, len(self.cont), i)
        # Один за другим извлекаем элементы из кучи.
        for j in range(len(self.cont) - 1, -1, -1):
            last = self.cont[j]
            self.cont[j] = self.cont[0]
            self.cont[0] = last
            # вызываем процедуру Heapify на уменьшенной куче.
            self.heapify(self.cont, j, 0)
