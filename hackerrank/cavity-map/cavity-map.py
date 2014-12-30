def find_cavities(ar,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            el = ar[i][j]
            top = ar[i-1][j]
            bottom = ar[i+1][j]
            left = ar[i][j-1]
            right = ar[i][j+1]
            if el > top and el > bottom and el > right and el > left:
                ar[i][j] = 'X'
    for row in ar:
        print "".join(map(str,row))
    return

n = input()
ar = []

for i in range(n):
    ar.append(map(int,list(raw_input())))
find_cavities(ar,n)