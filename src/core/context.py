from telegram import Update, InputFile
from telegram.ext import CallbackContext


class Context:
    def __init__(self, update: Update, raw_context: CallbackContext):
        self._update = update
        self._raw = raw_context

    def send_message(self, text: str):
        update = self._update
        bot = self._raw.bot

        return bot.send_message(update.effective_chat.id, text)

    def send_document(self, path: str, filename: str = None):
        update = self._update
        bot = self._raw.bot

        with open(path, 'rb') as file_reader:
            return bot.send_document(update.effective_chat.id, InputFile(file_reader, filename))
