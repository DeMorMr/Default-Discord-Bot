# Library for bot
import discord
from discord.ext import commands

intents=discord.Intents.default() # You intents!
intents.message # Bot see message
intents.member # Bot see a member info

Prefix='your prefix!' # Your Prefix

bot = commands.Bot(command_prefix=Prefix, intents=intents) # Bot and intents
# a remove default help👇
# bot.remove_command('help')

# <<Base>>
 # @bot.event
 # @bot.command()


@bot.event # Wow, you started?
async def on_ready():
    print(f'{bot.user.name} started') #duscird.Status. idle,online,offline                                         discord.ActivityType. [playing, watching] The rest is in the documentary
    await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name = f'RickRoll', type = discord.ActivityType.watching)) #Общее количество участников, за которыми следит бот (Находятся на серверах)


# A ctx. function
@bot.command() # send command
async def send(ctx):
    await ctx.send('Ping,Pong!🏓') #send
    
@bot.command() # reply command
async def reply(ctx):
    await ctx.reply('Hi friend!') #reply

# A ctx.author. function
@bot.command()
async def MyName(ctx):
   await ctx.reply(f'Your name {ctx.author.name}!')
   
@bot.command()
async def MentionMe(ctx):
    await ctx.reply(f'{ctx.author.mention} 🤫🧏‍♂️')

# Other function
@bot.command()
async def CreateAndGiveMeRole(ctx, text): 
    role = await guild.create_role(name=f"{text}") # create
    await ctx.author.add_roles(role) # give

@bot.command()
async def joke(ctx,text):
  await ctx.message.delete() # delete author message
  await ctx.send(f'{text}') # The bot writes the user's message

# A FULL EmBed message! UwU
@bot.command()                                                     # <Alternative>
async def UwU(ctx):                                                # discord.Color.from_rgb(0,0,0) # a rgb code
  embed=discord.Embed(title='Title',description='Description', color=discord.Color.black() ) # other color: gold(this yellow), blue 
  
  embed.add_field(name="Field1", value="Desc1", inline=False) # inline=False this fixation field
 # embed.add_field(name="Field2", value="Desc2", inline=False)
 # embed.add_field(name="Field3", value="Desc3", inline=False)
  
 # embed.set_thumbnail(url = 'URL_IMAGE')
 # embed.set_image(url = 'URL_IMAGE')
  
  embed.set_author(name='WoOOooW')
  embed.set_footer(text=f"iM A SuPEr Man!")
  
  await message.channel.send(embed=embed)

# Hyperlink
@bot.command()
async def FreeDiscordNitro(ctx):
   await ctx.reply('[press!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)')


# Create a token.txt witch token
token = open('token.txt').readline()
bot.run(token)
