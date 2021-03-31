try:
    n=int(input('Для какого числа крутим спираль?\n'))
    print()
    num=1
    i,j=0,0
    start=n
    end=n**2
    matrix=[[0]*n for x in range(n)]
    while (num<=end):
        for j in range(j,n):
                matrix[i][j]=num
                num+=1
                # print (f'el={matrix[i][j]} {i} {j} num={num} n={n}')
        for i in range (i+1,n):
                matrix[i][j]=num
                num+=1
                # print (f'el={matrix[i][j]} {i} {j} num={num} n={n}')
        for j in range (j-1,start-n-1,-1):
                matrix[i][j]=num
                num+=1
                # print (f'el={matrix[i][j]} {i} {j} num={num} n={n}')
        for i in range (i-1, start-n, -1):
                matrix[i][j]=num
                num+=1
                # print (f'el={matrix[i][j]} {i} {j} num={num} n={n}')
        n-=1
        j+=1
    for row in range(0,start):
        for column in range (0,start):
            print (f'{matrix[row][column]:<3} ', end='')
        print()
except ValueError:
    print ('Неверное значение, нужно целое число')
except IndexError:
    print('Почему-то мы выпали из массива')
except SyntaxError:
    print('Синтаксис сломался, всё пропало')
