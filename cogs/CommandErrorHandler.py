"""
If you are not using this inside a cog, add the event decorator e.g:
@bot.event
async def on_command_error(ctx, error)

For examples of cogs see:
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be

For a list of exceptions:
https://disnakepy.readthedocs.io/en/latest/ext/commands/api.html#exceptions
"""
import disnake
import traceback
import sys
from disnake.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.

        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, disnake.ext.commands.MissingRequiredArgument):
            embed = disnake.Embed()
            embed.title = f'Error'
            embed.add_field(name='Error Location', value=f'`{ctx.command}`', inline=False)
            embed.description = f'A missing argument was missing in {ctx.command}. Please run the command again but including the missing argument'
            embed.add_field(name='Type of Error', value=f'`Missing argument: {error.param}`', inline=False)
            embed.add_field(name='Correct Usage', value=f"`{ctx.prefix} {ctx.command.name} {ctx.command.signature}`", inline=False)
            embed.set_footer(text='An Exception has occured ... Details Above.')
            await ctx.send(embed=embed)
            return

        if isinstance(error, disnake.ext.commands.errors.NotOwner):
            embed = disnake.Embed()
            embed.title = f"Error"
            embed.add_field(name='Error Location', value=f'{ctx.command}', inline=True)
            embed.description = f"Hey {ctx.author.name}! You do not have permission to run this command. You do not own this bot."
            embed.set_footer(text="An Exception has occurred ... Details Above.")
            await ctx.send(embed=embed)
            return

        if isinstance(error, disnake.ext.commands.PrivateMessageOnly):
            embed = disnake.Embed()
            embed.title = f"Error"
            embed.add_field(name='Error Location', value=f'{ctx.command}', inline=True)
            embed.description = f"This command is only supported in private messages."
            embed.set_footer(text="An Exception has occurred ... Details Above.")
            await ctx.send(embed=embed)
            return

        if isinstance(error, disnake.ext.commmands.NoPrivateMessage):
            embed = disnake.Embed()
            embed.title = f"Error"
            embed.add_field(name='Error Location', value=f'{ctx.command}',inline=True)
            embed.description = f"This command cannot be executed in private messages."
            embed.set_footer(text="An Exception has occurred ... Details Above.")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')


        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                await ctx.send('I could not find that member. Please try again.')

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    """Below is an example of a Local Error Handler for our command do_repeat"""
"""
    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        A simple command which repeats your input!

        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        A local Error Handler for our command do_repeat.

        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        

        # Check if our required argument inp is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")
"""

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))