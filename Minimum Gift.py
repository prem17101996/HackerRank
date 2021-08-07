for i in range(int(input())):
    n=int(input())
    rank=list(map(int,(input().split())))
    rank1=1
    ra=1
    for i in range(n-1):

        if rank[i+1]>rank[i]:
            rank1+=1
            ra=ra+rank1
        else:

            rank1=1
            ra = ra + rank1
    print(ra)