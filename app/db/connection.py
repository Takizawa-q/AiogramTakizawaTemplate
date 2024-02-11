from aiomysql import Connection
from app.config import config
import aiosqlite

class DbConnection:

    pool: Connection = None

    @classmethod
    async def create_connection(cls) -> None:
        if cls.pool is None:
            print("CREATING CONNECTION...")
            cls.pool = await aiosqlite.connect(
            database=config.db.database,
            
        )
        else:
            print("CONNECTION ALREADY RUNNING")
        return cls
