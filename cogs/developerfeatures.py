import disnake
from disnake.ext import commands
from colorama import Fore


def setup(bot):
    bot.add_cog(developerfeatures(bot))


class developerfeatures(commands.Cog):
    """Useful Features for Bot Development."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Loading Developer Features cog')

    # code for optional integers
    # async def func(ctx, optional_arg: int=0)

    @commands.command(name='logoff')
    async def logoff(self, ctx):
        await ctx.send('`Bot Is Logging Off`')
        await self.bot.close()
        print('Bot Logged off')

    @commands.command(name='getemojis',
                      description='This Command Returns a list of Emojis for the Guild(Server) it is Run within.')
    async def getemojis(self, ctx, optional_arg: int = None):
        guild = int
        print(f"Guild output before check  ++ {guild}")
        if None == guild:
            guild = ctx.get_guild()
            print(Fore.CYAN + '[DEBUG]' + Fore.YELLOW + 'Detected No Guild Input')
            await ctx.send('Debug: Guild is equal to None', delete_after=5)
        await ctx.send(ctx.guild.emojis)
        print(ctx.guild.emojis)
