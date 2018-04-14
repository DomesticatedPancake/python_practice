import numpy as np
import csv
import os


resultg = []
first = []
second = []
torzs1 = []
z = []


# megniytja a fájlt
def openfile(filepath, torzs):
    global result1
    global max_length
    f = open(filepath, 'r')
    lines = f.readlines()
    result=[]
    for x in lines:
        if x.split('\t')[0].rstrip() == torzs:
            result.append(float(x.split('\t')[2].rstrip()))
    result1 = np.array(result)
    max_length = len(result1)

#minden xdik sort áltagolja
def average(result1, n):
    global new
    end = n * int(len(result1) / n)
    if len(result1) % n != 0:
        plus = sum(result1[end:(len(result1) - 1)]) / (len(result1)-end)
        osszeg = np.mean(result1[:end].reshape(-1, n), 1)
        new = osszeg.tolist()
        new.append(plus)
    else:
        plus = sum(result1[end:(len(result1) - 1)]) / (len(result1))
        osszeg = np.mean(result1[:end].reshape(-1, n), 1)
        new = osszeg.tolist()
        new.append(plus)
    print(n)

#kiszámítja a logokat
def logs(new):
    global resultg
    for i in new:
        if i >= 1:
            resultg.append(np.log10(i))
        else:
            resultg.append(0)
    print(n)


#megcsinálja az oszlopokat
def makescolumns(max_length, n, torzs):
    global first, second
    for a in range(1, max_length, n):
        if a + n > max_length:
            first.append(a)
            second.append(max_length)
        else:
            first.append(a)
    for b in range(n, max_length, n):
        second.append(b)
    for t in range(int(max_length/n + 1)):
        torzs1.append(torzs)
    second = second[1:] + [second[0]]
    print(n)

#végül fájlt kreál
def plswork(dir_name, remember):
    file_name = strain + '_' + str(n) + '_' + remember + '.txt'
    with open(os.path.join(dir_name, file_name), 'w', newline = '') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerows(zip(torzs1, first, second, resultg))
    print(n)



filepath = str(input('Where is the file? ' ))
k = input('What averages? ')
z = [int(i) for i in k.split()]
strain = str(input('Hows the strain called? '))
dir_name = str(input('Where to save? '))
remember = str(input('How do you remember? '))

for n in z:
    openfile(filepath, strain)
    average(result1, n)
    logs(new)
    makescolumns(max_length, n, strain)
    plswork(dir_name, remember)
    print (n*2)