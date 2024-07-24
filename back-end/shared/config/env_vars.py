import os


class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "test")
    MONGO_USERNAME = os.getenv("MONGO_USERNAME", "user")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "12")
    MONGO_HOST = os.getenv("MONGO_HOST", "")
    MONGO_DB = os.getenv("MONGO_DB", "default")