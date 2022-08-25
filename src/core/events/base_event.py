from abc import ABC, abstractmethod

from telegram.ext import BaseHandler
# noinspection PyProtectedMember
from telegram.ext._utils.types import HandlerCallback


class BaseEvent(ABC):

    @abstractmethod
    def make_handler(self, callback: HandlerCallback) -> BaseHandler:
        """ Make raw handler """
