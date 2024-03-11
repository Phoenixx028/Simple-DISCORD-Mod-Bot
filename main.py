import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# Custom decorator to check if the command is invoked by the owner
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 1211883781494022174  # Replace YOUR_OWNER_ID_HERE with your actual Discord user ID
    return commands.check(predicate)

# Define intents
intents = discord.Intents.all()

# Create an instance of the bot
bot = commands.Bot(command_prefix='!',intents=intents, help_command=None)

# Event to print a message in the console when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command to greet the user
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your friendly Discord bot.')

# Command to add two numbers
@bot.command()
async def add(ctx, num1: int, num2: int):
    await ctx.send(f'The sum is: {num1 + num2}')

# Command to display the list of available commands
@bot.command()
async def help(ctx):
    commands_list = "\n".join([f"• {command.name}" for command in bot.commands])
    await ctx.send(f"Available commands:\n{commands_list}")

# Command to check the bot's latency
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')

# Command to display bot information
@bot.command()
async def info(ctx):
    await ctx.send('I am a Discord bot created using discord.py!')

# Command to kick a user from the server (restricted to administrators)
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.name} has been kicked from the server.')

# Command to ban a user from the server (restricted to administrators)
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'{member.name} has been banned from the server.')

# Command to mute a user in the server (restricted to administrators)
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    # Add code to mute the user
    await ctx.send(f'{member.name} has been muted.')

# Command to unmute a user in the server (restricted to administrators)
@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    # Add code to unmute the user
    await ctx.send(f'{member.name} has been unmuted.')

# Command to retrieve weather information for a specified location
@bot.command()
async def weather(ctx, location):
    # Add code to retrieve weather information
    await ctx.send(f'The weather in {location} is...')

# Command to display the current time for a specified location
@bot.command()
async def time(ctx, location):
    # Add code to retrieve current time for the specified location
    await ctx.send(f'The current time in {location} is...')

# Command to look up a term on Urban Dictionary
@bot.command()
async def urban(ctx, term):
    # Add code to look up the term on Urban Dictionary
    await ctx.send(f'Urban Dictionary definition for "{term}"...')

# Command to roll a dice with a specified number of sides
@bot.command()
async def roll(ctx, number: int):
    # Add code to roll the dice
    await ctx.send(f'You rolled a {number}-sided dice and got...')

# Command to flip a coin
@bot.command()
async def flip(ctx):
    # Add code to flip a coin
    await ctx.send('Flipping a coin...')

# Command to display information about a user
@bot.command()
async def user(ctx, member: discord.Member):
    # Add code to display user information
    await ctx.send(f'Information about {member.name}...')

# Command to display information about the server
@bot.command()
async def server(ctx):
    # Add code to display server information
    await ctx.send(f'Information about the server...')

# Command to display the avatar of a user
@bot.command()
async def avatar(ctx, member: discord.Member):
    # Add code to display user avatar
    await ctx.send(member.avatar_url)

# Command to add a custom command (restricted to bot owner)
@bot.command()
@is_owner()
async def addcommand(ctx, command_name, *, response):
    # Add code to add a custom command
    await ctx.send(f'Added new command: !{command_name}')

# Command to delete a custom command (restricted to bot owner)
@bot.command()
@is_owner()
async def deletecommand(ctx, command_name):
    # Add code to delete a custom command
    await ctx.send(f'Deleted command: !{command_name}')

# Keep the bot alive
keep_alive()

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))
