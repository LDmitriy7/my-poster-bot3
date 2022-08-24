from dataclasses import dataclass

from .events import BaseEvent


@dataclass
class Handler:
    event: BaseEvent
    callback: ...
