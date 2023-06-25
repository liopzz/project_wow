from telethon import TelegramClient, events 
import re 
import asyncio 
from loguru import logger 

my_channel_id = -1001919719483
trix_channels = -1001786849294
ezcash_channels = -1001786849294
zooma_channels = -1001786849294
client = TelegramClient('session', api_id=29101580, api_hash='411c73eaa0b66447a571c6b0f4567588') #ставишь свой api_id и api_hash (api_id = 432, api_hash = '43242345234525435343') - пример

msg_list = ['sdfsdf']
with open("baza.txt", "r", encoding="utf8") as f:
    all_baza_msg = f.read().split('\n')

async def send_promo_trix(i, client):
 if i not in all_baza_msg and i not in msg_list and 'https' not in i:
    i = i.replace(" ", "")
    if len(i) < 8 or len(i) > 9: 
        return
    with open("baza.txt", "a", encoding="utf8") as f:
        f.write(f"{i}\n")
        code = await client.send_message(my_channel_id, f'`{i}`')
        await asyncio.sleep(5) 
        newmessage = f'`{i}`\n\n**🥇 trix - https://trx.direct/refs/979386**' #ставишь свою реф
        await client.edit_message(my_channel_id, code.id, newmessage, parse_mode='md', link_preview=False)
        msg_list.append(i)

async def send_promo_ezcash(i, client):
  if i not in all_baza_msg and i not in msg_list:
    with open("baza.txt", "a", encoding="utf8") as f:
        f.write(f"{i}\n") 
        code = await client.send_message(my_channel_id, f'`{i}`')
        await asyncio.sleep(5) 
        newmessage = f'`{i}`\n\n💎 ez-cash - https://ezcash.gg/r/o5AnPF' #ставишь свою реф
        await client.edit_message(my_channel_id, code.id, newmessage, parse_mode='md', link_preview=False)
        msg_list.append(i)
async def send_promo_zooma(i, client):
  if i not in all_baza_msg and i not in msg_list:
    with open("baza.txt", "a", encoding="utf8") as f:
        f.write(f"{i}\n") 
        code = await client.send_message(my_channel_id, f'`{i}`')
        await asyncio.sleep(5) 
        newmessage = f'`{i}`\n\n⚡️ zooma - https://zref.cc/239005' #ставишь свою реф
        await client.edit_message(my_channel_id, code.id, newmessage, parse_mode='md', link_preview=False)
        msg_list.append(i)
@client.on(events.NewMessage(chats=trix_channels))
async def Messages(message):
    if 'step' in message.text.lower():
        return
    if 'youtu' in message.text.lower():
        return
    if 'color' in message.text.lower():
        return
    if 'cat' in message.text.lower():
        return
    if '@' in message.text.lower():
        return
    if 't.me' in message.text.lower():
        return
    for i in re.findall(r'\b[a-zA-z0-9 ]{8,9}\b', message.text):
        await send_promo_trix(i, client)

@client.on(events.NewMessage(chats=ezcash_channels))
async def Messages(message):
    for i in re.findall(r'[EZ]{2}-[A-Z0-9]{6}-[SH]{2}', message.text):
            await send_promo_ezcash(i, client)
@client.on(events.NewMessage(chats=zooma_channels))
async def Messages(message):
    for i in re.findall(r'[ZM]{2}_[a-zA-Z0-9]{4,20}', message.text):
            await send_promo_zooma(i, client)
                    
client.start() 
client.run_until_disconnected()
