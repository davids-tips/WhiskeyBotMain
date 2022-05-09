import discord
from discord.ext import commands
from cogs.listvar import scritch
import json

def setup(bot):
    bot.add_cog(embd(bot))

class embd(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading embed cog')

@commands.command(name='cmd', description='boop someone', alias=['cmd1','cmd2'])
async def boop(self, ctx):
            print(f'{ctx.author.name} initiated boop command.')
            await ctx.send(f'ctx.message.attachments')
            print(ctx.message.attachments)