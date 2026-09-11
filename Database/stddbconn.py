# from pymongo import MongoClient

# ConnectionString = MongoClient(
#     "mongodb+srv://dipalikawade08_db_user:pd24r6xYxd0iW0V8@cluster1.mxawhza.mongodb.net/?appName=Cluster1"
# )

# Database = ConnectionString["Student123"]

# Collection = Database["StudentInfo"]


from pymongo import MongoClient

ConnectionString = MongoClient(
    "mongodb+srv://dipalikawade08_db_user:pd24r6xYxd0iW0V8@cluster1.mxawhza.mongodb.net/?appName=Cluster1"
)

Database = ConnectionString["Student123"]

collection = Database["StudentInfo"]