import os

class SQLConfig:
    USER_ID = 'root'
    PASSWORD = 'root'
    IP = os.getenv('DB_SERVER', '10.132.0.3')
    DB = os.getenv('DB_NAME ', 'clouddr') 

