from aiogram import Bot, Dispatcher
from app import config, utils, handlers
from app import middleware
from aiosqlite import Connection
import asyncio
from app.db.connection import DbConnection
import sys
from app.db.tables import db


async def register_middlewares(dp: Dispatcher, pool: Connection):
    middleware_types = [
        middleware.database.DbConnectionMiddleware(pool=pool),
        middleware.user.RegisterUser()
    ]
    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


async def create_tables():
    await db.user.create_table()


def register_routers(dp: Dispatcher):
    dp.include_router(handlers.user.prepare_router())
    dp.include_router(handlers.admin.prepare_router())


async def main():
    storage = utils.get_storage()
    bot = Bot(config.tgbot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    db_pool = await DbConnection().create_connection()
    
    
    register_routers(dp)
    await create_tables()
    
    await register_middlewares(dp,
                               pool=db_pool)

    await utils.on_startup(bot, config.tgbot.admin_ids)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit, SystemError):
        print("EXIT")
        sys.exit()
