# save api key, api key secret, bearer token, access token, access token secret in a config.py file
# pip install tweepy

# import packages
import tweepy
import config
# create a client
client = tweepy.Client(bearer_token = config.BEARER_TOKEN)
# search
query = 'H1B OR H-1B -is:retweet'

# get the response
# response = client.search_recent_tweets(query = query, max_results = 15, tweet_fields = ['created_at', 'lang'])

# print the tweets
# for tweet in response.data:
#     print(tweet.id)
#     print(tweet.text)
#     print(tweet.created_at)

# get user info
# use the expansion parameter
# https://developer.twitter.com/en/docs/twitter-api/expansions
# response = client.search_recent_tweets(query = query, max_results = 15, tweet_fields = ['created_at', 'lang'],
#                                        expansions = ['author_id'], user_fields = ['profile_image_url'])
#
# users = {u['id']: u for u in response.includes['users']}
#
# for tweet in response.data:
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         print(user.username)
#         #print(user.profile_image_url)
#         print(tweet.text)

# Paginator
# for tweet in tweepy.Paginator(client.search_recent_tweets, query = query, max_results = 15).flatten(limit = 100):
#     print(tweet.text)

# full archive search
# only available to academic account
# ADD the academic bearer token in the config file
# client = tweepy.Client(bearer_token = config.ACADEMIC_BEARER_TOKEN)
#
# query = 'H1B OR H-1B -is:retweet place_country:US'

# use search_all_tweets instead of search_recent_tweets
# can specify the start time and end time
# can filter the place_country if the user has geo information

# start_time = '2022-10-27T23:00:00.000Z'
# end_time = '2022-09-27T23:00:00.000Z'

# response = client.search_all_tweets(query = query, max_results = 100, start_time = start_time, end_time = end_time)
#
# for tweet in response.data:
#     print(tweet.id)

# Get the tweet volume for any topic
# # availabe in both recent_tweets (last 7 days) and all_tweets
# can specify the granularity of the time window
# counts = client.get_recent_tweets_count(query = query, granularity = 'day')
# # academic access
# # counts = client.get_all_tweets_count(query = query)
#
# for count in counts.data:
#     print(count)

# get a user's timeline
# need the user id
# users = client.get_users(usernames=['twitterdev'])
# for user in users:
#     print(user) # print the user id
#
# # get all tweets of a user
# tweets = client.get_users_tweets(id = '2244994945')
#
# for tweet in tweets.data:
#     print(tweet.id)
#     print(tweet.text)
#
# # get user's followers
# users = client.get_users_followers(id = '2244994945', user_fields = ['profile_image_url'])
#
# # can get who the user is following with get_users_following
#
# for user in users.data:
#     print(user.profile_image_url

# get the users who retweet a
# pass in the tweet id of a certain tweet
# users = client.get_retweeters(id = '1585707921433923585')
# for user in users.data:
#     print(user.id)

# create a tweet
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN,
                       access_token_secret= config.ACCESS_TOKEN_SECRET)

response = client.create_tweet(text = 'hi there')

print(response)
