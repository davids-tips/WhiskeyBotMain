# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# NOTICE PULL THE LATEST COMMIT FROM GITHUB THIS INSTANCE WAS FOR TESTING CHANNEL CREATION
import disnake
from disnake.ext import commands
import datetime
import os
# import requests
from dotenv import load_dotenv
#import aiohttp
#import aiofiles

#import logging

#logging.basicConfig(level=logging.INFO)



import cogs.whiskey
from colorama import Fore, Back, Style
bot = commands.Bot(command_prefix="$")
ct = datetime.datetime.now()
guild_ids = []
print('Starting Bot')
print('Connecting to Discord API.')
print('Please Wait')

@bot.event
async def on_ready():
    print(Fore.GREEN + 'Connected!' + Fore.WHITE)
    print(Fore.GREEN + 'Bot is ready!' + Fore.WHITE)
    print(Fore.CYAN + 'Waiting For Commands' + Fore.WHITE)
    bot.get_guild(798726719573065749)
    channel = bot.get_channel(798726720181633047)
    await channel.send('Bot Online!')
    embed = disnake.Embed()
    embed.title = f"**Online**"
    embed.description = f"[`{datetime.datetime.now().strftime('%b-%d-%Y`] @ [`%I:%M:%S')}`]\n\n" \
    f"- Bot account: `{bot.user.name}`\n" \
    f'- Bot ID: `{bot.user.id}`\n' \
    f"- Guilds: `{len(bot.guilds):,}`\n" \
    f"- Users: `{len(list(bot.get_all_members()))}`\n" \
#    f"- Project Repo Version: `{repo.version}`\n" 
    f"- Disnake Version: `{disnake.__version__}`\n" 
    embed.set_footer(text="Logging System")
    GUILD_ID = 798726719573065749
    CHANNEL_ID  = 798726720181633047
    location = bot.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
    await location.send(embed=embed)
# Add Cogs

#bot.load_extension('cogs.social')
#bot.load_extension('cogs.chat_room_managment')
# bot.load_extension('cogs.socialv2')
#bot.load_extension('cogs.database')
# bot.load_extension('cogs.embd')
bot.load_extension('cogs.developerfeatures')
print(Fore.YELLOW  + '[✓]' + '[Developer Features Cog] ' + Fore.GREEN  +  'Loading Complete' + Fore.WHITE)

# below command is to learn how to pull images from a message, will eventually be intregated into dnd homebrew approval grab command
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
    	print(Fore.CYAN  + '[DEBUG]' + Fore.YELLOW + 'Num Fallback Active' + Fore.WHITE)
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
        #checks if message had any reactions
        if msg.reactions:
            # scans message for specific reactions
            for reaction in msg.reactions:
                if reaction.emoji ==  '✅':
                    print(Fore.GREEN +  '[✓] Checkmark Detected')
                    # message sent is for debuging
                    await ctx.send(f'checkmark detected! it is in {msg.id}', delete_after=5)
                    #it then adds the reaction to the message with a checkmark reaction
                    await msg.add_reaction('<furheart:802746458088013864>')
                    # We break since we already found the check, heading to next message
                    await msg.reply('checkmark here^',delete_after=10)
                    break


# the following command is to showcase how to add buttons and get interactions with them.
#@bot.command(name='button')
#async def button(ctx):
#    # sends message with atached buttons
#    await ctx.send(
#        "Hello, World!",
#        components = [Button(label = "WOW button!", custom_id = "button1"), Button(label = "hahahaha", custom_id = "button2") ]
#    )
#    # waits for interaction with button
#    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button1")
#    # sends a "hidden message only visible to user who clicked button"
#    await interaction.send(content = "Button clicked!")
#    # replies to message that ran command.
#    await ctx.reply('reply here')
    
@bot.command(name="lnk")
async def lnk(ctx, link):
    print(Fore.YELLOW + ctx.message.content + Fore.WHITE)
#assuming this is inside a command
# I recommend creating a single ClientSession and storing it in a botvar
    async with aiohttp.ClientSession() as session:
        image = await session.get(link)
    async with aiofiles.open('image.png', 'wb') as f:
        await f.write(image.content)
        await ctx.send("image underneath", file=discord.File("image.png"))

  #  assuming url as an url 
#    response = requests.get(f'{link}')
#    content = response.content
#    open('image.png', 'wb').write(content)
#    await ctx.send(file=disnake.File(content))
  #  await ctx.send(file=discord.File(image.png))











# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
#avoid scrolling down to prevent token leak




load_dotenv()



token = os.getenv('TOKEN')


bot.run(token)
