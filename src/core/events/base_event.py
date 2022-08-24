from abc import ABC, abstractmethod

from telegram.ext import BaseHandler


class BaseEvent(ABC):

    @abstractmethod
    def make_handler(self, callback: ...) -> BaseHandler:
        """ Make raw handler """
