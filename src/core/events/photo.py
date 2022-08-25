from dataclasses import dataclass

from telegram.ext import MessageHandler, filters
# noinspection PyProtectedMember
from telegram.ext._utils.types import HandlerCallback

from .base_event import BaseEvent


@dataclass
class Photo(BaseEvent):

    def make_handler(self, callback: HandlerCallback) -> MessageHandler:
        return MessageHandler(filters.PHOTO, callback)
