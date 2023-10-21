"""Redis database implementation."""

from prettyconf import config
from redis import Redis


REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")

redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}"
redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT,
                   db=0, decode_responses=True)
