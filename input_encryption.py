import numbers_encryption
import symbols_encryption
import cyclic_shift_encryption

import random


def in_file(ifst):
    key = int(ifst.readline())
    if key == 1:
        sp = cyclic_shift_encryption.CyclicShiftEncryption(ifst)
        sp.print_source_string()
        return sp
    elif key == 2:
        sp = numbers_encryption.NumbersEncryption(ifst)
        sp.print_source_string()
        return sp
    elif key == 3:
        sp = symbols_encryption.SymbolsEncryption(ifst)
        sp.print_source_string()
        return sp
    print("Invalid input encryption type.")
    exit(-1)

    # Случайный ввод обобщенной фигуры


def in_rnd():
    k = random.randint(1, 3)
    if k == 1:
        sp = cyclic_shift_encryption.CyclicShiftEncryption()
        return sp
    elif k == 2:
        sp = numbers_encryption.NumbersEncryption()
        return sp
    elif k == 3:
        sp = symbols_encryption.SymbolsEncryption()
        return sp
