from aiogram import BaseMiddleware
from typing import Any, Awaitable, Callable, Dict
from aiogram.types import TelegramObject, Message
from app.db.connection import DbConnection
from app.db.tables import db


class DbConnectionMiddleware(BaseMiddleware):
    def __init__(self, pool):
        self.pool = pool

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        if not self.pool:
            self.pool = DbConnection().create_connection()
        data['db'] = db
        return await handler(event, data)
