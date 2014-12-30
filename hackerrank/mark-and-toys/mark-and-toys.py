def partition(ar,start,end):
    piv = ar[end]
    swap_pos = start
    for i in range(start,end):
        if ar[i] < piv:
            ar[i],ar[swap_pos] = ar[swap_pos],ar[i]
            swap_pos += 1
    ar[end],ar[swap_pos] = ar[swap_pos],ar[end]
    return swap_pos

def sort_prices(ar,start,end):
    if start >= end:
        return 
    piv_idx = partition(ar,start,end)
    sort_prices(ar,start,piv_idx -1)
    sort_prices(ar,piv_idx + 1, end)

def max_toys(prices, k,n):
    sort_prices(prices,0,n-1)
    total = 0
    answer = 0
    for p in prices:
        total += p
        if total <= k:
            answer += 1
        else:
            break
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k,n)
