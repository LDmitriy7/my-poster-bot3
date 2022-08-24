from core import Handler
from . import callbacks
from . import events

HANDLERS = [
    Handler(events.start, callbacks.ask_post),
    Handler(events.photo, callbacks.echo_photo),
    Handler(events.commands.logs, callbacks.send_logs),
]
