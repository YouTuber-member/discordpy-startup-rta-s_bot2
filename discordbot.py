import os
import traceback
import random
from discord.ext import commands as rta
from cog_basic import Basic
from cog_greet import Greet


bot = rta.Bot(command_prefix='$')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(name="ping")
async def ping(ctx):
        await ctx.send('pong')

@bot.command(name="dice")
async def dice(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    msg = f"{ctx.author.mention}\n" + result 
    await ctx.send(msg)



#class JapaneseHelpCommand(commands.DefaultHelpCommand):
#   def __init__(self):
#        super().__init__()
#        self.commands_heading = "コマンド:"
#        self.no_category = "その他"
#        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"
#
#    def get_ending_note(self):
#        return (f"各コマンドの説明: $help <コマンド名>\n"
#                f"各カテゴリの説明: $help <カテゴリ名>\n")
#

bot.add_cog(Greet(bot=bot))
bot.add_cog(Basic(bot=bot))

bot.run(token)
