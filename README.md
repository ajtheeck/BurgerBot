🍔 Burger Bot
Burger Bot is a fun Discord bot that lets users track how many burgers they've "eaten" in a server. It uses SQLite for persistent storage and offers a leaderboard to show who's the hungriest of them all.
🚀 Features
- !addburger [amount]: Adds burgers to your personal count.
- !removeburger: Removes one burger from your count.
- !burgerboard: Displays a leaderboard of burger consumption.
- !commands: Shows a list of available commands.
  
🛠️ Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/burger-bot.git
cd burger-bot


2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
pip install discord.py python-dotenv tabulate


3. Create a .env File
Add your Discord bot token to a .env file in the root directory:
DISCORD_TOKEN=your_discord_bot_token_here


4. Run the Bot
python bot.py


🧠 How It Works
- Database: Uses SQLite (burger.db) to store user burger counts.
- Logging: Logs bot activity to discord.log.
- Commands:
- !addburger [amount]: Adds burgers to your count (minimum 1).
- !removeburger: Removes one burger if you have any.
- !burgerboard: Displays a formatted leaderboard using tabulate.
- !commands: Lists all available commands.

📦 File Structure
burger-bot/
├── bot.py               # Main bot logic
├── burger.db            # SQLite database
├── discord.log          # Log file
├── .env                 # Environment variables
├── webserver.py         # Keeps bot alive (for hosting platforms like Replit)
