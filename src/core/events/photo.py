from dataclasses import dataclass

from telegram.ext import MessageHandler, filters

from .base_event import BaseEvent


@dataclass
class Photo(BaseEvent):

    def make_handler(self, callback: ...) -> MessageHandler:
        return MessageHandler(filters.PHOTO, callback)
