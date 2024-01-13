from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
import json

# Replace the following values with your own bot token
api_id = '18730450'
api_hash = '7e38d906ceeea918c77787290ca15255'
bot_token = '6884816078:AAGyQzMzeO26HW-oJEEt41S_ieqLFdkedGw'
from_channels = []
to_channels = []
# Create a new Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a handler for the /start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    user = message.from_user
    await message.reply_text(f"<b>👋🏻 Welcome!  <a href='tg://user?id={user.id}'>{user.first_name}</a></b>\n\nI am Auto Forwarder Bot. Add me to your channel as admin to make me forward the channels's messages.\n\nYoy can use this format to add new channel to forward.\n-> /add from_channel_id to_channel_id\nExample: <code>/add -1001597505131 -1001653503167</code>")
@app.on_message(filters.private)    
def add_channel(client, message):
	if "/add" in message.text:
		id = message.text.split(" ")
		from_channels.append(int(id[1]))
		to_channels.append(int(id[2]))
		message.reply_text(f"<b>✅ {id[1]} to {id[2]} added successfully in database for forwarding tasks.</b>")
		print(f"🛅 Database Updated:\n\nFrom Channel List: {from_channels}\nTo Channels List: {to_channels}")
@app.on_message(filters.channel)
async def forward_message(client, message):
    	print(message.chat.id)
    	print(from_channels)
    	if message.chat.id in from_channels:
    		to_num=-1
    		print("True, Now Forwarding...")
    		for i in from_channels:
    			to_num+=1
    			if message.chat.id == i:
    				print(f"Forwarding from {i} to {to_channels[to_num]}")
    				await message.copy(int(to_channels[to_num]))
    #message.reply_text(f"Updates: <code>{message.forward_from_chat}</code>")
# Start the client
print("Status: Online")
app.run()
