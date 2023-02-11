from .env import env

BOT_TOKEN = env.get('BOT_TOKEN')
MONGO_DB = env.get('MONGO_DB')
MONGO_HOST = env.get('MONGO_HOST', 'localhost')
MONGO_USER = env.get('MONGO_USER', None)
MONGO_PASSWORD = env.get('MONGO_PASSWORD', None)
