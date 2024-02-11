from ..connection import DbConnection
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class UserDTO:
    user_id: int
    username: Optional[str]
    full_name: Optional[str]
    reg_date: datetime = datetime.now()


class User(DbConnection):

    __tablename__ = "user"

    @classmethod
    async def create_table(cls):
        async with cls.pool.cursor() as cur:
            await cur.execute("CREATE TABLE IF NOT EXISTS "
                              "user (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT,"
                              "username TEXT, full_name TEXT, reg_date DATETIME)")

    @classmethod
    async def get_user(cls):
        async with cls.pool.cursor() as cur:
            cursor = await cur.execute("SELECT * FROM user;")
            rows = await cursor.fetchone()
            if rows:
                return UserDTO(
                    user_id=rows[0],
                    username=rows[1],
                    full_name=rows[2],
                    reg_date=rows[3]
                )
            else:
                return None
                

    @classmethod
    async def add_user(cls, user: UserDTO):
        async with cls.pool.cursor() as cur:
            await cur.execute("INSERT INTO user (user_id, username, full_name, reg_date)"
                              "VALUES (?, ?, ?, ?)", (user.user_id,
                                                          user.username,
                                                          user.full_name,
                                                          user.reg_date))
            await cls.pool.commit()