from redis import Redis
from os import getenv
from redis.exceptions import ConnectionError

try:
    redis_client = Redis(
        host= getenv('REDIS_HOST'),
        port= getenv('REDIS_PORT'),
        password= getenv('REDIS_PASSWORD'),
        ssl= bool(getenv('REDIS_SSL'))
    )
    print("Redis client connected successfully")
except ConnectionError as e:
    print(e)
