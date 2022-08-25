from telegram import Update, InputFile, Message
from telegram.ext import CallbackContext


class UpdateContext:
    def __init__(self, update: Update, raw_context: CallbackContext):
        self._update = update
        self._raw = raw_context

    @property
    def message(self) -> Message:
        return self._update.message

    @property
    def photo_id(self) -> str:
        return self.message.photo[-1].file_id

    def send_message(self, text: str):
        update = self._update
        bot = self._raw.bot

        return bot.send_message(update.effective_chat.id, text)

    def send_document(self, path: str, filename: str = None):
        update = self._update
        bot = self._raw.bot

        with open(path, 'rb') as file_reader:
            return bot.send_document(update.effective_chat.id, InputFile(file_reader, filename))

    def send_photo(self, photo_id: str):
        update = self._update
        bot = self._raw.bot
        return bot.send_photo(update.effective_chat.id, photo_id)
