import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8390321457:AAFmqNtMbgVTuIduLyqxDv3LqBfVaULFMew")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "13516702"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bf0cc3f062841935d3d5da65134ca4cf")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6407533831"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tanveer51749:8QU3occg03OHqD3Z@cluster0.ulrpc0d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "tanveersavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
