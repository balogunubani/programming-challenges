
def partition(ar,start,end):
    piv = ar[end]
    swap_pos = start
    for i in range(start,end):
        if ar[i] < piv:
            ar[i],ar[swap_pos] = ar[swap_pos],ar[i]
            swap_pos += 1
    ar[end],ar[swap_pos] = ar[swap_pos],ar[end]
    return swap_pos


def find_median(ar,start,end,mid):

    piv_idx = partition(ar,start,end)
    if piv_idx < mid:
        return find_median(ar,piv_idx + 1, end,mid)
    elif piv_idx > mid:
        return find_median(ar,start,piv_idx - 1,mid)
    else:
        return ar[piv_idx]

if __name__ == '__main__':
    n = input()
    ar = map(int,raw_input().split())
    mid = n/2
    print find_median(ar,0,n-1,mid)