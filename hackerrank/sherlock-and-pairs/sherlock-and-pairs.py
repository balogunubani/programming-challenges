"""
@author Ubani Anthony Balogun
@date 12/30/2014
"""
def sherlock_pairs(ar,n):
    counts = {}
    total = 0
    for a in ar:
        if a not in counts:
            counts[a] = 1
        else:
            counts[a] += 1
    for a in counts:
        total += counts[a] * (counts[a] -1)
    return total


T = input()

for i in range(T):
    n = input()
    ar = map(int,raw_input().split())
    print sherlock_pairs(ar,n)