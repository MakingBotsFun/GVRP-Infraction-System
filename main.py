import nextcord
from nextcord.ext import commands
import keep_alive
keep_alive.keep_alive()

client = commands.Bot(command_prefix="gvrp!")

raidnotifychannel = client.get_channel(974004033851371540)

@client.event
async def on_ready():
  await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"command execution"))

@client.listen()
async def on_message(message):
  if message.content.startswith("@everyone"):
    await message.delete()
    member = message.author
    embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
    await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@974004358909952070>")
    await member.send(embed=embed)
    await member.ban()    
    
  if message.content.startswith("@here"):
    await message.delete()
    member = message.author
    embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
    await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@974004358909952070>")
    await member.send(embed=embed)
    await member.ban()
  else:
    if len(message.mentions) > 7:
     await message.delete()
     embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
     member = message.author
     await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@974004358909952070>")
     await member.send(embed=embed)
     await member.ban()
    

@application_checks.has_role(964618093236219924)  
@client.slash_command(description="Strike someone!")
async def strike(interaction : nextcord.Interaction, member : nextcord.Member, reason : str):
  await member.send(f"You have been striked by {ctx.author.mention}. Infraction reason: \n \n {reason}")
  await interaction.send(f"Success! \n Infraction reason: {reason}", ephemeral=True)


client.run("TOKEN_HERE")
