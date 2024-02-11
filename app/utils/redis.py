
from redis import asyncio as aioredis

redis = aioredis.Redis(host='redis', port=6379, decode_responses=True)