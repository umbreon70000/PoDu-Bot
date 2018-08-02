import discord
import asyncio
import random
import sqlite3
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------------")

@client.event
async def on_message(message):
    ################
    ##### HELP #####
    ################

    ##################
    ##### LEVELS #####
    ##################
    if message.content.startswith(',deoxys-a'):
        await client.send_message(message.channel, "`Psycho Boost - This is one of the most reliable White Attacks in Duel`")
    if message.content.startswith(',cobalion'):
        await client.send_message(message.channel, "`Sword of Justice - Cobalion usually needs to hit its highest damage move as opposed to its Gold, especially when it is used with Steel Energy`")
    if message.content.startswith(',tapu-koko'):
        await client.send_message(message.channel, "`Melemele Wish -Tapu Koko is not often used to defeat figures, so it is usually best that it is able to survive`")
    if message.content.startswith(',dialga'):
        await client.send_message(message.channel, "`Roar of Time - Highest damage move and counters Twin Dragons`")
    if message.content.startswith(',lugia'):
        await client.send_message(message.channel, "`Cyclone - Lugia's other moves are weak and are unable to compete with meta figures. Cyclone is a very powerful Purple Move, and its effect is also very strong`")
    if message.content.startswith(',hooh'):
        await client.send_message(message.channel, "`Rainbow Wing - Ho-Oh is usually used for its ability, which revives figures in the PC. Rainbow Wing often will give it positional advantage, however sometimes it may do the opposite.`")
    if message.content.startswith(',tauros'):
        await client.send_message(message.channel, "`Take Down - The purple is also an option, however the purple allows the opponent to choose where to move, which could sometimes help them.`")
    if message.content.startswith(',blaziken'):
        await client.send_message(message.channel, "`Flare Blitz and Cyclone Kick - Both of these moves are very powerful, and if this Pokemon has evolved from Combusken, these moves become even more powerful. Sometimes you will want Blaziken to hit Purple, and other times White, so I would suggest at level 10 having 5 points on Flare Blitz and 4 points on Cyclone Kick.`")
    if message.content.startswith(',kyogre'):
        await client.send_message(message.channel, "`Hydro Pump - Kyogre will usually only be used in a Manaphy Deck, and with the damage buff from Manaphy, this move can Deal 150 damage, which can defeat most figures in meta.`")
    if message.content.startswith(',charizard'):
        await client.send_message(message.channel, "`Fire Spin - This Pokemon is usually used for high damage output from its repeated move.`")
    if message.content.startswith(',palkia'):
        await client.send_message(message.channel, "`Spacial Rend - Highest damage move and its effect can sometimes be useful.`")
    if message.content.startswith(',feraligatr'):
        await client.send_message(message.channel, "`Hydro Pump - This Pokemon will usually be used as an evolution from Crocnaw in a Water Deck, and this move's damage is extremely high with both of these buffs.`")
    if message.content.startswith(',darkrai'):
        await client.send_message(message.channel, "`Dark Void - This move works well with Darkrai's ability.`")
    if message.content.startswith(',smash'):
        await client.send_message(message.channel, "`Highest damage move. Break Energy is also an option as it counters decks which rely on Energy Plates.`")
    if message.content.startswith(',venusaur'):
        await client.send_message(message.channel, "`Solar Beam - Usually, this Pokemon needs to survive in Poison Decks, and since this move provides high damage output, Solar Beam is the best move to level up.`")
    if message.content.startswith(',mewtwo'):
        await client.send_message(message.channel, "`Psychic Shove - This move is a very powerful Purple Move, which can often be used to displace the opponent's defence.`")
    if message.content.startswith(',blastoise'):
        await client.send_message(message.channel, "`Hydro Pump - Adding to its Purple Move means that when it is paralysed, it can only beat One Star Purple Moves.`")
    if message.content.startswith(',mew'):
        await client.send_message(message.channel, "`Hyper Sonic or Shuttle Flip - Hyper Sonic is one of the most useful and reliable Gold Moves in Duel, however with the addition of Solgaleo, levelling up Shuttle Flip may be the better option.`")
    if message.content.startswith(',rayquaza'):
        await client.send_message(message.channel, "`Extremespeed - This is the most powerful Gold Move in Duel, and will defeat most moves your opponent uses.`")
    if message.content.startswith(',zygarde'):
        await client.send_message(message.channel, "`Land's Wrath - Usually you will not use this Pokemon with many other Purple attackers, or you will use its Plate alongside it, therefore Land's Wrath is the best option.`")
    if message.content.startswith(',snorlax'):
        await client.send_message(message.channel, "`Body Slam - Highest damage move and its purple also causes itself to sleep.`")
    if message.content.startswith(',keldeo'):
        await client.send_message(message.channel, "`You're actually levelling up Keldeo? Hydro Kick - The Bench effect can sometimes be useful`")
    if message.content.startswith(',giratina'):
        await client.send_message(message.channel, "`Shadow Claw - Highest damage move.`")
    if message.content.startswith(',xerneas'):
        await client.send_message(message.channel, "`Geomancy - Adding to Geomancy makes it more likely that Xerneas will deal a high amount of damage.`")
    if message.content.startswith(',yveltal'):
        await client.send_message(message.channel, "`Oblivion Wing - This move deals a high amount of damage, and with a buff from Dark Mist, this can continue increasing. Levelling up Dark Mist is also an option to try for the high damage, however I find that Oblivion Wing is most reliable`")
    if message.content.startswith(',chesnaught'):
        await client.send_message(message.channel, "`Spiky Shield - Displacement of the opponent's defence.`")
    if message.content.startswith(',swampert'):
        await client.send_message(message.channel, "`Tractor - This move is a fairly good Blue, which can often be used to displace the defence of your opponent.`")
    if message.content.startswith(',greninja'):
        await client.send_message(message.channel, "`Water Shuriken - With this Pokemon, you usually want its damage output to be fairly high from its Repeater Move, and this move also has the advantage of being Gold.`")
    if message.content.startswith(',electivire'):
        await client.send_message(message.channel, "`Electric Blast - Electivire is usually only used to Paralyse multiple Pokemon (if I'm honest, Electivire isn't used, but I had to write something)`")
    if message.content.startswith(',rhyperior'):
        await client.send_message(message.channel, "`Bulldozer - This is probably one of the best Blue Moves in Duel, if not the best. It forces the opponent to have to defend their Goal while Rhyperior is on the Board (unless they run Terrakion).`")
    if message.content.startswith(',garchomp'):
        await client.send_message(message.channel, "`Double Flight - This move allows it to move around the Board quickly.`")
    if message.content.startswith(',empoleon'):
        await client.send_message(message.channel, "`Ice Beam or Hydro Pump - I personally like to Freeze opposing figures using Empoleon, however Hydro Pump has a much higher damage output than Ice Beam, which is useful for Manaphy and Steel Decks.`")
    if message.content.startswith(',lucario'):
        await client.send_message(message.channel, "`Aura Sphere - This Pokemon will usually be used in a Steel Deck with Cobalion, so increasing Aura Sphere allows it to get a KO fairly easily, especially when this Pokemon is next to Cobalion.`")
    if message.content.startswith(',aggron'):
        await client.send_message(message.channel, "`Iron Tail - This move is extremely powerful in a Steel Deck. Heavy Slam is also an option as it counters all runners, however I prefer it being able to defeat 2MP figures easily as well.`")
    if message.content.startswith(',infernape'):
        await client.send_message(message.channel, "`Drive Kick - This move can sometimes get a win on its own since it allows Infernape to go to the Goal.`")
    if message.content.startswith(',gardevoir'):
        await client.send_message(message.channel, "`Warp Hole - This purple move can often be annoying for your opponent since it can often give you a positional advantagee`")
    if message.content.startswith(',deoxys-s'):
        await client.send_message(message.channel, "`Dodge - This Pokemon usually needs to survive, so its Blue move is generally the best one to increase`")
    if message.content.startswith(',deoxys-n'):
        await client.send_message(message.channel, "`Psycho Boost - Teleport is a very good purple, and is often useful for getting cheese wins, however Teleport makes it weak to Mew, and Deoxys N is usually used to counter Mew.`")
    if message.content.startswith(',manaphy'):
        await client.send_message(message.channel, "`Manaphy's Song - This move allows it to gain positional advantage when used alongside other Water Type Pokemon. The low damage of Bubble means that Bubble is very rarely useful for Manaphy.`")
    if message.content.startswith(',heatran'):
        await client.send_message(message.channel, "`Magma Slide - This move works very well longside Heatran's ability, and is also a reliable way of causing the Burn Status.`")
    if message.content.startswith(',deoxys-d'):
        await client.send_message(message.channel, "`Counter - This is the only move Deoxys-D has which can KO its opponents. However, if this Pokemon is being used in a Cobalion Sandwich Deck, its Purple Move would be a better option.`")
    if message.content.startswith(',torterra'):
        await client.send_message(message.channel, "`Earthquake - This move is its highest damaging move, and can often KO multiple Pokemon (however, sometimes it can KO your own team).`")
    if message.content.startswith(',suicune'):
        await client.send_message(message.channel, "`Sheer Cold - This Pokemon is usually used to banish Frozen Pokemon, however even when it does not have this role, the Purple is still an instant KO.`")
    if message.content.startswith(',zekrom'):
        await client.send_message(message.channel, "`Fusion Bolt - Zekrom is usually used alongside Reshiram, Tapu Koko and Overdrive, and with these buffs, Zekrom has possibly the most powerful banishing move in Duel.`")
    if message.content.startswith(',raikou'):
        await client.send_message(message.channel, "`Thunderous Blow or Thunder - Thunderous Blow is a fairly powerful Gold Move, especially when it is used with Tapu Koko. This move can also cause multiple Pokemon to become paralysed. Thunder provides a very high damage output when used with Tapu Koko, which can beat many figures in meta.`")
    if message.content.startswith(',latios'):
        await client.send_message(message.channel, "`Luster Purge - Highest damage move.`")
    if message.content.startswith(',genesect'):
        await client.send_message(message.channel, "`Techno Blast - This Pokemon is usually used for elimination, and this is the move which causes the elimination.`")
    if message.content.startswith(',latias'):
        await client.send_message(message.channel, "`Fly Away or Mist Ball - Usually, this Pokemon is used to rush, and Fly Away is useful for this deck. On the other hand, Mist Ball can deal a lot of damage.`")
    if message.content.startswith(',entei'):
        await client.send_message(message.channel, "`Sacred Fire - This move deals a fairly high amount of damage, and makes the opponent burnt if Entei is KO'd.`")
    if message.content.startswith(',delphox'):
        await client.send_message(message.channel, "`Don't level it up at all. You usually want it to miss so that it can activate its ability.`")
    if message.content.startswith(',typhlosion'):
        await client.send_message(message.channel, "`Fire Blast - When there are two Pokemon in the PC, this move has a fairly high damage output for a 3MP figure.`")
    if message.content.startswith(',reshiram'):
        await client.send_message(message.channel, "`Fusion Flare - Fairly reliable elimination move. Blue Flare could also be chosen for the high damage output.`")
    if message.content.startswith(',magmortar'):
        await client.send_message(message.channel, "`Flare Gun - Instant KO move on two Pokemon.`")
    if message.content.startswith(',zapdos'):
        await client.send_message(message.channel, "`Thunder Crash - This is a very high damage Gold Move, and is also a lot more reliable than many other Gold Moves.`")
    if message.content.startswith(',moltres'):
        await client.send_message(message.channel, "`Crushing Flames - This move is a reliable 110 damage move, which can often defeat meta figures.`")
    if message.content.startswith(',articuno'):
        await client.send_message(message.channel, "`Ice Charge - This is possibly the best move to Freeze Pokemon in the game, and since Freeze is the best status, I would suggest levelling up this move`")
    if message.content.startswith(',dragonite'):
        await client.send_message(message.channel, "`Dragon Tail - When this Pokemon  has evolved from Dratini, this move can deal 110 damage and also has a Bench effect, which makes it a fairly powerful move.`")
    if message.content.startswith(',sceptile'):
        await client.send_message(message.channel, "`Leaf Blade - This move can deal a potential 140 damage, which can defeat most figures in meta, and you usually want to have the best probability of hitting this 140.`")
    if message.content.startswith(',seismitoad'):
        await client.send_message(message.channel, "`Dodge - You usually want this figure to survive so it can poison as many Pokemon as possible. Also, make sure you only add to the Dodge which will not cause it to miss when it is confused.`")
    if message.content.startswith(',terrakion'):
        await client.send_message(message.channel, "`Stone Edge - Highest damage move.`")
    if message.content.startswith(',virizion'):
        await client.send_message(message.channel, "`Typhoon Slash - This can allow Virizion to often get easy wins against Pokemon defending the Goal.`")
    if message.content.startswith(',malamar'):
        await client.send_message(message.channel, "`Psycho Cut - This Pokemon usually needs to cause the highest amount of damage it can, and sine Tapu Koko hard counters the Sleep Status, it is best to choose its White Move.`")
    if message.content.startswith(',trevenant'):
        await client.send_message(message.channel, "`Manipulative - This move allows it to displace opposing Pokemon, and has very good synergy with its ability.`")
    if message.content.startswith(',gourgeist'):
        await client.send_message(message.channel, "`Trick Or Treat - This move makes it easier for your Pokemon to move around the board, and has very good synergy within a Phantom Deck`")
    if message.content.startswith(',noivern'):
        await client.send_message(message.channel, "`Boomburst - The instant KO effect of this move can often be very useful for this Pokemon.`")
    if message.content.startswith(',vikavolt'):
        await client.send_message(message.channel, "`Zap Cannon - This move can paralyse multiple opposing Pokemon, and is also its highest damaging move.`")
    if message.content.startswith(',magnezone'):
        await client.send_message(message.channel, "`Flash Cannon - When evolved, this move can deal an extremely high amount of damage, especially when used alongside Tapu Koko and Steel Energy.`")
    if message.content.startswith(',solgaleo'):
        await client.send_message(message.channel, "`Sunsteel Stike - This is a fairly powerful move which will also KO its opponentn when Solgaleo is KO'd.`")
    if message.content.startswith(',tapu-lele'):
        await client.send_message(message.channel, "`Psyshock - Since its other two moves aren't powerful, this is probably the best option for Tapu Lele.`")
    if message.content.startswith(',Lunala'):
        await client.send_message(message.channel, "`Psychic - This move has very good synergy with its ability, and is not weak to Gold. On the other hand, it makes Lunala very weak when it has a status effect, and for this reason Moongheist Beam is also an option.`")
    if message.content.startswith(',gengar'):
        await client.send_message(message.channel, "`Night Shade - This is a move which can deal a fairly high amount of damage.`")
    if message.content.startswith(',chandelure'):
        await client.send_message(message.channel, "`Inferno - Possibly the most reliable 110 damage move, which also causes its opponent to be burnt.`")
    if message.content.startswith(',decidueye'):
        await client.send_message(message.channel, "`Spirit Shackle - This moe deals a high amount of damage, especially when it has evolved, and it also gives a high amount of Wait (5).`")
    if message.content.startswith(',incineroar'):
        await client.send_message(message.channel, "`Darkest Lariat - This move has a very high damage output, and also has a fairly useful bench effect, which can often disturb opposing defences.`")
    if message.content.startswith(',tapu-bulu'):
        await client.send_message(message.channel, "`Full Swing - This move deals a high amount of damage and can cause problems for the opponent's positioning.`")
    if message.content.startswith(',primarina'):
        await client.send_message(message.channel, "`Balloon Flight - This move prevents Primarina from being KO'd on its next turn, in other words, Primarina's next battle is a free battle.`")
    if message.content.startswith(',tapu-fini'):
        await client.send_message(message.channel, "`Poni Wish - Poni Wish allows Fini to exclude a figure that your opponent may rely on, which usually gives you the advantage.`")
    if message.content.startswith(',groudon'):
        await client.send_message(message.channel, "`Smash - Highest damage move`")
    if message.content.startswith(',metagross'):
        await client.send_message(message.channel, "`Hyper Beam - This move has one of the highest damage outputs in the game. Even though it may sometimes give the opponent another turn, this move's power makes up for that.`")
    if message.content.startswith(',lunala'):
        await client.send_message(message.channel, "`Psychic - When this figure has reached the maximum amount of Clvls, this move will defeat most figures in meta, and will prevent it from being too weak to Gold moves.`")
    if message.content.startswith(',scizor'):
        await client.send_message(message.channel, "`Crushing Squeeze - This is the highest damage move, so has synergy with Steel Energy. Additionally, this move holds the best synergy with Scizor's ability.`")
    if message.content.startswith(',magearna'):
        await client.send_message(message.channel, "`Fleur Cannon - This is the highest damage move, therefore has good synergy with Steel Energy.`")

