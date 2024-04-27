import os


class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "test")