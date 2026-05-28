import aiosqlite

db_name = "bot.db"

async def init_db():
    async with aiosqlite.connect(db_name) as con:
        await con.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, language TEXT)")
        await con.execute("""
                          CREATE TABLE IF NOT EXISTS scrap_history(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                           user_id INT,
                           url TEXT,
                           result TEXT,
                           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                           FOREIGN KEY (user_id) REFERENCES users (user_id))
                          """)
        await con.commit()

async def create_user(user_id: int, username: str, user_first_name: str | None, user_language: str):
    async with aiosqlite.connect(db_name) as con:
        await con.execute("INSERT OR IGNORE INTO users (user_id, username, first_name, language) VALUES (?, ?, ?, ?)",
                           (user_id, username, user_first_name, user_language))
        await con.commit()
        
async def get_user(user_id: int):
    async with aiosqlite.connect(db_name) as con:
        async with con.execute("SELECT first_name, language FROM users WHERE user_id = ?", (user_id,)) as cur:
            return await cur.fetchone()
        
async def get_user_language(user_id: int):
    async with aiosqlite.connect(db_name) as con:
        async with con.execute("SELECT language FROM users WHERE user_id = ?", (user_id,)) as cur:
            return await cur.fetchone()
        
async def get_scraps_count(user_id: int):
    async with aiosqlite.connect(db_name) as con:
        async with con.execute("SELECT * FROM parse_history WHERE user_id = ?", (user_id,)) as cur:
            return await cur.fetchone()