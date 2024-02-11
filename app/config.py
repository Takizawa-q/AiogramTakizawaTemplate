from environs import Env
from dataclasses import dataclass
from typing import Optional


@dataclass
class DB:
    user: str
    password: str
    database: str
    host: str
    port: Optional[int]


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Redis:
    password: Optional[str]
    port: Optional[int]
    host: Optional[str]
    use_redis: Optional[str]

    def data_souce_name(self) -> str:
        if self.password:
            return f"redis://:{self.password}@{self.host}:{self.port}/0"
        else:
            return f"redis://{self.host}:{self.port}/0"


@dataclass
class Config():
    redis: Redis
    tgbot: TgBot
    db: DB


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        tgbot=TgBot(
            token=env.str("TOKEN"),
            admin_ids=list(map(int, env.list("ADMIN_IDS"))),
        ),
        db=DB(
            user=env.str("DB_USER"),
            password=env.str("DB_PASSWORD"),
            database=env.str("DB_DATABASE"),
            host=env.str("DB_HOST"),
            port=env.str("DB_PORT")
        ),
        redis=Redis(

            use_redis=env.str("USE_REDIS"),
            password=env.str("REDIS_PASS"),
            host=env.str("REDIS_HOST"),
            port=env.str("REDIS_PORT")
        )

    )


config = load_config()
