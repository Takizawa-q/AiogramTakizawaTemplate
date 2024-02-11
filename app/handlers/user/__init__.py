from aiogram import Router, F
from aiogram.filters import CommandStart
from . import start
from . import profile

def prepare_router() -> Router:
    user_router = Router()
    user_router.message.register(start.start, CommandStart())
    user_router.callback_query.register(start.start, F.data == "back_menu")
    user_router.callback_query.register(profile.profile, F.data == "user_profile")
    return user_router
    # user_router.callback_query.register(start.start, None)
