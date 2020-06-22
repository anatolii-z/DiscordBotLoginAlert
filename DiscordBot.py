import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot connected')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Наблюдателя'))


@client.command(pass_context=True)
async def hello(ctx, arg):  # команда hello, arg сообщение после команды в 1 слово
    author = ctx.message.author
    await ctx.send(f'{author.mention} ' + arg)  # ответ с упоминанием


token = open('token.txt', 'r').readline()
client.run(token)
