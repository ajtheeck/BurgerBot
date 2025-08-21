# 🍔 Burger Bot

Burger Bot is a playful Discord bot that tracks how many burgers each user has "eaten." It uses SQLite for persistent storage and offers a few simple commands to manage and display burger counts.

## 🚀 Features

- `!addburger [amount]` — Add one or more burgers to your personal burger count.
- `!removeburger` — Remove a burger from your count (if you have any).
- `!burgerboard` — View the burger leaderboard for all users.
- `!commands` — Display a help guide with available commands.

## 🛠 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/burger-bot.git
   cd burger-bot
   ```

2. **Install dependencies**  
   ```bash
   pip install discord.py python-dotenv tabulate
   ```

3. **Create a `.env` file**  
   Add your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

4. **Run the bot**  
   ```bash
   python bot.py
   ```

## 🧠 Tech Stack

- Python 3
- discord.py
- SQLite
- dotenv
- tabulate

## 📁 Database

Burger Bot uses a simple SQLite database (`burger.db`) with a single table:

```sql
CREATE TABLE IF NOT EXISTS counters (
    user_id TEXT PRIMARY KEY,
    count INTEGER DEFAULT 0
);
```

## 📜 License

MIT License — feel free to fork, modify, and share!

---

Made with hunger and humor 🍔
```

Let me know if you'd like a version tailored for GitHub Pages or with badges and visuals. I can spice it up!

