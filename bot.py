import discord
from discord.ext import commands
import random
import sqlite3

conn = sqlite3.connect('bot.db')
c = conn.cursor()

# conn.execute('DROP TABLE IF EXISTS users')

conn.execute('CREATE TABLE IF NOT EXISTS `users` (\
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `DiscordId` STRING NOT NULL,\
    `Credits` INTEGER NOT NULL,\
    `ClanMember` BOOLEAN NOT NULL,\
    `Rating` INTEGER NOT NULL,\
    `Points` INTEGER NOT NULL,\
    `Admin` BOOLEAN NOT NULL);')

bot = commands.Bot(command_prefix='!', description='Pokemon Duel Bot.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Adds two integer parameters
@bot.command()
async def add(a: int, b: int):
    "Add two numbers together"
    await bot.say(a + b)

#Subtracts two integer parameters
@bot.command()
async def subtract(a: int, b: int):
    "Subtract two numbers from each other"
    await bot.say(a - b)

#Multiply two integer paramters
@bot.command()
async def multiply(a: int, b: int):
    "Multiply two numbers together"
    await bot.say(a * b)

#Divide two integer paramters
@bot.command()
async def divide(a: int, b: int):
    "Divide two numbers"
    await bot.say(a / b)

#Rolls a die between the two parameters
@bot.command()
async def dice(a: int, b: int):
    "Roll a dice"
    roll = random.randint(a, b)
    await bot.say(roll)

@bot.command()
async def reverse(word: str):
    "Reverse a string"
    await bot.say(word[::-1])

@bot.command(pass_context = True)
async def register(ctx):
    "Register account to database"
    id = ctx.message.author.id
    c.execute("SELECT COUNT(*) FROM users WHERE DiscordId = ?", (id, ))
    foundId = c.fetchone()[0]
    if(foundId == 0):
        if(id == "342256596631683073"):
                c.execute("INSERT INTO users (DiscordId,Credits,ClanMember,Rating,Points,Admin)\
                VALUES (?,?,?,?,?,?)", (id, 500, True, 0, 0, True))
                conn.commit()
                await bot.say("Admin account has been registered with 500 credits.")
        else:
            c.execute("INSERT INTO users (DiscordId,Credits,ClanMember,Rating,Points,Admin)\
            VALUES (?,?,?,?,?,?)", (id, 500, False, 0, 0, False))
            conn.commit()
            await bot.say("Your account has been registered with 500 credits.")
    else:
        await bot.say("Account already registered.")

@bot.command(pass_context = True)
async def setrating(ctx, rating: int, member: discord.Member):
    id = ctx.message.author.id
    userId = member.id
    admin = c.execute("SELECT Admin FROM users WHERE DiscordId = ?", (id, ))
    if admin:
        c.execute("UPDATE users SET Rating = ? WHERE DiscordId = ?", (rating, id))
        conn.commit()
        await bot.say("User's rating has been set.")
    else:
        await bot.say("User does not have permission to set rating.")

@bot.command()
async def rating(member: discord.Member):
    id = member.id
    ratingObj = c.execute("SELECT Rating FROM users WHERE DiscordId = ?", (id, ))
    rating = c.fetchone()[0]
    await bot.say(rating)

@bot.command(pass_context = True)
async def setpoints(ctx, points: int, member: discord.Member):
    id = ctx.message.author.id
    userId = member.id
    admin = c.execute("SELECT Admin FROM users WHERE DiscordId = ?", (id, ))
    if admin:
        c.execute("UPDATE users SET Points = ? WHERE DiscordId = ?", (points, id))
        conn.commit()
        await bot.say("User's points has been set.")
    else:
        await bot.say("User does not have permission to set points.")

@bot.command()
async def points(member: discord.Member):
    id = member.id
    points = c.execute("SELECT Points FROM users WHERE DiscordId = ?", (id, ))
    foundPoints = c.fetchone()[0]
    await bot.say(foundPoints)

@bot.command(pass_context = True)
async def recordmatch(ctx, result: str, member: discord.Member):
    id = ctx.message.author.id
    userId = member.id
    admin = c.execute("SELECT Admin FROM users WHERE DiscordId = ?", (id, ))
    pointsObj = c.execute("SELECT Points FROM users WHERE DiscordId = ?", (id, ))
    points = c.fetchone()[0]
    if admin:
        if result == "win":
            points += 3
            c.execute("UPDATE users SET Points = ? WHERE DiscordId = ?", (points, id))
            bot.say("Points updated by 3.")
        elif result == "dnf":
            points += 1
            c.execute("UPDATE users SET Points = ? WHERE DiscordId = ?", (points, id))
            bot.say("Points updated by 1.")
        else:
            bot.say("Invalid result.")
    else:
        bot.say("User does not have permission to use this command.")

bot.run('NDU0MjkzODI1MDc5MjE0MDgw.DfrVog.l_LDusmnwpGVRHMNHf9G2R4iRuI')
