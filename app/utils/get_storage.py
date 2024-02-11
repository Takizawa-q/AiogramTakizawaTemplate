from app.config import config
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder


def get_storage():
    if config.redis.use_redis:
        return RedisStorage.from_url(
            f"redis://{config.redis.password}@{config.redis.host}:{config.redis.port}/db",
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()
