# ------------------------------------------------------------------------------
# Encryption.py - содержит процедуры связанные с шифрованием поступившей строки
# ------------------------------------------------------------------------------

# структура, обобщающая все имеющиеся фигуры
class Encryption:
    def __init__(self):
        self.source_string = ""
        self.size = 0

    def get_source_string(self):
        return self.source_string

    def set_source_string(self, value):
        self.source_string = value

    # Частное от деления суммы кодов незашифрованной строки на число символов в этой строке
    def quotient_of_division(self):
        char_sum = 0
        i = 0
        if self.size < len(self.get_source_string()):
            size = self.size
        else:
            size = len(self.get_source_string())
        while i < size:
            char_sum += ord(self.get_source_string()[i])
            i += 1
        if self.size == 0:
            return 0
        return char_sum / self.size

    # Вывод исходной строки, результата общей функции и зашифрованной строки в поток
    def out_current_string(self, encryption, ofst):
        encryption.out(ofst)

    # Выводи исходной строки в консоль
    def print_source_string(self):
        print("String \"", end='')
        i = 0
        if self.size < len(self.get_source_string()):
            size = self.size
        else:
            size = len(self.get_source_string())
        while i < size:
            print(self.get_source_string()[i], end='')
            i += 1
        print("\" was encrypted.", end='')
        print("\n", end='')
