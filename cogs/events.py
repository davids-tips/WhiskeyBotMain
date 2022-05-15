import disnake
from disnake.ext import commands
from colorama import Fore, Back, Style
from datetime import datetime

start_time = datetime.now()


class events(commands.Cog):
    """Useful Features for Bot Development."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Loading Events cog')

    @commands.Cog.listener()
    async def on_ready(self):
        import time
        mytime = time.localtime()
        if mytime.tm_hour < 12:
            timeofday = 'AM'
        else:
            timeofday = 'PM'
        print(Fore.GREEN + 'Connected!' + Fore.WHITE)
        print(Fore.GREEN + 'Bot is ready!' + Fore.WHITE)
        print(Fore.CYAN + 'Waiting For Commands' + Fore.WHITE)
        self.bot.get_guild(798726719573065749)
        channel = self.bot.get_channel(798726720181633047)
        await channel.send('Bot Online!')
        embed = disnake.Embed()
        embed.title = f"**Online**"
        embed.set_footer(text="Logging System")
        embed.set_author(name='WhiskeyBot', icon_url=f"{self.bot.user.avatar}")
        embed.description = f"""**Bot Startup and Information**
        Start Time: `{datetime.now().strftime('%b-%d-%Y at %I:%M:%S')} {timeofday}`
        Bot account: `{self.bot.user.name}`
        Bot ID: `{self.bot.user.id}`
        Guilds: `{len(self.bot.guilds):,}`
        Users: `{len(list(self.bot.get_all_members()))}`
        Disnake Version: `{disnake.__version__}`
        Loaded Cogs: `{list(self.bot.cogs)}`
        Developer: `whiskeythefox#7339`
        """

        GUILD_ID = 798726719573065749
        CHANNEL_ID = 798726720181633047
        location = self.bot.get_guild(GUILD_ID).get_channel(CHANNEL_ID)
        await location.send(embed=embed)

        pass

    @commands.command(name="uptime")
    async def uptime(self, ctx):
        await ctx.send(f"{datetime.now() - start_time}")


def setup(bot):
    bot.add_cog(events(bot))
