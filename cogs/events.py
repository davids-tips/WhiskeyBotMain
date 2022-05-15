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
        print(Fore.GREEN + 'Connected!' + Fore.WHITE)
        print(Fore.GREEN + 'Bot is ready!' + Fore.WHITE)
        print(Fore.CYAN + 'Waiting For Commands' + Fore.WHITE)
        self.bot.get_guild(798726719573065749)
        channel = self.bot.get_channel(798726720181633047)
        await channel.send('Bot Online!')
        embed = disnake.Embed()
        embed.title = f"**Online**"
        embed.set_footer(text="Logging System")
        embed.set_author(name='Bot Status and Information', icon_url=f"{self.bot.user.avatar}")
        embed.description = f"[`{datetime.now().strftime('%b-%d-%Y`] @ [`%I:%M:%S')}`]\n\n" \
                            f"- Bot account: `{self.bot.user.name}`\n" \
                            f"- Bot ID: `{self.bot.user.id}`\n" \
                            f"- Guilds: `{len(self.bot.guilds):,}`\n" \
                            f"- Users: `{len(list(self.bot.get_all_members()))}`\n" \
                            f"- Disnake Version: `{disnake.__version__}`\n" \
                            f"- Loaded Cogs: `{list(self.bot.cogs)}`\n"  \
                            f"- Developer: `whiskeythefox#7339`\n" \


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