#############################################
##################Funny Commands#############
#############################################
    if message.content.startswith(',cosmo'):
        await client.send_message(message.channel, "Broken")
    if message.content.startswith(',car'):
        await client.send_message(message.channel, "Yes, I will provide pictures of cars for you soon Sfpm")
    if message.content.startswith(',food'):
        await client.send_message(message.channel, "If only Umbreon could type...")
    if message.content.startswith(',test'):
        await client.send_message(message.channel, "Test")



################################################
######################Games#####################
################################################
    if message.content.startswith(',rock'):
        comp = random.randint(0,2)
        compChose = ""
        result = ""
        if comp == 0:
            compChose = "Rock"
            result = "I chose Rock. It's a draw!"
            await client.send_message(message.channel, result)
        if comp == 1:
            compChose = "Paper"
            result = "I chose Paper. You Lose!"
            await client.send_message(message.channel, result)
        if comp == 2:
            compChose = "Scissors"
            result = "I chose Scissors. You win!"
            await client.send_message(message.channel, result)

    if message.content.startswith(',paper'):
        comp = random.randint(0,2)
        compChose = ""
        result = ""
        if comp == 0:
            compChose = "Rock"
            result = "I chose Rock. You win!"
            await client.send_message(message.channel, result)
        if comp == 1:
            compChose = "Paper"
            result = "I chose Paper. It's a draw!"
            await client.send_message(message.channel, result)
        if comp == 2:
            compChose = "Scissors"
            result = "I chose Scissors. You lose!"
            await client.send_message(message.channel, result)

    if message.content.startswith(',scissors'):
        comp = random.randint(0,2)
        compChose = ""
        result = ""
        if comp == 0:
            compChose = "Rock"
            result = "I chose Rock. You Lose!"
            await client.send_message(message.channel, result)
        if comp == 1:
            compChose = "Paper"
            result = "I chose Paper. You Win!"
            await client.send_message(message.channel, result)
        if comp == 2:
            compChose = "Scissors"
            result = "I chose Scissors. It's a draw!"
            await client.send_message(message.channel, result)


    if message.content.startswith(',ask'):
        number = random.randint(0,8)
        resp = ""
        if number == 0:
            resp = "`Definitely!`"
            await client.send_message(message.channel, resp)
        if number == 1:
            resp = "`Not a chance.`"
            await client.send_message(message.channel, resp)
        if number == 2:
            resp = "`Not looking good.`"
            await client.send_message(message.channel, resp)
        if number == 3:
            resp = "`Positive outlook.`"
            await client.send_message(message.channel, resp)
        if number == 4:
            resp = "`I have no idea. Ask again.`"
            await client.send_message(message.channel, resp)
        if number == 5:
            resp = "`Probably.`"
            await client.send_message(message.channel, resp)
        if number == 6:
            resp = "`Yes.`"
            await client.send_message(message.channel, resp)
        if number == 7:
            resp = "`No.`"
            await client.send_message(message.channel, resp)
        if number == 8:
            resp = "`It is not likely.`"
            await client.send_message(message.channel, resp)

    if message.content.startswith(',howmany'):
        amountHowMany = random.randint(0,100)
        await client.send_message(message.channel, amountHowMany)

