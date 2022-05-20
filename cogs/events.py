import disnake
from disnake.ext import commands
from colorama import Fore
from datetime import datetime
import time

# below are two date time functions that have different functions but one of them adds to the other durring startup
start_time = datetime.now()
mytime = time.localtime()
if mytime.tm_hour < 12:
    timeofday = 'AM'
else:
    timeofday = 'PM'

guild_ids = [798726719573065749]
class events(commands.Cog):
    """Useful Features for Bot Development."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Loading Events cog')

    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.GREEN + 'Connected!')
        print('Bot is ready!' + Fore.WHITE)
        print(Fore.CYAN + 'Waiting For Commands' + Fore.WHITE)
        embed = disnake.Embed()
        embed.title = f"**Online**"
        embed.set_footer(text="Logging System")
        embed.set_author(name='WhiskeyBot', icon_url=f"{self.bot.user.avatar}")
        embed.description = f"""**Bot Startup and Information**
        Start Time: `{datetime.now().strftime('%b-%d-%Y at %I:%M:%S')} {timeofday}`
        Current Uptime: <t:{round(datetime.timestamp(start_time))}:R>
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

    @commands.slash_command(name="uptime",description="checks bots uptime", guild_ids=guild_ids)
    async def uptime(self, interaction):
        print("uptime")
        now = datetime.now()
        delta = datetime.now() - start_time
        days, hours, minutes, seconds = delta.days, delta.seconds // 3600, (
                    delta.seconds // 60) % 60, delta.seconds % 60
        await interaction.send(f'Bot has been Online for: `{days} Days {hours} hrs {minutes} mins {seconds} secs`')

    @commands.command(name="ping")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.slash_command(name="ping", description="Checks Bot's Latency", guild_ids=guild_ids)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        print ('Executing ping command via slash')
        
        print(f'{command}')
        await self.bot.send(f'{command}')
        await self.bot.invoke(self.bot.command.get_commands())


    @commands.slash_command(name="ee", description='Check Bots Latency', guild_ids=guild_ids)
    async def pingee(self,inter):
        await inter.response.send_message("Pong!")



def setup(bot):
    bot.add_cog(events(bot))
