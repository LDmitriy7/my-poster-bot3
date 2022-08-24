import config
from core import events

logs = events.Command('logs', user_id=config.ADMINS_IDS)
