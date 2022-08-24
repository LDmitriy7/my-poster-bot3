import logging

import config
from core import App
from handlers import HANDLERS

logging.basicConfig(level=logging.INFO, filename='.log', filemode='w')

app = App(config.BOT_TOKEN, HANDLERS)

app.run()
