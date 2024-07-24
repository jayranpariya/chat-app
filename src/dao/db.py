from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from src.core.config import get_app_settings


settings = get_app_settings()

# Create a Motor client
client = AsyncIOMotorClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

# Get the database
db = client[settings.MONGO_INITDB_DATABASE]

# Get collections
User = db.users

# Function to create indexes


async def create_indexes():
    await User.create_index([("email", 1)], unique=True)

# Run the index creation
asyncio.get_event_loop().run_until_complete(create_indexes())
