class Twitter:
    """
    - use a hashmap to store following
        - each key is a userId, and each value is a list of following
        - but we want to manipulate the list of following efficiently, so we can use a hashset to add and remove in constant time
    - use a hashmap to store tweets
        - the keys are userIds, and the values are the list of tweets by the user
        - we need a way to compare which tweets were more recent across mulitple users
            - so tweets will be stored as a pair, containing the tweetId and a timestamp, which can just be a counter that increments each time anyone posts a tweet
    - use a max heap to compile the most recent tweets in a user's feed
        - how get the 10 most recent tweets across multiple users?
            - use merge k sorted lists alg, starting with the most recent of each user
            - that way we can stop when we get to 10 so were not doing extra work
    """

    """
    Initializes twitter object
    """
    def __init__(self):
        self.tweetCount = 0 # count will actually go negative since were using a min heap in python, and thus want to prioritize the lowest (most recent) value
        self.followingMap = {} # a hashmap of hashsets (could also use a dictionary for less code such as the tweetMap)
        self.tweetMap = defaultdict(list) # a dictionary of lists, to store user tweets in order

    """
    - given: tweet id and userId
    - creates a new tweet
    """
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [self.tweetCount, tweetId] # construct the tweet with the current counter
        self.tweetMap[userId].append(tweet)
        self.tweetCount -= 1 # using negative counts for min heap

    """
    - given: a userId
    - returns: the 10 most recent tweets in the user's feed (tweets by users the user follows, or the user themself)
    """
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [] # 10 most recent tweets
        tweetHeap = []

        # insert the most recent tweet from each following into a heap
        if not userId in self.followingMap: # initially, each user in the hashmap must be initialized to an empty set
            self.followingMap[userId] = set()
            self.followingMap[userId].add(userId) # users are technically following themselves when it comes to their feed
        for user in self.followingMap[userId]:
            if user in self.tweetMap: # if the user has any tweets
                tweetPointer = len(self.tweetMap[user]) - 1 # grab the user's latest tweet, and keep a pointer to iterate to older tweets
                tweet = self.tweetMap[user][tweetPointer] # get the tweet
                tweetPos = tweet[0]
                tweetId = tweet[1]
                tweetInfo = [tweetPos, tweetId, user, tweetPointer - 1] # construct the tweet info for the heap
                heapq.heappush(tweetHeap, tweetInfo) # toss it in the heap
        
        # to get the most recent tweet: pop it, then push the next most recent of that user to the heap. repeat 10 times
        while tweetHeap and len(feed) < 10:
            nextLatestTweet = heapq.heappop(tweetHeap)
            feed.append(nextLatestTweet[1])
            # put the next recent tweet from the user into the heap
            user = nextLatestTweet[2]
            ptr = nextLatestTweet[3]
            if ptr >= 0:
                tweet = self.tweetMap[user][ptr]
                tweetPos = tweet[0]
                tweetId = tweet[1]
                tweetInfo = [tweetPos, tweetId, user, ptr - 1]
                heapq.heappush(tweetHeap, tweetInfo)

        return feed
    """
    - given: 2 userIds
    - add the followee to the follower's following list
    """
    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followingMap: # initially, each user in the hashmap must be initialized to an empty set
            self.followingMap[followerId] = set()
            self.followingMap[followerId].add(followerId) # users are technically following themselves when it comes to their feed
        self.followingMap[followerId].add(followeeId)
    """
    - given: 2 userIds
    - remove the followee from the follower's following list
    """
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followingMap and followeeId in self.followingMap[followerId]: # check that they're currently following this person
            self.followingMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)