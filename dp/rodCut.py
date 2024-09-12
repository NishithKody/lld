from sys import stdin
import sys

def cutRod(price, n):

    def util(i,N):

        if(i==0):
            return N*price[0]

        dsel = 0 +  util(i-1, N)
        sel = -float('inf')
        rodLen = i + 1
        if(rodLen <=N):
            sel = util(i,N-rodLen) + price[i]
        return max(dsel,sel)

    res = util(len(price)-1, n)
    return res

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
