import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from pip._internal.utils.misc import tabulate
from tabulate import tabulate


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#create SQL Database

import sqlite3

conn = sqlite3.connect('burger.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS counters (
        user_id TEXT PRIMARY KEY,
        count INTEGER DEFAULT 0
    )
''')

conn.commit()
conn.close()

#end Create SQL Database

bot = commands.Bot(command_prefix='!', intents=intents)

#Increment counters
@bot.command()
async def addburger(ctx, amount: int = 1):
    user_id = str(ctx.author.id)
    conn = sqlite3.connect('burger.db')
    c = conn.cursor()

    # Validate input
    if amount < 1:
        await ctx.send(f"{ctx.author.name}, you need to eat at least one burger!")
        conn.close()
        return

    # Check if user already exists
    c.execute('SELECT count FROM counters WHERE user_id = ?', (user_id,))
    result = c.fetchone()

    if result:
        new_total = result[0] + amount
        c.execute('UPDATE counters SET count = ? WHERE user_id = ?', (new_total, user_id))
    else:
        new_total = amount
        c.execute('INSERT INTO counters (user_id, count) VALUES (?, ?)', (user_id, new_total))

    conn.commit()
    conn.close()

    await ctx.send(f"{ctx.author.name}, you've devoured {amount} burger{'s' if amount > 1 else ''}! 🍔 Total burgers: {new_total}")

# Remove counter
@bot.command()
async def removeburger(ctx):
    user_id = str(ctx.author.id)
    conn = sqlite3.connect('burger.db')
    c = conn.cursor()

    c.execute('SELECT count FROM counters WHERE user_id = ?', (user_id,))
    result = c.fetchone()

    if result:
        current_count = result[0]
        if current_count > 0:
            c.execute('UPDATE counters SET count = count -1 WHERE user_id = ?', (user_id,))
            conn.commit()
            await ctx.send(f"{ctx.author.name}, you've hurled up a burger.")
        else:
            await ctx.send(f"{ctx.author.name}, you don't have a burger to hurl.")

    conn.close()

#Display table
@bot.command()
async def burgerboard(ctx):
    conn = sqlite3.connect('burger.db')
    c = conn.cursor()

    c.execute('SELECT user_id, count FROM counters ORDER BY count DESC')
    rows = c.fetchall()
    conn.close()

    table = []
    for user_id, count in rows:
        user = await bot.fetch_user(int(user_id))
        table.append([user.name, count])

    formatted_table = tabulate(table, headers=["User", "Count"], tablefmt="pretty")
    await ctx.send(f"```\n{formatted_table}\n```")


@bot.command()
async def commands(ctx):
    help_text = """ 
    *** 🍔 Burger Bot Command Guide 🍔 ***
    
    !addburger [amount] - this will add one or more burgers to your burger count
    !removeburger - this will remove a burger from your burger count
    !burgerboard - this will display the current burger counts for participants

    """
    await ctx.send(help_text)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
