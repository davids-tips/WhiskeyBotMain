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
    @disnake.ext.commands.is_owner()
    async def logoff(self, inter):
        await inter.send('ATTENTION: Bot is Logging off')
        await self.bot.close()
        print('Bot Logged Off')
        await exit()

    @commands.command(name='ggemoji',
                      description='This Command Returns a list of Emojis for the Guild(Server) it is Run within.')
    async def gemoji(self, ctx, optional_arg: int = None):
        guild_opt = optional_arg
        print(f"Guild output before check  ++ {guild_opt}")
        if guild_opt is None:
            guild = ctx.get_guild()
            print(Fore.CYAN + '[DEBUG]' + Fore.YELLOW + 'Detected No Guild Input')
            ctx.send('Debug: Guild is equal to None', delete_after=5)
            await ctx.send(ctx.guild.emojis)
            print(ctx.guild.emojis)
        else:
            print(Fore.CYAN + '[DEBUG]' + Fore.YELLOW + 'Detected Guild Input')
            await ctx.send('Debug: Guild is equal to None', delete_after=5)
            await ctx.send(ctx.guild.emojis)
            print(ctx.guild.emojis)
