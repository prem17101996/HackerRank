

def insertion_sort(l):
    a=l.sort()
    return a

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))