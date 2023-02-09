import pymongo

db_client = pymongo.MongoClient()
random_avatars_db = db_client['Random_avatars_bot']
single_avatars = random_avatars_db['Single_avatars']

