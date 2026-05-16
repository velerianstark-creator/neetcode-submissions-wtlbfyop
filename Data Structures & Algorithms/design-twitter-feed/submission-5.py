from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        self.tweets = dict()
        self.heap = []
        self.followers = dict()
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        heappush(self.heap, - self.timestamp)
        
        self.tweets[-self.timestamp] = [userId, tweetId]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        heap = self.heap.copy()
        while len(output) < 10 and heap:
            timestamp = heappop(heap)
            tweet = self.tweets[timestamp]
            if (tweet[0] == userId or tweet[0] in self.followers.get(userId, [])):
                output.append(tweet[1])
        return output
            

    def follow(self, followerId: int, followeeId: int) -> None:
        lst = self.followers.setdefault(followerId, [])
        if followeeId not in lst:
            lst.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for user in self.followers.get(followerId, []):
            self.followers[followerId].remove(followeeId)
