from collections import defaultdict

class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1
        
    # 10 most recent tweets in user's feed
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        heap += self.tweets[userId]

        for user in self.following[userId]:
            heap += self.tweets[user]
        
        heapq.heapify(heap)

        if not heap:
            return []

        res = []
        for i in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]: 
            self.following[followerId].remove(followeeId)
        
