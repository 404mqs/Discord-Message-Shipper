import requests
import time
import random

repeats = int(input("[?] How many times do you want to send the message?"))
cooldown = int(input("[?] How many interval do you want between each message?"))
message = input("[?] Which message do you want to send?")
token = input("[?] Token: ")
channel = input("[?] Channel/DM Id: ")

for i in range(0,repeats): 

    requests.post(
        f"https://discord.com/api/channels/{channel}/messages",
        data = {'content': message},
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : token
        }
    )

    time.sleep(cooldown)

print("[+] Messages sent successfully")


