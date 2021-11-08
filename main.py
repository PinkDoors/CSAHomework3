from sys import argv
import container

# ------------------------------------------------------------------------------
# main.py - содержит главную функцию,
# обеспечивающую простое тестирование
# ------------------------------------------------------------------------------

import time


def err_message_1():
    print("incorrect command line!")
    print("  Waited:")
    print("     command -f infile outfile01 outfile02")
    print("  Or:")
    print("     command -n number outfile01 outfile02")


def err_message_2():
    print("incorrect qualifier value!")
    print("  Waited:")
    print("     command -f infile outfile01 outfile02")
    print("  Or:")
    print("     command -n number outfile01 outfile02")


if len(argv) != 5:
    err_message_1()
    exit(1)

print("Start of the program")
start_time = time.time()
c = container.Container()

# Ввод содержимого из потока (файл).
if argv[1] == "-f":
    ifst = open(argv[2])
    c.in_file(ifst)

# Ввод случайных элементов.
elif argv[1] == "-n":
    size = int(argv[2])
    if (size < 1) or (size > 10000):
        print("Incorrect numer of figures = ", end='')
        print(size, end='')
        print(". Set 0 < number <= 10000")
        exit(3)
    # Заполнение контейнера генератором случайных чисел
    c.in_rnd(size)
else:
    err_message_2()
    exit(2)

# Вывод содержимого контейнера в файл.
ofst1 = open(argv[3], 'w', encoding="utf8")
ofst1.write("Filled container:\n")
c.out(ofst1)
print('The container is saved to a file \"', end='')
print(argv[3], end='')
print("\"")

# Вывод отсортированного содержимого контейнера в файл.
c.heap_sort()
ofst2 = open(argv[4], 'w',encoding="utf8")
ofst2.write("Sorted container:\n")
c.out(ofst2)
print("The sorted container is saved to a file \"", end='')
print(argv[4], end='')
print("\"")

print("The program ended successfully")
print("Time: ", end='')
print(time.time() - start_time, end='')
print("\n", end='')
