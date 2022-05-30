import disnake
from disnake.ext import commands
from colorama import Fore
from datetime import datetime
import time
from wb import config

#below are two date time functions that have different functions but one of them adds to the other during startup

start_time = datetime.now()
mytime = time.localtime()
if mytime.tm_hour < 12:
    timeofday = 'AM'
else:
    timeofday = 'PM'

class events(commands.Cog):
    """Useful Features for Bot Development."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print(Fore.CYAN + 'Loading Events cog' + Fore.WHITE)

    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.GREEN + 'Connected!')
        print('Bot is ready!' + Fore.WHITE)
        print(Fore.CYAN + 'Waiting For Commands' + Fore.WHITE)

    @commands.slash_command(name="ping", guild_ids=config)
    async def ping(self, ctx):
        await ctx.send('Pong! {0}'.format(round(self.bot.latency, 1)) + ' seconds')

    @commands.slash_command(name="uptime", guild_ids=config)
    async def uptime(self, ctx):
        now = datetime.now()
        delta = datetime.now() - start_time
        days, hours, minutes, seconds = delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60
        await ctx.send(f'`{days} Days {hours} hrs {minutes} mins {seconds} secs`')

    @commands.slash_command(name="checkmark", guild_ids=config)
    async def checkmark(self, ctx, amount: int = None):
        msgs = [message async for message in ctx.channel.history(limit=amount)]
        count = 0
        if amount is None:
            amount = 10
            
        total = amount
        for amount in msgs:
            count = count + 1
            await amount.add_reaction('✅')
            await amount.reply(f'Added Checkmark^ (current count: {count} out of {total} messages.)',delete_after=2)

    @commands.slash_command(name="remove-checkmark", guild_ids=config)
    async def rmcheckmark(self,ctx, amount: int = None):
        if amount is None:
            amount = 10
            return
        await ctx.respond('Command in Progress.')
        msgs = [message async for message in ctx.channel.history(limit=amount)]
        count = 1
        total = amount
        for amount in msgs:
            await amount.clear_reaction('✅')
            count += 1
            await amount.reply(f'Cleared checkmark reaction^ ({count} out of {total})',)

    @commands.slash_command(name="removereaction", guild_ids=config)
    async def rmreaction(self, ctx, reaction: str = commands.Param('reaction_name', description='Your choice depicts what reaction will be removed', choices=['checkmark','furheart','both']), amount: int = commands.Param('how_many_messages', description="Your input depicts the number of messages who's reactions get removed.", min_value=0)):
        msgs = [message async for message in ctx.channel.history(limit=amount)]
        count = 1
        total = amount
        for amount in msgs:
            if reaction == 'checkmark':
                await amount.clear_reaction('✅')
                await amount.reply(f'cleared (checkmark) reaction^ (number {count} out of {total} messages)',delete_after=2)
                count += 1
                
            elif reaction == 'furheart':
                await amount.clear_reaction('<furheart:802746458088013864>')
                await amount.reply(f'cleared (furheart) reaction^ (number {count} out of {total} messages)',delete_after=2)
                count += 1
                
            elif reaction == 'both':
                await amount.clear_reaction('✅')
                await amount.clear_reaction('<furheart:802746458088013864>')
                await amount.reply(f'cleared (furheart and checkmark) reactions^ (number {count} out of {total} messages)',delete_after=2)
                count += 1
                
            else:
                ctx.respond('{option -> reaction must be checkmark, furheart, or both.')
                
    @commands.command(name='heh')
    async def heh(self, ctx, nerdz, nerdz2):
        await ctx.send('heh cute')

    @commands.slash_command(name="homebrewapproved", guild_ids=config)
    async def hbapproval(self, ctx, messagecount: int = None):
        if messagecount is None:
            messagecount = 10
            await ctx.send(f"Since A value wasnt supplied for the message count I will be reverting to the default {messagecount} messages.", ephemeral=True)
        else:
            await ctx.send(f"Running Command for {messagecount} messages.", ephemeral=True)
        msgs = [message async for message in ctx.channel.history(limit=messagecount)]
        for messagecount in msgs:
            for reaction in messagecount.reactions:
                if reaction.emoji == '✅':
                    print(Fore.GREEN + f'[✓] Checkmark Detected in {messagecount.id}')
                    await messagecount.add_reaction('<furheart:802746458088013864>')
                    await messagecount.reply('checkmark here^', delete_after=5)
                    break


def setup(bot):
    bot.add_cog(events(bot))
