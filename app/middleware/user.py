from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from app.db.models.user import UserDTO
from app.utils.redis import redis
from app.db.tables import db
from app.config import config

class RegisterUser(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Union[Message, CallbackQuery],
                       data: Dict[str, Any]) -> Any:

        user = UserDTO(user_id=event.from_user.id,
                       username=event.from_user.username,
                       full_name=event.from_user.full_name)
        if config.redis.use_redis:
            print("user redis")
            if not await redis.get(name=f"if_user_exists: {str(user.user_id)}"):
                db.user.add_user(user=user)
                await redis.set(name=f"if_user_exists: {str(user.user_id)}", value=1)
        else:
            db_user = await db.user.get_user()
            if not db_user:
                await db.user.add_user(user=user)

        return await handler(event, data)
