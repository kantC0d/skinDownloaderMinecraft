#this project is using python 3.6.1
import requests
import base64
import json

#ask the user for a minecraft username
username = input("\nEnter a valid Minecraft username: ")

#get the minecraft uuid of the user
r = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(username)).json()

uuid = r["id"]

#get the minecraft skin of the user
r = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/{}'.format(uuid)).json()

#get the value (base64)
value = r["properties"][0]["value"]

#decode base64
value = json.loads(str(base64.b64decode(value), 'utf-8'))
#get the skin URL
skinURL = value["textures"]["SKIN"]["url"]

#download skin from skin url
r = requests.get(skinURL, allow_redirects=True)
open(username + ".png", 'wb').write(r.content)


#print user username and uuid
print("\n\nUsername: " + username)
print("UUID: " + uuid)
#print skin url
print("\nSkin URL: " + skinURL)
