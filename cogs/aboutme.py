import disnake
from disnake.ext import commands
from datetime import datetime
import time
from wb import config
from colorama import Fore


class aboutme(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print(Fore.CYAN + 'Loading About Me cog' + Fore.WHITE)

    @commands.slash_command(name='info', description='Tells you about myself.')
    async def info(self, inter):
        embed = disnake.Embed()
        embed.title = 'About Me UwU'
        embed.set_footer(text='❤ Made with Love ❤')
        embed.set_author(name=f'{self.bot.user.name}', icon_url=f'{self.bot.user.avatar}')
        embed.description = f"""
        eeeeee
    """
        await inter.send(embed=embed)

    @commands.slash_command(name='permissions')
    async def permissions(self, inter):
        permissions_list = inter.me.guild_permissions
        permslist = []
        perm = ['administrator','view_audit_log','attach_files']
        for perm in permissions_list:
            if perm in inter.me.guild_permissions:
                print(perm[0])

    @commands.slash_command(name='test', guild_ids=config)
    async def permissions(self, inter, heh):
        """Look into embed fields for adding the permissions
           into the embed since you can add fields later on"""
        embed = disnake.Embed()
        embed.title("Bot Permissions")
        embed.set_footer('❤ Made with Love ❤')
        embed.description('e')
        message = await inter.channel.send(embed=embed)
        time.sleep(2)
        new_embed = message.embed[0]  # Message.embeds returns a list, so just index the first element
        new_embed.description += "UwU"
        time.sleep(2)
        new_embeded = message.embed[0]
        new_embeded.description += f"heh"
        await message.edit(embed=new_embed)



        """
        for i in list:
            print(f'{i}')
            perm = i.replace("'", '')
            print(inter.me.permission_list)
            print(perm)
            print(inter.me.guild_permissions)
            print()
          #  print(f'{inter.me.guild_permissions.i}')

        if permissions.add_reactions is True:
            return
"""


def setup(bot):
    bot.add_cog(aboutme(bot))
