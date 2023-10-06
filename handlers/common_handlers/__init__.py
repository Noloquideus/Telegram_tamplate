from handlers.common_handlers.start_handler import start_handler


def register_common_handlers(dp):
    dp.register_message_handler(start_handler, commands='start')