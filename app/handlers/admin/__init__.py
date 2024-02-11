from aiogram.dispatcher.router import Router
from aiogram import F
from . import get_users
from . import users_sender


def prepare_router() -> Router:
    admin_router = Router()
    admin_router.callback_query.register(get_users.get_users, F.data == "admin_users")
    admin_router.callback_query.register(users_sender.user_send_message, F.data == "admin_sender")
    return admin_router