import disnake
from disnake.ext import commands
from datetime import datetime
import os
# import requests
from dotenv import load_dotenv
import time
# import aiohttp
# import aiofiles
import logging
import cogs.whiskey
from colorama import Fore
import nacl
logging.basicConfig(level=logging.INFO)

start_time = datetime.now()
mytime = time.localtime()
if mytime.tm_hour < 12:
    timeofday = 'AM'
else:
    timeofday = 'PM'



load_dotenv()
guild_strings = os.getenv('GUILDS')
config = [int(guild_id) for guild_id in guild_strings.split(",")]
bot = commands.Bot(command_prefix="$", intents=disnake.Intents.all())

ct = datetime.now()
guild_ids = []
print('Starting Bot')
print('Connecting to Discord API.')
print('Please Wait')


# Add Cogs

# bot.load_extension('cogs.social')
# bot.load_extension('cogs.chat_room_managment')
# bot.load_extension('cogs.socialv2')
# bot.load_extension('cogs.database')
# bot.load_extension('cogs.embd')
bot.load_extension('cogs.CommandErrorHandler')
bot.load_extension('cogs.developerfeatures')
bot.load_extension('cogs.events')
bot.load_extension('jishaku')
bot.load_extension('cogs.aboutme')
print(Fore.YELLOW + '[✓]' + '[Developer Features Cog] ' + Fore.GREEN + 'Loading Complete' + Fore.WHITE)
print(Fore.YELLOW + '[✓]' + '[Events Cog] ' + Fore.GREEN + 'Loading Complete' + Fore.WHITE)
print(Fore.YELLOW + '[✓]' + '[jishaku Cog] ' + Fore.GREEN + 'Loading Complete' + Fore.WHITE)
print(Fore.YELLOW + '[✓]' + '[About Me Cog] ' + Fore.GREEN + 'Loading Complete' + Fore.WHITE)


# below command is to learn how to pull images from a message, will eventually be intregated into dnd homebrew
# approval grab command
@bot.command(name='cmd')
async def urls(ctx):
    list_urls = []
    for atchm in ctx.message.attachments:
        list_urls.append(atchm.url)
        await ctx.send(atchm.url)
        print(atchm.url)
        #          await ctx.send( "\n".join(list_urls)
    # optional_arg: int = None


@bot.command(name='allmsg')
async def msg(ctx, num: int = None):
    # below is a debug output to show when command is recieved.
    print('Running Search')
    if num == None:
        num = 10
        # fallback settings incase commanding user dosen't specify a number of messages'
        print(Fore.CYAN + '[DEBUG]' + Fore.YELLOW + 'Num Fallback Active' + Fore.WHITE)
    else:
        print(num)
        # debug output to show if custom number of messages is used
        print(Fore.CYAN + '[DEBUG]' + Fore.YELLOW + f'Custom Message Number Active {num}' + Fore.WHITE)

    msgs = [message async for message in ctx.channel.history(limit=num)]
    # ^ messages is now a list of Messages
    # below line runs checks for each message as described / laid out beloq
    for msg in msgs:
        # below print statment is for debugging.
        print(Fore.CYAN + '[MSG CONTENT]-' + Fore.YELLOW + msg.content + Fore.WHITE)
        # checks if message had any reactions
        if msg.reactions:()
            # scans message for specific reactions
        for reaction in msg.reactions:
                if reaction.emoji == '✅':
                    print(Fore.GREEN + '[✓] Checkmark Detected')
                    # message sent is for debuging
                    await ctx.send(f'checkmark detected! it is in {msg.id}', delete_after=5)
                    # it then adds the reaction to the message with a checkmark reaction
                    await msg.add_reaction('<furheart:802746458088013864>')
                    # We break since we already found the check, heading to next message
                    await msg.reply('checkmark here^', delete_after=3)
                    break


"""
@bot.command(name="lnk")
async def lnk(ctx, link):
    print(Fore.YELLOW + ctx.message.content + Fore.WHITE)
    # assuming this is inside a command
    # I recommend creating a single ClientSession and storing it in a botvar
    async with aiohttp.ClientSession() as session:
        image = await session.get(link)
    async with aiofiles.open('image.png', 'wb') as f:
        await f.write(image.content)
        await ctx.send("image underneath", file=discord.File("image.png"))"""


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
# avoid scrolling down to prevent token leak
async def startup():
    await bot.wait_until_ready()
    print('running startup embed')
    embed = disnake.Embed()
    embed.title = f"**Online**"
    embed.set_footer(text="Logging System")
    embed.set_author(name='WhiskeyBot', icon_url=f"{bot.user.avatar}")
    embed.description = f"""**Bot Startup and Information**
    Start Time: `{datetime.now().strftime('%b-%d-%Y at %I:%M:%S')} {timeofday}`
    Current Uptime: <t:{round(datetime.timestamp(start_time))}:R>
    Bot account: `{bot.user.name}`
    Bot ID: `{bot.user.id}`
    Guilds: `{len(bot.guilds):,}`
    Users: `{len(list(bot.get_all_members()))}`
    Disnake Version: `{disnake.__version__}`
    Loaded Cogs: `{list(bot.cogs)}`
    Developer: `whiskeythefox#7339`
    """
    GUILD_ID = 798726719573065749
    CHANNEL_ID = 798726720181633047
    location = bot.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
    await location.send(embed=embed)
bot.loop.create_task(startup())
load_dotenv()

token = os.getenv('TOKEN')

bot.run(token)