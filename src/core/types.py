from typing import Callable, Coroutine

from .update_context import UpdateContext

Callback = Callable[[UpdateContext], Coroutine]
