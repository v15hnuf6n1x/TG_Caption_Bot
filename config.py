import os



class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "V15HNUF6N1X")
      ADMIN_ID = int(os.environ.get("ADMIN", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
