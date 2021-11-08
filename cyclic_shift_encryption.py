import encryption
# ------------------------------------------------------------------------------
# cyclic_shift_encryption.py - содержит реализацию строки, зашифрованной циклическим сдвигом кода каждого символа на n.
# ------------------------------------------------------------------------------

import random


# Строка, зашифрованная циклическим сдвигом кода каждого символа
class CyclicShiftEncryption(encryption.Encryption):

    def __init__(self, ifst=None):
        encryption.Encryption.__init__(self)
        self.encrypted_string = ""
        self.shift = 0
        self.size = 0
        if ifst is None:
            self.random_constructor()
        else:
            self.file_constructor(ifst)

    # Инициализация и шифрование случайными данными
    def random_constructor(self):
        self.encrypted_string = ""
        self.shift = 0
        self.size = random.randint(0, 256)
        alphanum = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
        i = 0
        while i < self.size:
            symbol = random.randint(0, 61)
            self.set_source_string(self.get_source_string()[:i] +
                alphanum[symbol] + self.get_source_string()[i + 1:])
            i += 1
        self.shift = random.randint(0, 999)
        i = 0
        while i < self.size:
            self.encrypted_string = self.encrypted_string[:i] + chr(
                ord(self.get_source_string()[i]) + self.shift) + self.encrypted_string[i + 1:]
            i += 1

    # Инициализация и шифрование данными из файла
    def file_constructor(self, ifst):
        self.encrypted_string = ""
        input_string = ifst.readline().split()
        self.size = int(input_string[0])
        if self.size > 256 or self.size < 0:
            print("Incorrect size of the input string, the size is set to 0")
            self.size = 0
        self.set_source_string(input_string[1])
        self.shift = int(ifst.readline())
        i = 0
        while i < self.size:
            self.encrypted_string = self.encrypted_string[:i] + chr(
                ord(self.get_source_string()[i]) + self.shift) + self.encrypted_string[i + 1:]
            i += 1

    # Вывод зашифрованной строки
    def out(self, ofst):
        ofst.write("Input string = ")
        i = 0
        while i < self.size:
            ofst.write(self.get_source_string()[i])
            i += 1
        ofst.write(".\n\n")
        ofst.write("The quotient of dividing the sum of "
                   + "the codes of an unencrypted "
                   + "string by the number of characters in "
                   + "this string = ")
        ofst.write(str(self.quotient_of_division()))
        ofst.write(".\n\n")
        ofst.write("Result of the encryption: ")
        i = 0
        ofst.write(self.encrypted_string)
        ofst.write(".\n")
