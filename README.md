# TF2 API
A simple tf2 API!<br/>
-----
### Example:
```py
from tf2 import TF2
import getpass4

tf2 = TF2(str(getpass4.getpass('Enter Steam Web API Key: ' , '*')), 123456789012345) # the getpass4 thing is a password thing. You can put a string with the api key there.

scoutk = tf2.get_kills_as_class('Scout')
heavyk = tf2.get_kills_as_class('Heavy')
pyrok = tf2.get_kills_as_class('Pyro')
spyk = tf2.get_kills_as_class('Spy')
medick = tf2.get_kills_as_class('Medic')
sniperk = tf2.get_kills_as_class('Sniper')
soldierk = tf2.get_kills_as_class('Soldier')
engineerk = tf2.get_kills_as_class('Engineer')
demomank = tf2.get_kills_as_class('Demoman')

total_kills = scoutk + heavyk + pyrok + spyk + medick + sniperk + soldierk + engineerk + demomank

print(f"Total Kills (All Classes): {total_kills}")

print("--------------------------------------")

scoutp = tf2.get_playtime_as_class('Scout')
heavyp = tf2.get_playtime_as_class('Heavy')
pyrop = tf2.get_playtime_as_class('Pyro')
spyp = tf2.get_playtime_as_class('Spy')
medicp = tf2.get_playtime_as_class('Medic')
sniperp = tf2.get_playtime_as_class('Sniper')
soldierp = tf2.get_playtime_as_class('Soldier')
engineerp = tf2.get_playtime_as_class('Engineer')
demomanp = tf2.get_playtime_as_class('Demoman')

print(f"""
Scout playtime: {scoutp}
Heavy Playtime: {heavyp}
Pyro Playtime: {pyrop}
Spy Playtime: {spyp}
Medic Playtime: {medicp}
Sniper Playtime: {sniperp}
Soldier Playtime: {soldierp}
Engineer Playtime: {engineerp}
Demoman Playtime: {demomanp}
""")

print("--------------------------------------")

print(f"""
PyPi Page: {tf2.pypi_page}
Github Page: {tf2.github_page}
""")
```