#Лабораторная 2
import random

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
nechetSpisok = [random.randrange(1,10) for i in range(10)]
print(nechetSpisok)
resNechet = 1
for i in range(1,len(nechetSpisok),2):
    resNechet*=nechetSpisok[i]
print(resNechet)
print()
print("Задание 2")
maxSpisok = [random.randrange(1,100) for i in range(10)]
print(maxSpisok)
maxSpisok.remove(max(maxSpisok))
print(maxSpisok)

print("Вариант 5")
print()
print("Задание 1")
chetElement = [random.randrange(1,100) for i in range(10)]
minChet = 0
for i in range(0,len(chetElement),2):
    if(minChet==0):
        minChet=chetElement[i]
    elif(minChet>chetElement[i]):
        minChet=chetElement[i]
print(minChet)



print("Задание 2")
zeroElements = [0,0,12,3,4,5,1,0,1,0,2,3,4,51,24,0]
chechkZero = 0
for i in range(len(zeroElements)):
    if(zeroElements[i]==0):
        zeroElements[i],zeroElements[chechkZero]=zeroElements[chechkZero],zeroElements[i]
        chechkZero+=1
print(zeroElements)

print("Вариант 6")
print("Задание 1")

delspis = [random.randrange(1,10) for i  in range(10)]
deltest = int(input("Задайтие чеисло множество которого в сумме должно делиться на него: "))
delspis.sort(reverse=True)
delResSpis = []
delcounter = 0
while delcounter<len(delspis):
    if deltest>delspis[delcounter]:
        delResSpis.append(delspis[delcounter])
        delcounter+=1
    else:
        delcounter+=1
delResSpis.sort()
leftPoint = 0
rightPoint = len(delResSpis)
while leftPoint<rightPoint:
    testDelSpis = delResSpis[leftPoint:rightPoint]
    if (sum(testDelSpis)>deltest):
        rightPoint-=1
    else:
        if(sum(testDelSpis)%deltest==0):
            print(testDelSpis)
            break
        else:
            for i in range(0,len(testDelSpis)):
                if((sum(testDelSpis)-testDelSpis[i])%deltest==0):
                    print(sum(testDelSpis)-testDelSpis[i]) #Ну либо принтим список но без этого числа
                    break
                else:
                    leftPoint+=1
if(leftPoint==rightPoint):
    print(testDelSpis)
    print("Такого множества не нашли")

print("Задание 2")
print("Задание 2.1")
testMatrix = [[random.randrange(1,100) for i in range(10)] for p in range(10)]
testRes = 0
for a in range(len(testMatrix)):
    if sum(testMatrix[a])>testRes:
        testRes = a
print(testRes)

print("Задание 2.2")

simMatrix = [[1,2,3],
             [2,1,3],
             [3,3,1]]
nonSimMatrix = [[4,2,5],
                [6,1,4],
                [2,8,0]]

def testSim(testMatrix):
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            if testMatrix[i][j] == testMatrix[j][i]:
                continue
            else:
                print("Матрица не симметрична")
                return False
    print("Матрица симметрична")
    return True
testSim(simMatrix)
testSim(nonSimMatrix)

print("Задание 3")

testSumMatrix1 = [[random.randrange(1,100) for d in range(10)] for s in range(10)]
testSumMatrix2 = [[random.randrange(1,100) for f in range(10)] for g in range(10)]

resTestSumMatrix = [[0 for k in range(10)] for l in range(10)]

for i in range(len(resTestSumMatrix)):
    for j in range(len(resTestSumMatrix[i])):
        resTestSumMatrix[i][j] = testSumMatrix1[i][j]+testSumMatrix2[i][j]
for i in resTestSumMatrix:
    print(i)

