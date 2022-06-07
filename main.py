import nextcord
from nextcord.ext import commands
import keep_alive
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import application_checks
keep_alive.keep_alive()

client = commands.Bot(command_prefix="gvrp!")


@client.event
async def on_ready():
  await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"command execution"))

@client.listen()
async def on_message(message):
  if message.author.id == 961699072140521553:
    return
  else:
    if message.author.id == 851206490638254152:
      return
    else:
      if message.content.startswith("@everyone"):
        await message.delete()
        member = message.author
        raidnotifychannel = client.get_channel(974004033851371540)
        embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
        await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raid type: @everyone ping \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@&974004358909952070>")
        await member.send(embed=embed)
        await member.ban()    
    
  if message.content.startswith("@here"):
    await message.delete()
    member = message.author
    raidnotifychannel = client.get_channel(974004033851371540)
    embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
    await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raid type: @here ping \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@&974004358909952070>")
    await member.send(embed=embed)
    await member.ban()
  else:
    if len(message.mentions) > 7:
     await message.delete()
     embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
     member = message.author
     raidnotifychannel = client.get_channel(974004033851371540)
     await raidnotifychannel.send(f"Hey! A raid might have occured in the server. Please check the server. \n Raid type: Over 7 people pinged \n Raider: {member.mention} \n Raider ID: {member.id} \n Ping: <@&974004358909952070>")
     await member.send(embed=embed)
     await member.ban()
    


@application_checks.has_role(964618093236219924)  
@client.slash_command(description="Strike someone!")
async def strike(interaction : nextcord.Interaction, member : nextcord.Member, reason : str):
  await member.send(f"You have been striked by {ctx.author.mention}. Infraction reason: \n \n {reason}")
  await interaction.send(f"Success! \n Infraction reason: {reason}", ephemeral=True)



client.run("TOKEN_HERE")
