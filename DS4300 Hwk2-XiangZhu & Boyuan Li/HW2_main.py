from HW2 import RedisAPI

import redis

client = redis.Redis(host='localhost', port=6379)
redis_api = RedisAPI(client)
redis_api.clear_db()
redis_api.add_followers()
redis_api.post_tweets(True)
redis_api.post_tweets(False)
redis_api.get_timeline(245, True)
redis_api.get_timeline(245, False)
