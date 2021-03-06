import os

# Telegram bot API settings.

# Bot token received from BotFather.
TELEGRAM_BOT_TOKEN = 'set in local_settings.py'


# DialogFlow API settings.

# Path to private key settings generated by google cloud.
PRIVATE_KEY_PATH = 'set in local_settings.py'

DIALOGFLOW_PROJECT_ID = 'set in local_settings.py'

# Default language code, override in local_settings.py if it is necessary.
DIALOGFLOW_LANGUAGE_CODE = 'en-US'


try:
	from app.local_settings import *
except ImportError:
	pass


# Setup.

assert os.path.exists(PRIVATE_KEY_PATH)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PRIVATE_KEY_PATH
