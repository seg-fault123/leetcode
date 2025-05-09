import heapq
class Twitter:

    def __init__(self):
        self.num_tweets = 0
        self.user_tweets = {}
        self.user_following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.num_tweets -= 1
        if userId in self.user_tweets:
            self.user_tweets[userId].append((self.num_tweets, tweetId))
        else:
            self.user_tweets[userId] = [(self.num_tweets, tweetId)]
        return


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []+self.user_tweets.get(userId, [])
        following = self.user_following.get(userId, set())
        for user in following:
            heap.extend(self.user_tweets.get(user, []))
        
        heapq.heapify(heap)
        result = []
        for _ in range(10):
            if not heap:
                break
            result.append(heapq.heappop(heap)[-1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_following:
            self.user_following[followerId].add(followeeId)
        else:
            self.user_following[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.user_following.get(followerId, set())
        if followeeId in following:
            following.remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
