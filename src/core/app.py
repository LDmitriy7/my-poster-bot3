from telegram import Update
from telegram.ext import Application, CallbackContext

from .context import Context
from .handler import Handler


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


def adapt_callback(callback: ...):
    def wrapper(update: Update, raw_context: CallbackContext):
        context = Context(update, raw_context)
        return callback(context)

    return wrapper
