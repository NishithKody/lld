from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)  # Maps user to the set of users they follow
        self.tweets = defaultdict(list)    # Maps user to their list of tweets
        self.timestamp = 0                 # Global timestamp for ordering tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1  # Decrease timestamp to prioritize recent tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.followers[userId].add(userId)  # Include user's own tweets

        # Collect recent tweets from the user and their followees
        for followee in self.followers[userId]:
            for ts, tid in self.tweets[followee][-10:]:
                heapq.heappush(heap, (ts, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)

        # Extract tweets from heap and reverse to get most recent first
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
