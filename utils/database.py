import aiosqlite

db_name = "bot.db"

async def init_db():
    async with aiosqlite.connect(db_name) as con:
        await con.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, user_first_name TEXT, user_language TEXT)")
        await con.execute("""
                          CREATE TABLE IF NOT EXISTS parse_history(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                           user_id INT,
                           url TEXT,
                           result TEXT,
                           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                           FOREIGN KEY (user_id) REFERENCES users (user_id))
                          """)
        await con.commit()