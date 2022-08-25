from telegram import Update
from telegram.ext import Application, CallbackContext
# noinspection PyProtectedMember
from telegram.ext._utils.types import HandlerCallback

from .update_context import UpdateContext
from .handler import Handler
from .types import Callback


class App:
    def __init__(self, token: str, handlers: list[Handler]):
        self._raw = Application.builder().token(token).build()
        self._setup_handlers(handlers)

    def _setup_handlers(self, handlers: list[Handler]):
        for handler in handlers:
            self._setup_handler(handler)

    def _setup_handler(self, handler: Handler):
        event = handler.event
        callback = adapt_callback(handler.callback)
        raw_handler = event.make_handler(callback)
        self._raw.add_handler(raw_handler)

    def run(self):
        self._raw.run_polling()


def adapt_callback(callback: Callback) -> HandlerCallback:
    def wrapper(update: Update, raw_context: CallbackContext):
        context = UpdateContext(update, raw_context)
        return callback(context)

    return wrapper
