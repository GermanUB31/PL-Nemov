m=int(input('строк: '))
n=int(input('столбцов: '))
A=[]
B=[]
for i in range(m):
    b=[]
    for j in range(n):
        b.append(float(input('элемент :')))
    A.append(b)
print('матрица до изменения, добавленная в файл')
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
f=open('НемовГерманАнтонович_УБ31_VVOD.txt','w')
for i in A:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write('\n')
f.close()
data=[]
with open('НемовГерманАнтонович_УБ31_VVOD.txt','r') as f:
    for line in f:
        data.append([float(x) for x in line.split()])
f.close
for p in data:
    B.append(sorted(p))
print('матрица после изменения, добавленная в файл')
for i in range(m):
    for j in range(n):
        print(B[i][j], end=' ')
    print()
f=open('НемовГерманАнтонович_УБ31_VIVOD.txt','w')
for i in B:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write('\n')
f.close()
