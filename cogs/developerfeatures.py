import disnake
from disnake.ext import commands
from colorama import Fore, Back, Style
def setup(bot):
    bot.add_cog(developerfeatures(bot))
class developerfeatures(commands.Cog):
    """Useful Features for Bot Development."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Loading Developer Features cog')
# code for optional intergers
# async def func(ctx, optional_arg: int=0)


    @commands.command(name='ggemoji', description='This Command Returns a list of Emojis for the Guild(Server) it is Run within.')
    async def gemoji(self, ctx, optional_arg: int = None):
     guild = int
     print(f"Guild output before check  ++ {guild}")
     if guild == None:
     	guild = ctx.get_guild()
     	print ( Fore.CYAN + '[DEBUG]' + Fore.YELLOW + 'Detected No Guild Input')
     	ctx.send('Debug: Guild is equal to None', delete_after=5)
     await ctx.send(ctx.guild.emojis)
     print (ctx.guild.emojis)