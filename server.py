import json
import asyncio
import websockets

class ChatServer:
    def __init__(self):
        # Initialize data structure for connected clients here

    async def broadcast(self, message, message_type):
        """
        Broadcast received message to all connected clients
        """
        # Implement broadcast logic here

    async def send_custom_response(self, recipant_name, sender_name, message):
        """
        Send custom message to specific client
        """
        # Implement send_custom_response logic here

    async def handle_client(self, client, path):
        """
        Handle connected client, receive messages, and broadcast or send custom message
        """
        # Implement handle_client logic here

    def run(self):
        start_server = websockets.serve(self.handle_client, "localhost", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    chat_server = ChatServer()
    chat_server.run()
