from aiogram import Dispatcher
from handlers.admin_handlers import register_admin_handlers
from handlers.common_handlers import register_common_handlers
from handlers.user_handlers import register_user_handlers


def setup(dp: Dispatcher):
    register_admin_handlers(dp)
    register_common_handlers(dp)
    register_user_handlers(dp)