##########################################
###############Event Duration#############
##########################################
    if message.content.startswith(',time'):
        t = datetime.utcnow()
        s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
        utcTime = s[:-7] #Removing the milliseconds
        await client.send_message(message.channel, utcTime)

    if message.content.startswith(',event'):
        utcTime = datetime.utcnow()
        s = utcTime.strftime('%Y-%m-%d %H:%M:%S.%f')
        newUtc = s[:-7] #Removing the milliseconds
        strUtc = str(newUtc)
        eventTime = '2018-08-07 07:59:00' #This is the time when the event ends, the one I change
        FMT = '%Y-%m-%d %H:%M:%S'
        if eventTime > strUtc:
            tdelta = datetime.strptime(eventTime, FMT) - datetime.strptime(strUtc, FMT)
        else:
            tdelta = "`There is currently no event.`"
        await client.send_message(message.channel, tdelta)

    if message.content.startswith(',month'):
        utcTime = datetime.utcnow()
        s = utcTime.strftime('%Y-%m-%d %H:%M:%S.%f')
        newUtc = s[:-7] #Removing the milliseconds
        strUtc = str(newUtc)
        eventTime = '2018-08-31 14:59:59'
        FMT = '%Y-%m-%d %H:%M:%S'
        if eventTime > strUtc:
            tdelta = datetime.strptime(eventTime, FMT) - datetime.strptime(strUtc, FMT)
        else:
            tdelta = "`Month reset.`"
        await client.send_message(message.channel, tdelta)

    if message.content.startswith(',maint'):
        utcTime = datetime.utcnow()
        s = utcTime.strftime('%Y-%m-%d %H:%M:%S.%f')
        newUtc = s[:-7] #Removing the milliseconds
        strUtc = str(newUtc)
        maintStart = '2018-06-01 02:00:00'
        maintTime = '2018-06-01 08:00:00'
        FMT = '%Y-%m-%d %H:%M:%S'
        if maintStartTime > strUtc:
            tdelta = datetime.strptime(maintTime, FMT) - datetime.strptime(strUtc, FMT)
        else:
            tdelta = "`There is no maintenance.`"
        await client.send_message(message.channel, tdelta)


##########################################
###############Credit System##############
##########################################

    if message.content.startswith(',myname'):
        myname = message.author.name
        await client.send_message(message.channel, myname)



client.run('Mzg5MDAxNzU0MDMwNzY4MTMw.DSxZTA.08-i9eiBCO0Y2E3JTvVajQY1mO4')
