from dataclasses import dataclass

from telegram.ext import CommandHandler, filters
# noinspection PyProtectedMember
from telegram.ext._utils.types import HandlerCallback

from .base_event import BaseEvent


@dataclass
class Command(BaseEvent):
    value: str
    user_id: int | list[int] = None

    def make_handler(self, callback: HandlerCallback) -> CommandHandler:
        filters_ = None

        if self.user_id:
            filters_ = filters.User(self.user_id)

        return CommandHandler(self.value, callback, filters_)
