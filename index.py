import getpass
from typing import Text
from colorama import Fore, Style
from colorama import init, Fore, Back, Style
from discord import channel
from discord.client import Client
init(convert=True)
import os, time, datetime, random, asyncio, aiohttp, json, discord, time, colorama, requests
from itertools import cycle
from discord import Game, File
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
token = open('./Data/token.txt', 'r').readline()
client = commands.Bot(command_prefix='!')
client.remove_command('help')
os.system('cls')
serverid = 838789505888419841 #replace this with your own server id braindead paster
rainbowrolename = "bot" # this is a rainbow role thing so it changes color every couple seconds making it look cool change if you want xx
delay = 2
colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

@client.event
async def on_ready():
    print("Bot Online :p")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help | !stock | FREE ACCOUNTS: discord.gg/STZJGHKs"))
    import itertools, threading, time, sys
    done = False

@client.event
async def on_ready():
    client.loop.create_task(lolhaha(rainbowrolename))
    banner = f"""
        {Fore.RED};) ██╗  █{Fore.YELLOW}█╗███████{Fore.GREEN}╗███╗   █{Fore.CYAN}█╗███████{Fore.BLUE}█╗ █████╗{Fore.MAGENTA} ██╗ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║██╔════{Fore.GREEN}╝████╗  █{Fore.CYAN}█║╚══██╔═{Fore.BLUE}═╝██╔══██{Fore.MAGENTA}╗██║ :-).
        {Fore.RED};) ██████{Fore.YELLOW}█║█████╗ {Fore.GREEN} ██╔██╗ █{Fore.CYAN}█║   ██║ {Fore.BLUE}  ███████{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██╔══█{Fore.YELLOW}█║██╔══╝ {Fore.GREEN} ██║╚██╗█{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██╔══██{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║███████{Fore.GREEN}╗██║ ╚███{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██║  ██{Fore.MAGENTA} ██║ :-).
        {Fore.RED};) ╚═╝  ╚{Fore.YELLOW}═╝╚══════{Fore.GREEN}╝╚═╝  ╚══{Fore.CYAN}═╝   ╚═╝ {Fore.BLUE}  ╚═╝  ╚═{Fore.MAGENTA}╝╚═╝ :-).
        {Fore.RESET}"""

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help | !stock | FREE ACCOUNTS: discord.gg/STZJGHKs"))
    print(banner)
    print(f'{Fore.RED}        Logged in on {Fore.YELLOW}{client.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{client.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')


@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "Members")
    await ctx.add_roles(role)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="AccGenServ", color=0x109319)
    embed.set_author(name="Rosee", url="https://twitter.com/Rosee__Z", icon_url="https://pbs.twimg.com/profile_images/1386402289905246208/xL-fxxNn_400x400.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/838789549433815110/844584060101853214/45c39eff35bac186329cb8f6f3e50764.png")
    embed.add_field(name="========= gen commands ========", value="Account Gen Options", inline=False) 
    embed.add_field(name="!Stock", value="shows the stock for accounts", inline=False) 
    embed.add_field(name="!Spotify", value="Generates A Spotify Account", inline=False)
    embed.add_field(name="!Hulu", value="Generates A Hulu Account", inline=False)
    embed.add_field(name="!Nitro", value="Generates A Nitro Code", inline=False)
    embed.set_footer(text="AccGen Serv")
    embed.add_field(name="======== proxy's Commands =======", value="Proxy Options", inline=False) 
    embed.add_field(name="!Http", value="Generates Http Proxy List", inline=False)
    embed.add_field(name="!Https", value="Generates Https Proxy List", inline=False)
    embed.add_field(name="!Socks4", value="Generates socks4 Proxy List", inline=False)
    embed.add_field(name="!Socks5", value="Generates socks5 Proxy List", inline=False)
    embed.add_field(name="======== other commands =======", value="Bassically Fun Commands For Nerds", inline=False)
    embed.add_field(name="Gmail Dot Trick", value="Applies Gmail Dot Trick To The Email Given. Useage: !gmail autism@gmail.com")
    embed.add_field(name="!Ad-bypass", value="bypasses ad links", inline=False) 
    embed.add_field(name="========  Admin  Commands  =======", value="Admin Options", inline=False) 
    embed.add_field(name="!Ban @user#1010", value="Bans User", inline=False) 
    embed.add_field(name="!Unban uesr#1010", value="Unbans User", inline=False) 
    ctx.author.display_name
    ctx.author.avatar_url    
    await ctx.send(embed=embed)


@client.command()
async def bypass(ctx, arg):
    r=requests.get('https://adlink-bypass-api.bigbypassalt.repl.co/api?='+arg)
    a = ('%'+r.text)
    chunks = a.split(',')
    dest = chunks[1]
    stripped = dest.split('"')
    embed = discord.embed()
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/838789549433815110/844584060101853214/45c39eff35bac186329cb8f6f3e50764.png")
    embed.add_field(name="Bypassed Link:", value=stripped[3], inline=False)
    await ctx.send(embed=embed)


