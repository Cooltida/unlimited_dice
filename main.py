import random
import logging
import discord
import os
from discord.ext import commands

logging.basicConfig(level=logging.DEBUG)


def dice(sides=6):
    logging.debug("A {} sided dice has been selected".format(sides))
    result = round((random.random() * (sides - 1) + 1))
    logging.debug("The dice show with a {}".format(result))
    return result


def hand(number_of_dice=1, sides=6):
    total = 0
    for i in range(0, number_of_dice):
        current_dice = dice(sides)
        if current_dice == sides:
            total = total + hand(number_of_dice=2, sides=sides)
        else:
            total = total + current_dice
    return total


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="ob", help="!ob 3t6")
async def ob(ctx, input: str):
    try:
        modifier = 0
        number_of_dice, sides = input.split("t")
        if len(sides.split("+")) > 1:
            sides, modifier = sides.split("+")
        if int(sides) < int(2):
            await ctx.send("You think you smart? HACKERMAN!")
            return
        if int(number_of_dice) > 10:
            await ctx.send("Cant do more than 10 dice on this hardware")
            return
        await ctx.send(hand(int(number_of_dice), int(sides)) + int(modifier))
    except:
        await ctx.send("Cant break this!")


bot.run(os.environ.get("DISCORD_TOKEN"))
