import discord
import sys

amount = sys.argv

TOKEN = "ODAxMjQ0NzMwOTE3OTEyNjA2.YAd3Tg.m8KweYQb0y0d0YxAN_i6VKwxVoQ"
bot = discord.Client()



@bot.event
async def on_ready(ctx):
	global amount
	await bot.get_channel(801242591421005835).send(f"$tip @cashier {amount}")
	

	


bot.run(TOKEN)
