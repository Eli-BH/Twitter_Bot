import tweepy
import time
from sys import argv
from private_keys import keys


auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])
api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print('Rate limit Exceeded')
            time.sleep(30)
            continue
        except StopIteration:
            break


# check follower amount function


def check_followers():
    for follower in limit_handle(tweepy.Cursor(api.followers).items()):
        if follower:
            print(follower.name)
        else:
            print('no followers found')


#  like a tweet with the search query word
def auto_like(query, limit):
    for tweet in limit_handle(tweepy.Cursor(api.search, query).items(limit)):
        try:
            tweet.favorite()
            tweet.retweet()
            api.create_friendship(tweet.user.id)

            print('Liked the tweet')
            time.sleep(1000)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            pass


# follows anyone that follow my account
def follow_followers():
    for follower in limit_handle(tweepy.Cursor(api.followers).items()):
        follower.follow()


#  unfollows anyone that is not following me
def unfollow_nonfollowers():
    following_me = []
    friends = []
    for follower in limit_handle(tweepy.Cursor(api.followers).items()):
        following_me.append(follower.screen_name)

    for friend in limit_handle(tweepy.Cursor(api.friends).items()):
        friends.append(friend.screen_name)

    for friend in friends:
        if friend not in following_me:
            api.destroy_friendship(friend)


if __name__ == '__main__':
    auto_like()
