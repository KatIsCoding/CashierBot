import discord
from discord.ext import commands
from updateconf import updatenow
import json
from sharedcommands import *

TOKEN = ""
bot = commands.Bot(command_prefix="#", help_command=None)

guser = ""
gamount = ""
author = ""
owner = ""
user = ""



def getAmount(serverid, amount, currency):
    with open("storage.json","r") as storage:
        data = json.load(storage)
    feepercent = data[serverid]["fee"]
    amount= amount.replace(",","")
    #amount= amount.replace(",","")
    if currency == 0:
        amount = float(amount)
        x = float((amount*feepercent) / 100) #Default 100
        realamount = float((amount - x) / 100)
        print(round(realamount))
        return round(realamount,3)
    elif currency == 1:
        amount = float(amount) * 100000
        x = float((amount*feepercent) / 100) #Default 100
        realamount = float((amount - x) / 100)
        print(round(realamount))
        return round(realamount,3)

@bot.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help", description="Prefix: # This are the current available commands and it's usage:", color=0xFFFF00)
    embedVar.add_field(name="update", value="Usage: #update cashier @cashiername or #update fee feeinteger", inline=False)
    embedVar.add_field(name="getconfig", value="Prints the current configuration file", inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def getconfig(ctx):
     
    serverid = str(ctx.message.guild.id)
    try:
        getconf(serverid)
        embedVar = discord.Embed(title="Current Configuration:", description="Prints the current configuration", color=0xFFFF00)
        embedVar.add_field(name="Cashier", value=getconf(serverid)[0], inline=False)
        embedVar.add_field(name="Fee", value=getconf(serverid)[1], inline=False)
        await ctx.send(embed=embedVar)
    except Exception: 
        await ctx.send("ERROR: There is no configuration file for your server, please tell your moderators to use the update command first, see #help for more information")

@bot.command()
async def update(ctx, key, value):
    serverid = str(ctx.message.guild.id)
    
    role = discord.utils.get(ctx.guild.roles, name="Poker Admin")
    if role in ctx.author.roles:
        if updatenow(serverid, key, value):
            with open("storage.json","r") as storage:
                data = json.load(storage)
            embedVar = discord.Embed(title="Configuration", description="Current configuration file", color=0x00ff00)
            embedVar.add_field(name="Cashier", value=data[serverid]["cashier"], inline=False)
            embedVar.add_field(name="Fee", value=data[serverid]["fee"], inline=False)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="Error", description="Please provide a correct fee value", color=0xff0000)
            embedVar.add_field(name="Type", value="An integer between 0-100", inline=False)
            await ctx.send(embed=embedVar)
    else:
        await ctx.send("You don't have Poker Admin role")







@bot.event
async def on_message(message):
    global user
    amount = ""
    await bot.process_commands(message)
    if message.content.startswith("$tip"):
        user = str(message.author.id)
        print(user)
        
    
    if message.author.id == 617037497574359050:    #Check if the message is from tip.cc bot
        serverid = str(message.guild.id)
        with open("storage.json","r") as storage:
            data = json.load(storage)

        if serverid in data:
            data[serverid]["cashier"] = data[serverid]["cashier"].replace("!","")
            if user in message.content and data[serverid]["cashier"] in message.content:
                print("message from the bot")
                print(message.content)
                lstart = message.content.find(data[serverid]["cashier"] + " **") + len(data[serverid]["cashier"] + " **")
                lend = message.content.find("(")
                values = ["satoshi","bit","mBTC"]
    
                for x in values:
                    if x in message.content[lstart:lend]:
                        print("Value: " + x)
                        lend = message.content.find(f" {x}**")
                        amount= message.content[lstart:lend]
                        amount= amount.replace("*","")
                        if x == "satoshi":
                            await message.channel.send(f"!pac <@{user}> {getAmount(serverid, amount, 0)}")
                            print(user)
                        elif x == "mBTC":
                            await message.channel.send(f"!pac <@{user}> {getAmount(serverid, amount, 1)}")
    
    
                
    
    
    
    
    
    
                if "$" in message.content[lstart:lend]:
                    print("Value: $")
                    lstart = message.content.find(" **")
                    lend = message.content.find("**).")
                    values = ["satoshi","bit","mBTC"]
                    amount = ""
                    for x in values:
                        if x in message.content[lstart:lend]:
                            lend = message.content.find(f" {x}**).")
                            amount= message.content[lstart:lend]
                            amount= amount.replace("*","")
                            await message.channel.send(f"!pac <@{user}> {getAmount(serverid, amount, 0)}")
                            if x == "mBTC":
                                lend = message.content.find(f" {x}**).")
                                amount= message.content[lstart:lend]
                                amount= amount.replace("*","")
                                await message.channel.send(f"!pac <@{user}> {getAmount(serverid, amount, 1)}")
    
    
        lstart = ""
        lend = ""



            
        
    

@bot.event
async def on_ready():
    print("Ready")

bot.run(TOKEN)
