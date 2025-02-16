from typing import (
    List,
)

from collections import defaultdict
from itertools import combinations
class Solution:
    """
    @param username: An array with username
    @param timestamp: Timestamp of the user's visit to the website
    @param website: Websites visited by users
    @return: Most frequent access behavior
    """
    def most_visited_pattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # write your code here

        users = defaultdict(list)
        n = len(username)
        patternMap = defaultdict(int)

        for i in range(n):
            curUser = username[i]
            curWeb = website[i]
            curTs = timestamp[i]
        
            users[curUser].append([curTs, curWeb])

        for key in users.keys():
            users[key].sort(key=lambda item:item[0])
            sites = []
            for [ts, site] in users[key]:
                sites.append(site)

            patterns = set(combinations(sites,3))
            for pattern in patterns:
                patternMap[pattern] += 1
            
        sortedPattern = sorted(patternMap.items(), key=lambda item:(-item[1], item[0]))
            
        return sortedPattern[0][0]
        