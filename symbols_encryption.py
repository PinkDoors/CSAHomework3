import encryption

# ------------------------------------------------------------------------------
# symbols_encryption.py - содержит реализацию строки, зашифрованной заменой символов на другие символы.
# ------------------------------------------------------------------------------

import random


# Строка, зашифрованная заменой символов
class SymbolsEncryption(encryption.Encryption):

    # Инициализация и шифрование случайными данными
    def __init__(self, ifst=None):
        encryption.Encryption.__init__(self)
        self.encrypted_string = ""
        self.symbols = []
        self.init()
        if ifst == None:
            self.random_constructor()
        else:
            self.file_encrypt(ifst)

    # Инициализация и шифрование данными из файла
    def file_encrypt(self, ifst):
        input_string = ifst.readline().split()
        self.size = int(input_string[0])
        if self.size > 256 or self.size < 0:
            print("Incorrect size of the input string, the size is set to 0")
            self.size = 0
        if self.size > 0:
            self.set_source_string(input_string[1])
        self.encrypt(ifst)

    # Шифрование случайными данными
    def random_constructor(self):
        alphanum = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
        self.size = random.randint(0, 256)
        i = 0
        while i < self.size:
            symbol = random.randint(0, 61)
            self.set_source_string(self.get_source_string()[:i] +
                                   alphanum[symbol] + self.get_source_string()[i + 1:])
            i += 1
        for i in range(0, 62):
            symbol = random.randint(0, 61)
            self.symbols[i][1] = alphanum[symbol]
        i = 0
        while i < self.size:
            for j in range(0, 62):
                if self.get_source_string()[i] == self.symbols[j][0]:
                    self.encrypted_string = self.encrypted_string[:i] + str(self.symbols[j][1]) + self.encrypted_string[
                                                                                                  i + 1:]
            i += 1

    # Шифрование данными из файла
    def encrypt(self, ifst):
        number_of_symbols = int(ifst.readline())
        i = 0
        while i < number_of_symbols:
            input_symbols = ifst.readline().split()
            old_symbol = input_symbols[0]
            new_symbol = input_symbols[1]
            for j in range(0, 62):
                if self.symbols[j][0] == old_symbol:
                    self.symbols[j][1] = new_symbol
            i += 1
        i = 0
        if self.size < len(self.get_source_string()):
            size = self.size
        else:
            size = len(self.get_source_string())
        while i < size:
            for j in range(0, 62):
                if self.get_source_string()[i] == self.symbols[j][0]:
                    self.encrypted_string = self.encrypted_string[:i] + str(self.symbols[j][1]) + self.encrypted_string[
                                                                                                  i + 1:]
            i += 1

    # Инициализация массива пар [символ, символ]
    def init(self):
        number_of_symbol = 0
        for i in range(0, 10):
            self.symbols.append([chr(i + 48), chr(i + 48)])
            number_of_symbol += 1
        for i in range(17, 43):
            self.symbols.append([chr(i + 48), chr(i + 48)])
            number_of_symbol += 1
        for i in range(49, 75):
            self.symbols.append([chr(i + 48), chr(i + 48)])
            number_of_symbol += 1

    # Вывод зашифрованной строки.
    def out(self, ofst):
        ofst.write("Input string = ")
        i = 0
        if self.size < len(self.get_source_string()):
            size = self.size
        else:
            size = len(self.get_source_string())
        while i < size:
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
        if self.size < len(self.encrypted_string):
            size = self.size
        else:
            size = len(self.encrypted_string)
        while i < size:
            ofst.write(self.encrypted_string[i])
            i += 1
        ofst.write(".\n")
