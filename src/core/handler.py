from dataclasses import dataclass

from .events import BaseEvent
from .types import Callback


@dataclass
class Handler:
    event: BaseEvent
    callback: Callback
