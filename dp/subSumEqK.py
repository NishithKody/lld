# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.
# For Example :

# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.


from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    def util(i,target):

        if(i<0):
            return False
        if(target==0):
            return True

        dsel = util(i-1, target)
        sel = False
        if(target>=arr[i]):
            sel = util(i-1, target-arr[i])
    
        return sel or dsel
    
    res = util(n-1,k)
    return res

def subsetSumToK(n, k, arr):

    dp = []
    for i in range(n+1):
        val = [False] * (k+1)
        dp.append(val)
    
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1,n+1):
        for j in range(1,k+1):
            sel = False
            
            if(j>=arr[i-1]):
                sel = dp[i-1][j-arr[i-1]]
            dsel = dp[i-1][j]

            dp[i][j] = sel or dsel 
    
    return dp[n][k]

    
    