from aiogram import Bot
import asyncio


async def on_startup(bot: Bot, admin_ids: list[int]):
    
    for admin_id in admin_ids:
        try:
            await bot.send_message(admin_id, "Bot is started!")
            await asyncio.sleep(0.05)
        except Exception:
            print(
                f"Couldn't send on_startup() to admin with admin_id: {admin_id}")
            pass
