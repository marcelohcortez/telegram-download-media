import asyncio
from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeVideo

# Set up Telegram API credentials
api_id = TELEGRAM_API_KEY  #put you telegram API key here
api_hash = 'TELEGRAM_API_HASH' #put yout telegram API hash here
client = TelegramClient('session_name', api_id, api_hash)

# Define a function to download media files
async def download_media(message):
    try:
        # Check if the message contains media
        if message.media is not None:
            # Check if the media is an image, video or GIF
            if hasattr(message.media, 'photo') or hasattr(message.media, 'document') and isinstance(message.media.document.attributes[0], DocumentAttributeVideo) or hasattr(message.media, 'document') and message.media.document.mime_type.split("/")[0] == 'image' and message.media.document.mime_type.split("/")[1] == 'gif':
                # Download the media file
                file = await client.download_media(message.media)
                print(f"Downloaded media: {file}")
    except Exception as e:
        print(f"Error downloading media: {e}")

# Define an async function to iterate over messages and download media files
async def download_all_media():
    try:
        # Log in to the Telegram API
        await client.start()

        # Get the group or channel entity
        entity = await client.get_entity('name_code_from_group_chat') #insert here the name or code for the chat/group which you want to download media from

        # Iterate over the messages and download media files
        async for message in client.iter_messages(entity):
            await download_media(message)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Log out of the Telegram API
        await client.disconnect()

# Define and call an async function to run the script
async def main():
    await download_all_media()

# Call the main function inside an async function
async def run():
    await main()

asyncio.run(run())