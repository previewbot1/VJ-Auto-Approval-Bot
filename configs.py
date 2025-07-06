# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20342933"))
    API_HASH = getenv("API_HASH", "9233e5deebe6abfc9ba297a9678851be")
    BOT_TOKEN = getenv("BOT_TOKEN", "7232503574:AAHvuJuw0L5pmW9xpUlRPjrh1JTZ2UrSvJU")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002722969828")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sanjusen212121:skjdJi9uJwmwjCs7@cluster0.frho2nd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
