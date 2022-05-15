import disnake
from disnake.ext import commands
from colorama import Fore, Back, Style
def setup(bot):
    bot.add_cog(events(bot))
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
