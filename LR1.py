#Лабораторная 2
print("Вариант 1")
print()
import random

print("Задание 1: Удаляем все повторяющиеся числа в массиве")
print()
spisok = [random.randrange(1,10) for i in range(20)]

print("Первоначальный список = ", spisok)
NewSpisok = list(set(spisok))                     #преобразуем в множество и уже готовое множество в список
print()
print("Новый список = ", NewSpisok)

print()
print("Задание 2: Находим подмножество чисел")
print()
test = int(input("Задайте необходимое вам число: "))
print()

spisok.sort(reverse=True)
result = []
i = 0
while test>0 or test!=0:
    if test<min(spisok):
        break
    if spisok[i]>test:
        i+=1
        continue
    else:
        test-=spisok[i]
        result.append(spisok[i])
        i+=1
if test!=0:
    print("Множество не найдено")
else:
    print("Множество из чисел равно : ", result)
print()
print("Вариант 2")
print()
print("Задание 1")
spisok2= [random.randrange(1,10) for i in range(10)]

spisok2.sort(reverse=True)
print(spisok2)
for q in range(len(spisok2)):
    if spisok2[q]%2!=0:
        print("Максимальный нечётный элемент равен = ", spisok2[q])
        break
print()

print("Задание 2")

spisok2.sort()
print(spisok2)
for e in range(len(spisok2)):
    if(abs(spisok2[e])==spisok2[e]):
        print("минимальный по модулю элемент равен",abs(spisok2[e]))
        break

print()

print("Вариант 3")
print()
print("Задание 1")
print()
negativeSpisok = [random.randrange(-10,10) for i in range(20)]
tempCounter = 0
for r in range(len(negativeSpisok)):
    if negativeSpisok[r]<0:
        tempCounter+=negativeSpisok[r]
print("Сумма отрицательных элементов равна = ",tempCounter)
print()
print("Задание 2")
print()
zeroSpisok = [0,1,1,1,1,1,0,35,22,12,32,32]
zeroCounter = 0
resultZero = 0
spisokIndex = 0
for i in range(len(zeroSpisok)):
    if zeroSpisok[i]==0:
        counterZero = i
        break
while(zeroSpisok[counterZero+1]!=0):
    resultZero+=zeroSpisok[counterZero+1]
    counterZero+=1
print(resultZero)       #Должно получиться 5

print()
print("Вариант 4")
print()
print("Задание 1")
print()

