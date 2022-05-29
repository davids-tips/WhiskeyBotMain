import disnake
from disnake.ext import commands
from cogs.listvar import scritch
import json


def setup(bot):
    bot.add_cog(embd(bot))

class embd(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading embed cog')

@commands.command(name='attachment', description='lists messages attachments url')
async def attachment(self, ctx):
            print(f'{ctx.author.name} initiated message attachment command.')
            await ctx.send(f'ctx.message.attachments')
            print(ctx.message.attachments)