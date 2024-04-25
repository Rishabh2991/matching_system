class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/matchmaking'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379