#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    stroka1 = input("Введите первую строку: ")
    stroka2 = input("Введите вторую строку: ")

    one = set(stroka1)
    two = set(stroka2)

    a = one.intersection(two)
    print("Общие символы двух строк: ", a)
    