@client.command()
async def http(ctx):
    f = open("./Data/proxies/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("./Data/proxies/http-proxies.txt"))

@client.command()
async def https(ctx):
    f = open("./Data/proxies/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("./Data/proxies/https-proxies.txt"))

@client.command()
async def socks4(ctx):
    f = open("./Data/proxies/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("./Data/proxies/socks4-proxies.txt"))

@client.command()
async def socks5(ctx):
    f = open("./Data/proxies/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("./Data/proxies/socks5-proxies.txt"))

@client.command()
async def all(ctx):
    f = open("./Data/proxies/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("./Data/proxies/all-proxies.txt"))


@client.command(pass_context=True)
async def stock(ctx):
    spotifystock = sum(1 for line in open('./data/accounts/spotify.txt'))
    nordsstock = sum(1 for line in open('./data/accounts/nord.txt'))
    hulustock = sum(1 for line in open('./data/accounts/hulu.txt'))
    disneystock = sum(1 for lines in open('./data/accounts/disney.txt'))
    Nitrosstock = sum(1 for lines in open('./data/accounts/Nitro Codes.txt'))

    stock=discord.Embed(title="stock", description="AccGenServ", color=0x109319)
    stock.set_author(name="Rosee", url="https://twitter.com/Rosee__Z", icon_url="https://pbs.twimg.com/profile_images/1386402289905246208/xL-fxxNn_400x400.jpg")
    stock.set_thumbnail(url="https://cdn.discordapp.com/attachments/838789549433815110/844584060101853214/45c39eff35bac186329cb8f6f3e50764.png")
    stock.add_field(name="============= stock ============", value="AccGenServ Stock", inline=False) 
    stock.add_field(name="Hulu: ", value=hulustock, inline=False) 
    stock.add_field(name="spotify: ", value=spotifystock, inline=False)
    stock.add_field(name="Disney: ", value=disneystock, inline=False)
    stock.add_field(name="Nord:", value=nordsstock, inline=False)
    stock.add_field(name="Nitro:", value=Nitrosstock, inline=False)
    ctx.author.display_name
    ctx.author.avatar_url    
    await ctx.send(embed=stock)
    
@client.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f"http://extreme-ip-lookup.com/json/%7Bipaddr%7D%27")
    geo = r.json()
    ipnigga = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            ipnigga.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=ipnigga)

@client.command(pass_context=True)
@commands.cooldown(1, 900, commands.BucketType.user)
async def nitro(ctx):
    author = ctx.message.author
    with open('./data/accounts/Nitro Codes.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('./data/accounts/Nitro Codes.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Nitro Code at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

@client.command(pass_context=True)
@commands.cooldown(1, 900, commands.BucketType.user)
async def disney(ctx):
    author = ctx.message.author
    with open('./data/accounts/disney.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('./data/accounts/disney.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Disney Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

@client.command(pass_context=True)
@commands.cooldown(1, 900, commands.BucketType.user)
async def nord(ctx):
    author = ctx.message.author
    with open('./data/accounts/nord.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('./data/accounts/nord.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a NordVpn Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

@client.command(pass_context=True)
@commands.cooldown(1, 900, commands.BucketType.user)
async def spotify(ctx):
    author = ctx.message.author
    with open('./data/accounts/spotify.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('./data/accounts/spotify.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")



@client.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} {exception}")


@client.command(pass_context=True)
@commands.cooldown(1, 900, commands.BucketType.user)
async def hulu(ctx):
    author = ctx.message.author
    with open('./data/accounts/hulu.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('./data/accounts/hulu.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Hulu Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")


@client.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} {exception}")

@client.command(pass_context=True)
async def gmail(ctx, account):
	length = len(account) - 10
	i = 0
	final_str = ""
	while i < 10:
		amount_of_periods = random.randint(0, length - 1)
		period_count = 0
		new_account = account
		index_arr=[]

		while period_count < amount_of_periods:
			index = random.randint(1, length - 1)
			temp_index = index
			if index in index_arr:
				while temp_index in index_arr:
					temp_index = random.randint(1, length - 1)
				index = temp_index
			
			new_account = new_account[:index] + "." + new_account[index:]
			for arr_index, item in enumerate(index_arr):
				if item > index:
					index_arr[arr_index] += 1

			index_arr.append(index)
			print(index_arr)
			period_count += 1

		final_str = final_str + new_account + "\n"
		i+=1

	final_str = remove_duplicates(final_str)

	em = discord.Embed(title="Gmail Generator", description= "", color=0x109319)
	em.add_field(name=account, value=final_str, inline=False)
	await ctx.send(embed=em)
	
def remove_duplicates(string):
    for i, (a, b) in enumerate(zip(string, string[1:])):
        if a == b and a == ".":
            return string[:i] + remove_duplicates(string[i+1:])
    return string

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

async def lolhaha(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(lolhaha(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(lolhaha(rainbowrolename))

client.run(token.strip())
