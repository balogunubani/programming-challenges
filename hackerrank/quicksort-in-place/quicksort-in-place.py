def swap(ar,i,j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp
    return 


def partition(ar,start,end):
    piv = ar[end]
    swap_idx = start
    for i in range(start, end):
        if ar[i] < piv:
            swap(ar,swap_idx,i)
            swap_idx += 1
    swap(ar,swap_idx,end)
    return swap_idx

def quickSort(ar,start,end):
    if start >= end:
        return
    piv_idx = partition(ar,start,end)
    print " ".join(map(str,ar))
    quickSort(ar,start,piv_idx - 1)
    quickSort(ar,piv_idx + 1, end)
    

if __name__ == '__main__':
    n = input()
    ar = map(int,raw_input().split())
    quickSort(ar,0,n-1)
    