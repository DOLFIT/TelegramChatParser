from telethon import TelegramClient, functions, sync
import config 

client = TelegramClient("Get Chats", config.api_id, config.api_hash)

with open("end.txt", "r", encoding="utf-8") as file:
	ends = file.read().split("\n")
	
with open("words.txt", "r", encoding="utf-8") as file:
	names = file.read().split("\n")

client.start()
print('soft download from github.com/DOLFIT/TelegramChatParser')
print('if soft not work - search update in github')

old = []
with open("chats.txt", "w", encoding="utf-8") as file:
	print("Run script...")
	for title in names:
		for end in ends:
			name = title + end
			print("Search chat with name: ", name)
			name = name.lower()
			request = client(functions.contacts.SearchRequest(q=name,limit=10))
			for channel in request.chats:
				if channel.megagroup:
					username = channel.username.lower() if channel.username is not None else ""
					if username not in old:
						if channel.title not in old:
							print(f"Found chat: t.me/{channel.username}")
							file.write(f"t.me/{channel.username}\n")
							old.append(channel.username)
							print("Chat: ", channel.title)
print("Stopped...")