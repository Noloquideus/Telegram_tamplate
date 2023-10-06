import asyncpg
from data import DATABASE_URL


async def create_connection():
    try:
        connection = await asyncpg.connect(DATABASE_URL)
        print("Connection successful")
        return connection
    except asyncpg.exceptions.PostgresError as e:
        print(f"Error '{e}' occurred")
