```python
import asyncio
from aiohttp import web
from src.chatroom.chatroom_config import CHATROOM_CONFIG
from src.chatroom.chatroom_utils import format_message, parse_message
from src.chatroom.message_schema import MessageSchema

class VirtualChatroom:
    def __init__(self):
        self.users = {}
        self.message_schema = MessageSchema()

    async def register(self, websocket):
        user_id = id(websocket)
        self.users[user_id] = websocket
        return user_id

    async def unregister(self, user_id):
        del self.users[user_id]

    async def notify_users(self, message):
        if self.users:
            message = format_message(message)
            await asyncio.wait([user.send(message) for user in self.users.values()])

    async def handle_message(self, websocket, path):
        user_id = await self.register(websocket)
        try:
            async for message in websocket:
                message = parse_message(message)
                if self.message_schema.validate(message):
                    await self.notify_users(message)
        finally:
            await self.unregister(user_id)

    def run(self):
        start_server = web.WebSocketResponse(self.handle_message, CHATROOM_CONFIG['host'], CHATROOM_CONFIG['port'])
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    chatroom = VirtualChatroom()
    chatroom.run()
```