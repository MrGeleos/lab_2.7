#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    stroka = input("Введите строку: ").lower()
    s = set(stroka)
    l = set("аоуыэеёиюяaeiouy")

    count = 0
    for i in stroka:
        if i in l:
            count += 1

    print(count)